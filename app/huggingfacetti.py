from huggingface_hub import login, InferenceClient
from app.banner import generate_banner
from app.utils import save_uploaded_file, allowed_file
import os
from PIL import Image

def generate_and_save_banner(files, offer, theme, color_palette, generator_type, format='PNG', size=None):
    filenames = []
    for file in files:
        if not allowed_file(file.filename):
            return {'error': 'Invalid file type'}
        filenames.append(save_uploaded_file(file))
    
    # Generate banner prompt with analyzed image data
    image, banner_prompt = generate_banner(filenames, offer, theme, color_palette, generator_type)

    # Resize the image if size is provided
    if size:
        image = image.resize(size)
    
    # Save the image with a unique identifier
    import time
    timestamp = int(time.time())
    image_filename = f"generated_banner_{timestamp}.{format.lower()}"
    image_path = os.path.join("static", "generated", image_filename)
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    
    if generator_type == 'huggingface':
        image.save(image_path, format=format)
    elif generator_type == 'imagen':
        with open(image_path, 'wb') as f:
            f.write(image._image_bytes)
    
    result = {
        'message': "Banner generated and saved",
        'prompt': banner_prompt,
        'image_path': f'/static/generated/{image_filename}',
        'format': format
    }
    if size:
        result['size'] = size

    return result

