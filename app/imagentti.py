import os
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
from dotenv import load_dotenv
from PIL import Image
import io
import time

load_dotenv()
PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')

def generate_with_imagen(prompt, format='PNG', size=None):
    vertexai.init(project=PROJECT_ID, location="us-central1")
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

    images = model.generate_images(
        prompt=prompt,
        number_of_images=1,
        language="en",
        aspect_ratio="1:1",
        safety_filter_level="block_some",
        person_generation="allow_adult",
    )

    if hasattr(images[0], '_image_bytes'):
        pil_image = Image.open(io.BytesIO(images[0]._image_bytes))
    else:
        raise ValueError("Failed to retrieve image from Imagen.")

    if size:
        pil_image = pil_image.resize(size)

    timestamp = int(time.time())
    image_filename = f"generated_banner_{timestamp}.{format.lower()}"
    image_path = os.path.join("static", "generated", image_filename)
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    pil_image.save(image_path, format=format)

    return image_path, images[0]._generation_parameters
