import os
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
output_file = "image.png"
prompt = """


## Big Basket Champions League Combo Offer Banner Design

**1. Theme Influence:**

The banner draws inspiration from the UEFA Champions League by using a dynamic, stadium-like background with overlaid spotlights. This energetic theme evokes the excitement of the tournament and connects it to the thrill of scoring amazing deals on Big Basket.

**2. Layout and Arrangement:**

- **Top:** The banner prominently features the Big Basket logo on the top left corner, ensuring immediate brand recognition.
- **Center:** The main headline, Score Big with Champions League Combos, dominates the center in bold white font, grabbing attention and clearly communicating the offer.
- **Below Headline:** Two product showcase sections are placed side-by-side, each highlighting one combo offer:
    - **Left:** Features an enticing image of Lays chips with the tagline Crunchy Goals, Delicious Wins!      
    - **Right:** Displays a refreshing image of Maaza bottles with the tagline Quench Your Thirst for Victory!- **Bottom:** A clear call to action, Order Your Combo Now, is placed within a rectangular button with the Big Basket brand color (green) for emphasis.

**3. Color Palette and Product Colors:**

- The banner utilizes the provided red, blue, green, and teal palette, drawing from the UEFA Champions League 
branding and creating a visually appealing contrast.
- The green background subtly reinforces the Big Basket brand while allowing the product images and offer text to pop.
- The red and blue hues in the background echo the Lays and Maaza packaging, creating a harmonious visual connection.

**4. Notable Design Elements:**

- The spotlight effects in the background add a sense of dynamism and excitement, mirroring the energy of the 
UEFA Champions League.
- The product images are slightly tilted to create a sense of movement and urgency.
- The use of bold, sans-serif fonts ensures readability and adds to the modern, sporty aesthetic.

**5. Big Basket Branding:**

- The Big Basket logo is prominently placed in the top left corner, ensuring immediate brand recognition.     
- The brands signature green is used for the call-to-action button, further reinforcing the association between the offer and Big Basket.
- The overall design language is consistent with Big Baskets brand identity, maintaining a clean, professional, and approachable aesthetic.

This banner design effectively leverages the UEFA Champions League theme to create a visually engaging and persuasive promotion for Big Baskets combo offer. The clear layout, strategic use of color, and dynamic elements 
work together to capture attention and drive conversions.


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