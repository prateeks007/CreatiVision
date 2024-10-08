import google.generativeai as genai
import logging
import os
from dotenv import load_dotenv
from app.analyze_image import analyze_image
from abc import ABC, abstractmethod

load_dotenv()

class ImageGenerator(ABC):
    @abstractmethod
    def generate_image(self, prompt):
        pass

class HuggingFaceGenerator(ImageGenerator):
    def __init__(self):
        from huggingface_hub import login, InferenceClient
        login(token=os.getenv('HUGGING_FACE_API_KEY'))
        self.client = InferenceClient()

    def generate_image(self, prompt):
        return self.client.text_to_image(
            prompt,
            num_inference_steps=100,
            guidance_scale=7.5
        )

class GoogleImagenGenerator(ImageGenerator):
    def __init__(self):
        import vertexai
        from vertexai.preview.vision_models import ImageGenerationModel
        project_id = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
        vertexai.init(project=project_id, location="us-central1")
        self.model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

    def generate_image(self, prompt):
        images = self.model.generate_images(
            prompt=prompt,
            number_of_images=1,
            language="en"
        )
        return images[0]

def get_image_generator(generator_type):
    if generator_type == 'huggingface':
        return HuggingFaceGenerator()
    elif generator_type == 'imagen':
        return GoogleImagenGenerator()
    else:
        raise ValueError(f"Unknown generator type: {generator_type}")

def generate_banner(filenames, offer, theme, color_palette, generator_type):
    logging.info(f"Generating banner prompt for offer: {offer}")
    
    product_descriptions = []
    for filename in filenames:
        image_analysis = analyze_image(filename)
        main_product = image_analysis['labels'][0]
        colors = image_analysis.get('colors', [])
        objects = image_analysis.get('objects', [])
        texts = image_analysis.get('texts', [])
        logos = image_analysis.get('logos', [])
        
        product_description = f"Product: {main_product}\n"
        product_description += f"Specific Description: {', '.join(objects[:3])}\n"
        product_description += f"Colors: {', '.join(colors[:3])}\n"
        product_description += f"Text on Product: {', '.join(texts[:3])}\n"
        product_description += f"Logos: {', '.join(logos[:3])}\n"
        product_descriptions.append(product_description)

    products_info = "\n".join(product_descriptions)
    
    main_products = ', '.join([desc.split('\n')[0].split(': ')[1] for desc in product_descriptions])
    dominant_colors = ', '.join(set(color for desc in product_descriptions for color in desc.split('\n')[2].split(': ')[1].split(', ')[:2]))

    # print("%%%%%%%%%%%%%%" + main_products + products_info )

    prompt = f"""
    Design a professional promotional banner for Big Basket, an Indian online grocery delivery service.

    Theme: {theme}
    The theme should guide the overall design and inspire a catchy headline.

    Color Palette: {", ".join(color_palette)}
    Offer: {offer}

    Products:
    {products_info} This is the main thing to be included in the banner.

    Banner Elements:
    
    1. Main Heading: Create a creative and catchy heading that incorporates the essence of "{theme} Special" without using these exact words. Make it engaging and relevant to Big Basket's offerings.
    2. Product Showcase: Prominently display ONLY the main product(s) mentioned above: {main_products}. Do not add or showcase any products that are not listed here. Ensure accurate representation of each product's specific appearance, including color and packaging details. Do not add any text or modifications to the product packaging itself.
    3. Offer Display: Use exactly this text for the offer: "{offer}"
    4. Call to Action: Include a clear call-to-action phrase encouraging users to shop at BigBasket
    5. Background: Design a background that complements the theme and product colors.
    6. Big Basket Logo: Include the text "Big Basket" in a logo-like format.

    Design Guidelines:
    - Use the provided color palette throughout the banner
    - Incorporate the dominant colors from the product images: {dominant_colors}
    - Maintain a clear visual hierarchy with the main eye-catching text as a focal point, but not centrally located
    - Ensure all text is legible
    - Optimize the layout for quick comprehension
    - Make sure the Big Basket branding is clearly visible and recognizable

    Important:
    - Headline should never be at the Center of the banner.
    - Do not alter product packaging or branding
    - Maintain a professional and clear message
    - Incorporate any visible text or logos from the product images if relevant
    - Ensure the Big Basket logo or text is a key element of the banner
    - Accurately represent each product's specific appearance, including exact packaging details and colors
    - Use only the exact text provided for headings, offer.
    - Do not add any text or modifications to the product packaging itself
    - Do not include any products that are not mentioned in the product list above

    Provide a concise description of the banner design, focusing on:
    1. The catchy headline created and how it relates to the theme
    2. How the theme influences the overall design
    3. The layout and arrangement of key elements, including the Big Basket logo and the specific products ({main_products})
    4. Use of the color palette and product colors, emphasizing the accurate representation of product packaging colors
    5. Any notable design elements inspired by the product images
    6. How the Big Basket branding is integrated into the design
    7. Accurate representation of each product's specific packaging and appearance, including exact colors
    8. Exact placement and representation of the provided text elements
    """

    model = genai.GenerativeModel('models/gemini-1.5-pro')
    response = model.generate_content(prompt)
    generated_text = response.text if hasattr(response, 'text') else str(response)
    
    # Remove any quotes from the generated text
    generated_text = generated_text.replace('"', '').replace("'", "")
    
    print(generated_text)
    
    generator = get_image_generator(generator_type)
    image = generator.generate_image(generated_text)
    
    return image, generated_text 