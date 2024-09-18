from huggingface_hub import login, InferenceClient
from app.banner import generate_banner
from app.utils import save_uploaded_file, allowed_file
import os

def generate_and_save_banner(file, offer, theme, color_palette):
    if not allowed_file(file.filename):
        return {'error': 'Invalid file type'}

    filename = save_uploaded_file(file)
    
    # Generate banner prompt
    banner_prompt = generate_banner(filename, offer, theme, color_palette)

    # Login to Hugging Face
    login(token=os.getenv('HUGGING_FACE_API_KEY'))

    # Specify the model you want to use
    # model_name = "black-forest-labs/FLUX.1-dev"  # You can change this to any supported model
   
    # model_name = "stabilityai/stable-diffusion-2"

    # Initialize the client with the specific model
    client = InferenceClient()

    # Use the generated prompt for text-to-image generation with additional parameters
    image = client.text_to_image(
        banner_prompt,
        num_inference_steps=100,
        guidance_scale=7.5
    )
    
    # Save the image with a unique identifier
    import time
    timestamp = int(time.time())
    image_filename = f"generated_banner_{timestamp}.png"
    image_path = os.path.join("static", "generated", image_filename)
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    image.save(image_path)

    return {
        'message': "Banner generated and saved",
        'prompt': banner_prompt,
        'image_path': f'/static/generated/{image_filename}'
    }

