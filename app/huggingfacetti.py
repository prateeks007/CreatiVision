from huggingface_hub import InferenceClient
from app.banner import generate_banner
from app.utils import save_uploaded_file, allowed_file
import os
from PIL import Image
import io
import time

def generate_and_save_banner(files, offer, theme, color_palette, generator_type, format='PNG', size=None):
    filenames = []
    for file in files:
        if not allowed_file(file.filename):
            return {'error': 'Invalid file type'}
        filenames.append(save_uploaded_file(file))

    # CALL generate_banner: returns ONLY 2 things
    image, banner_prompt = generate_banner(filenames, offer, theme, color_palette, generator_type)

    # Determine if fallback was used based on the prompt (hacky but effective)
    fallback_used = "a cute cat" in banner_prompt.lower() or "default" in banner_prompt.lower()
    warnings = []
    if fallback_used:
        warnings.append("Image analysis failed (Google Vision & Hugging Face). Used default caption.")

    # Convert GeneratedImage to PIL Image if necessary
    if hasattr(image, '_image_bytes'):
        pil_image = Image.open(io.BytesIO(image._image_bytes))
    elif isinstance(image, Image.Image):
        pil_image = image
    else:
        return {'error': 'Unsupported image format'}

    if size:
        pil_image = pil_image.resize(size)

    timestamp = int(time.time())
    image_filename = f"generated_banner_{timestamp}.{format.lower()}"
    image_path = os.path.join("static", "generated", image_filename)
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    pil_image.save(image_path, format=format)

    return {
        'message': "Banner generated and saved",
        'prompt': banner_prompt,
        'image_path': f'/static/generated/{image_filename}',
        'format': format,
        'fallback_used': fallback_used,
        'warnings': warnings,
        'size': size if size else None
    }
