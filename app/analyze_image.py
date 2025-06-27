import os
from dotenv import load_dotenv
from PIL import Image
import requests
from google.api_core.exceptions import PermissionDenied

load_dotenv()

def analyze_image(path, generator_type='imagen'):
    warnings = []

    # Try Google Vision
    try:
        from google.cloud import vision
        client = vision.ImageAnnotatorClient()
        with open(path, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = client.annotate_image({
            'image': image,
            'features': [
                {'type_': vision.Feature.Type.LABEL_DETECTION},
                {'type_': vision.Feature.Type.OBJECT_LOCALIZATION},
                {'type_': vision.Feature.Type.IMAGE_PROPERTIES},
                {'type_': vision.Feature.Type.TEXT_DETECTION},
                {'type_': vision.Feature.Type.LOGO_DETECTION},
            ]
        })
        labels = response.label_annotations
        objects = response.localized_object_annotations
        texts = response.text_annotations
        logos = response.logo_annotations

        pil_img = Image.open(path)
        colors = pil_img.getcolors(pil_img.size[0] * pil_img.size[1]) or [(0,(255,255,255))]
        dominant = max(colors, key=lambda x: x[0])[1]

        return {
            'description': ' '.join(l.description for l in labels[:3]),
            'labels': [l.description for l in labels],
            'objects': [o.name for o in objects],
            'dominant_color': f"rgb{dominant}",
            'text': ' '.join(t.description for t in texts[1:3]) if texts else '',
            'logos': [logo.description for logo in logos],
            'fallback_used': False,
            'warnings': warnings
        }

    except Exception as err:
        msg = "[Google Vision failed]: Billing might not be enabled or credentials are invalid."
        print(msg, err)
        warnings.append(msg)

    # Try Hugging Face captioning
    try:
        with open(path, 'rb') as f:
            img_bytes = f.read()
        resp = requests.post(
            "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning",
            headers={"Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_KEY')}"},
            files={"file": img_bytes},
            timeout=60
        )
        if resp.status_code != 200:
            raise RuntimeError(f"HF API error {resp.status_code}: {resp.text}")
        data = resp.json()
        caption = data[0]['generated_text'] if isinstance(data, list) else data.get('generated_text') or str(data)

        pil_img = Image.open(path)
        colors = pil_img.getcolors(pil_img.size[0] * pil_img.size[1]) or [(0,(255,255,255))]
        dominant = max(colors, key=lambda x: x[0])[1]

        return {
            'description': caption,
            'labels': [caption],
            'objects': [],
            'dominant_color': f"rgb{dominant}",
            'text': '',
            'logos': [],
            'fallback_used': False,
            'warnings': warnings
        }

    except Exception as e2:
        msg = "[Hugging Face fallback failed]: No inference access or invalid API key."
        print(msg, e2)
        warnings.append(msg)

    # Final fallback
    fallback_msg = "[No providers available — using default prompt with user data]"
    print(fallback_msg)
    warnings.append(fallback_msg)

    return {
        'description': 'A cute cat on a sunny day',
        'labels': ['cat', 'cute', 'sunny'],
        'objects': [],
        'dominant_color': 'rgb(255, 255, 255)',
        'text': '',
        'logos': [],
        'fallback_used': True,
        'warnings': warnings
    }
