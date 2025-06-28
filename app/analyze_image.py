import os
from dotenv import load_dotenv
from PIL import Image
import requests
from google.api_core.exceptions import GoogleAPICallError, PermissionDenied

load_dotenv()

def analyze_image(path):
    """
    Try Google Vision first, then HF captioning, then fallback.
    Returns dict with description, labels, objects, dominant_color, text, logos,
    fallback_used(bool) and warnings(list).
    """
    warnings = []

    # 1) Google Vision
    try:
        from google.cloud import vision
        client = vision.ImageAnnotatorClient()
        with open(path, "rb") as f:
            content = f.read()
        image = vision.Image(content=content)
        features = [
            vision.Feature(type_=vision.Feature.Type.LABEL_DETECTION),
            vision.Feature(type_=vision.Feature.Type.OBJECT_LOCALIZATION),
            vision.Feature(type_=vision.Feature.Type.IMAGE_PROPERTIES),
            vision.Feature(type_=vision.Feature.Type.TEXT_DETECTION),
            vision.Feature(type_=vision.Feature.Type.LOGO_DETECTION),
        ]
        response = client.annotate_image({"image": image, "features": features})

        labels = [l.description for l in response.label_annotations]
        objects = [o.name for o in response.localized_object_annotations]
        texts = [t.description for t in response.text_annotations]
        logos = [l.description for l in response.logo_annotations]

        # dominant color
        pil = Image.open(path)
        colors = pil.getcolors(pil.size[0] * pil.size[1]) or [(0, (255,255,255))]
        dominant = max(colors, key=lambda x: x[0])[1]

        return {
            "description": " ".join(labels[:3]),
            "labels": labels,
            "objects": objects,
            "dominant_color": f"rgb{dominant}",
            "text": " ".join(texts[1:3]) if len(texts)>1 else "",
            "logos": logos,
            "fallback_used": False,
            "warnings": warnings,
        }
    except (GoogleAPICallError, PermissionDenied) as e:
        msg = "[Google Vision failed]: billing or credentials issue"
        warnings.append(f"{msg}: {e.message if hasattr(e,'message') else str(e)}")
    except Exception as e:
        warnings.append(f"[Google Vision failed]: {str(e)}")

    # 2) HF captioning
    try:
        with open(path, "rb") as f:
            img_bytes = f.read()
        resp = requests.post(
            "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning",
            headers={"Authorization": f"Bearer {os.getenv('HUGGING_FACE_API_KEY')}"},
            files={"file": img_bytes},
            timeout=60,
        )
        if resp.status_code != 200:
            raise RuntimeError(f"HF API {resp.status_code}: {resp.text[:100]}")

        data = resp.json()
        caption = (
            data[0]["generated_text"]
            if isinstance(data, list) and "generated_text" in data[0]
            else data.get("generated_text", str(data))
        )

        pil = Image.open(path)
        colors = pil.getcolors(pil.size[0] * pil.size[1]) or [(0,(255,255,255))]
        dominant = max(colors, key=lambda x: x[0])[1]

        return {
            "description": caption,
            "labels": [caption],
            "objects": [],
            "dominant_color": f"rgb{dominant}",
            "text": "",
            "logos": [],
            "fallback_used": False,
            "warnings": warnings,
        }
    except Exception as e:
        warnings.append(f"[HF caption failed]: {str(e)}")

    # 3) Final fallback
    warnings.append("[No providers available — using default caption]")
    return {
        "description": "A cute cat on a sunny day",
        "labels": ["cat", "cute", "sunny"],
        "objects": [],
        "dominant_color": "rgb(255,255,255)",
        "text": "",
        "logos": [],
        "fallback_used": True,
        "warnings": warnings,
    }
