import os
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
output_file = "image.png"
prompt = """

## Big Basket: Interstellar Grocery Run

**1. Catchy Headline:** Launch Your Taste Buds into Orbit! This headline captures the essence of the interstellar theme while relating it to the excitement of exploring new flavors and enjoying Big Baskets grocery 
offerings.

**2. Theme Influence:** The overall design is inspired by the vastness and mystery of space. A dark, starry background with swirling nebulas of purple, blue, and orange creates an otherworldly atmosphere.

**3. Layout:**

* **Top Left:** Launch Your Taste Buds into Orbit! in bold, white text with a subtle glow effect.
* **Bottom Right:**  Big Basket logo in its signature orange and green colors, slightly enlarged for prominence.
* **Center:** A cluster of the specified products: A bag of Lays chips angled dynamically and a Pepsi can with condensation, both realistically rendered with accurate packaging colors and logos.
* **Below Products:** combo offer in smaller, red text.
* **Right of Products:** Shop Now at BigBasket.com within a vibrant green button with rounded edges.       

**4. Color Palette:** The background utilizes the provided blue, purple, and orange hues in a cosmic swirl, evoking nebulae. The product colors - red (Lays) and blue (Pepsi) - pop against the dark background and are further emphasized by subtle glow effects.

**5. Product-Inspired Design:**  The Lays bag is angled as if floating in zero gravity, while the Pepsi can features realistic condensation, adding to the dynamic, out-of-this-world feel.

**6. Big Basket Branding:** The signature orange and green Big Basket logo is prominently displayed in the 
bottom right corner, instantly recognizable and reinforcing brand identity.

**7. Product Representation:** Products are displayed with meticulous attention to detail. The Lays bag accurately reflects its packaging, including the logo, color scheme, and bag texture. Similarly, the Pepsi can is faithfully recreated with accurate branding, color, and even the condensation effect for added realism.
**8. Text Placement:**
* combo offer is placed directly below the product cluster in a smaller font size, clearly associated with 
the displayed items.
*  Shop Now at BigBasket.com is incorporated within a clear call-to-action button to the right of the products, prompting immediate action.

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