import os
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
output_file = "image.png"
prompt = """


Create a promotional banner for Big Basket featuring Lays chips and a Pepsi can.

Theme: Attack on Titan (without mentioning the name directly)
Headline: Colossal Grocery Assault: 50% Off Your Favorite Provisions!
Color Palette: Red, Blue, Green (reference Big Basket branding)
Products: Lays Chips, Pepsi Cans (with accurate packaging)
Layout: Catchy headline in center, Big Basket logo top left, product images with call to action on bottom right.
Style: Action-oriented, dynamic background with subtle manga influences.

Important: Ensure the text is placed above or beside the product images. Avoid placing text directly on the product packaging.

"""

vertexai.init(project=PROJECT_ID, location="us-central1")

model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

images = model.generate_images(
    prompt=prompt,
    # Optional parameters
    number_of_images=1,
    language="en",
    # You can't use a seed value and watermark at the same time.
    # add_watermark=False,
    # seed=100,
    aspect_ratio="1:1",
    safety_filter_level="block_some",
    person_generation="allow_adult",
)

images[0].save(location=output_file, include_generation_parameters=False)

# Optional. View the generated image in a notebook.
# images[0].show()

print(f"Created output image using {len(images[0]._image_bytes)} bytes")
# Example response:
# Created output image using 1234567 bytes