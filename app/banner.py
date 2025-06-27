import os, logging
from dotenv import load_dotenv
from app.analyze_image import analyze_image
import google.generativeai as genai
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
        try:
            return self.client.text_to_image(prompt, num_inference_steps=100, guidance_scale=7.5)
        except Exception as e:
            logging.error("[HF image gen failed]: %s", e)
            raise

class GoogleImagenGenerator(ImageGenerator):
    def __init__(self):
        import vertexai
        from vertexai.preview.vision_models import ImageGenerationModel
        vertexai.init(project=os.getenv('GOOGLE_CLOUD_PROJECT_ID'), location="us-central1")
        self.model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

    def generate_image(self, prompt):
        try:
            return self.model.generate_images(prompt=prompt, number_of_images=1, language="en")[0]
        except Exception as e:
            logging.error("[Imagen gen failed]: %s", e)
            raise

def get_image_generator(generator_type):
    if generator_type == 'huggingface':
        return HuggingFaceGenerator()
    elif generator_type == 'imagen':
        return GoogleImagenGenerator()
    else:
        raise ValueError(f"Unknown generator type: {generator_type}")

def generate_banner(filenames, offer, theme, color_palette, generator_type):
    product_descs = []
    for fname in filenames:
        analysis = analyze_image(fname, generator_type)
        product_descs.append(
            f"Product: {analysis['labels'][0] if analysis['labels'] else 'item'}\n"
            f"Objects: {', '.join(analysis.get('objects', [])[:3])}\n"
            f"Colors: {analysis.get('dominant_color')}\n"
            f"Text: {analysis.get('text')}\n"
            f"Logos: {', '.join(analysis.get('logos', [])[:3])}\n"
        )

    products_info = "\n".join(product_descs)
    main_products = ', '.join(d.split('\n')[0].split(': ')[1] for d in product_descs)
    domcolor = ', '.join(set(d.split('\n')[2].split(': ')[1] for d in product_descs))

    prompt = f"""Design a banner:
Theme: {theme}
Offer: {offer}
Colors: {', '.join(color_palette)}
Products: {products_info}
Main products: {main_products}
Product colors: {domcolor}
"""

    # Generate description using Gemini but allow fallback
    banner_text = ''
    try:
        model = genai.GenerativeModel('models/gemini-1.5-pro')
        resp = model.generate_content(prompt)
        banner_text = getattr(resp, 'text', str(resp)).replace('"', '')
    except Exception as e:
        logging.error("[Banner text gen failed]: %s", e)
        banner_text = f"{offer} - {theme} banner featuring {main_products}"

    generator = get_image_generator(generator_type)
    try:
        image = generator.generate_image(banner_text)
    except Exception as e:
        logging.error("[Image generation failed]: %s", e)
        return None, banner_text

    return image, banner_text
