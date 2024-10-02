import os
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
output_file = "image.png"
prompt = """


## Big Basket: Interstellar Snack Attack!

**1. Catchy Headline & Theme:** Interstellar Snack Attack! uses the interstellar theme with a playful twist to connect it to grocery shopping. It suggests an out-of-this-world snacking experience with Big Basket.  

**2. Theme Influence:** The banner features a stylized depiction of outer space with swirling nebulas and twinkling stars in shades of red, blue, green, purple, and orange. This vibrant backdrop reinforces the interstellar theme while aligning with the specified color palette.

**3. Layout & Element Arrangement:**

* **Top Left:**  The Big Basket logo in its standard format.
* **Center:** Interstellar Snack Attack! in bold, large font, with a slight arc for dynamism.
* **Slightly Below Center:** A Lays chips bag and a Pepsi can are realistically rendered and prominently displayed, showcasing their actual packaging and colors.
* **Below Products:** combo offer in a smaller font, emphasizing the deal.
* **Below Lays:** Crunchy, satisfying goodness! in a fun font.
* **Below Pepsi:**  Out-of-this-world refreshment! in a similar fun font.
* **Bottom Right:** Shop Now at BigBasket.com  in a clear call to action button.

**4. Color Palette & Product Colors:**  The background nebula uses the specified colors with gradients to create depth. The dominant colors of the Lays bag (red, yellow) and Pepsi can (blue, red, white) are reflected in the nearby nebulas, subtly linking the products with the background.

**5.  Design Elements Inspired by Product Images:** The Lays bags wave design is subtly echoed in the surrounding nebula pattern, adding a visual connection without altering the product image itself.

**6. Big Basket Branding:** The Big Basket logo is prominently displayed in the top left corner, ensuring immediate brand recognition.

**7. Accurate Product Representation:** Both the Lays bag and Pepsi can are depicted with photographic accuracy, including their respective logos, color schemes, and packaging details. No modifications are made to 
the original product images.

**8. Text Placement:** All provided text elements (combo offer, Shop Now at BigBasket.com) are incorporated exactly as specified and positioned for optimal readability and impact.

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