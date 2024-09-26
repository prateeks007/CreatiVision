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
        product_description += f"Colors: {', '.join(colors[:3])}\n"
        product_description += f"Objects: {', '.join(objects[:3])}\n"
        product_description += f"Text: {', '.join(texts[:3])}\n"
        product_description += f"Logos: {', '.join(logos[:3])}\n"
        product_descriptions.append(product_description)

    products_info = "\n".join(product_descriptions)
    
    main_products = ', '.join([desc.split('\n')[0].split(': ')[1] for desc in product_descriptions])
    dominant_colors = ', '.join(set(color for desc in product_descriptions for color in desc.split('\n')[1].split(': ')[1].split(', ')[:2]))

    prompt = f"""
    Design a professional promotional banner for Big Basket, an Indian online grocery delivery service.

    Theme: {theme}
    The theme should guide the overall design.

    Color Palette: {", ".join(color_palette)}
    Offer: {offer}

    Products:
    {products_info}

    Banner Elements:
    1. Main Heading: Create a clear headline incorporating the theme {theme}.
    2. Product Showcase: Prominently display the main product(s): {main_products}.
    3. Offer Display: Present the offer {offer} clearly.
    4. Taglines: Create brief, relevant taglines for each product (5-7 words each).
    5. Call to Action: Include a clear call to action.
    6. Background: Design a background that complements the theme and product colors.
    7. Big Basket Logo: Incorporate the Big Basket logo or text prominently in the banner design.

    Design Guidelines:
    - Use the provided color palette throughout the banner
    - Incorporate the dominant colors from the product images: {dominant_colors}
    - Maintain a clear visual hierarchy
    - Ensure all text is legible
    - Optimize the layout for quick comprehension
    - Make sure the Big Basket branding is clearly visible and recognizable

    Important:
    - The design should be culturally appropriate for an Indian audience
    - Do not alter product packaging or branding
    - Maintain a professional and clear message
    - Incorporate any visible text or logos from the product images if relevant
    - Ensure the Big Basket logo or text is a key element of the banner

    Provide a concise description of the banner design, focusing on:
    1. How the theme influences the overall design
    2. The layout and arrangement of key elements, including the Big Basket logo and the specific products ({main_products})
    3. Use of the color palette and product colors
    4. Any notable design elements inspired by the product images
    5. How the Big Basket branding is integrated into the design
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