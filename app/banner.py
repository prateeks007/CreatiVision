import os, logging
from dotenv import load_dotenv
from app.analyze_image import analyze_image
import google.generativeai as genai
from abc import ABC, abstractmethod

load_dotenv()

# -- Image generator interface --
class ImageGenerator(ABC):
    @abstractmethod
    def generate_image(self, prompt):
        pass

class HuggingFaceGenerator(ImageGenerator):
    def __init__(self):
        from huggingface_hub import login, InferenceClient
        login(token=os.getenv("HUGGING_FACE_API_KEY"))
        self.client = InferenceClient()

    def generate_image(self, prompt):
        return self.client.text_to_image(prompt, num_inference_steps=100, guidance_scale=7.5)

class GoogleImagenGenerator(ImageGenerator):
    def __init__(self):
        import vertexai
        from vertexai.preview.vision_models import ImageGenerationModel
        vertexai.init(project=os.getenv("GOOGLE_CLOUD_PROJECT_ID"), location="us-central1")
        self.model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

    def generate_image(self, prompt):
        imgs = self.model.generate_images(prompt=prompt, number_of_images=1, language="en")
        return imgs[0]

def get_image_generator(generator_type):
    if generator_type == "huggingface":
        return HuggingFaceGenerator()
    elif generator_type == "imagen":
        return GoogleImagenGenerator()
    else:
        raise ValueError(f"Unknown generator type '{generator_type}'")

def generate_banner(filenames, offer, theme, color_palette, generator_type):
    """
    Returns (image_obj or None, banner_prompt:str, text_warnings:list)
    """
    text_warnings = []
    # 1) Build the prompt from analyzed images
    descs = []
    for f in filenames:
        analysis = analyze_image(f)
        # collect any analysis warnings
        text_warnings += analysis["warnings"]
        descs.append(
            f"Product: {analysis['labels'][0] if analysis['labels'] else 'item'} | "
            f"Colors: {analysis['dominant_color']} | "
            f"Objects: {', '.join(analysis['objects'][:3])}"
        )

    main_products = ", ".join(d.split("|")[0].split(":")[1].strip() for d in descs)
    products_info = " ; ".join(descs)

    banner_prompt = ""
    # 2) Try Gemini for a snazzy headline & description
    try:
        prompt = (
            f"Design a banner for offer '{offer}' with theme '{theme}', colors {color_palette}, "
            f"main products: {main_products}. Details: {products_info}"
        )
        model = genai.GenerativeModel("models/gemini-1.5-pro")
        resp = model.generate_content(prompt)
        banner_prompt = getattr(resp, "text", str(resp)).replace('"', "")
    except Exception as e:
        logging.error("[Banner text gen failed]: %s", e)
        text_warnings.append(f"[Gemini text gen failed]: {str(e)}")
        banner_prompt = f"{offer} - {theme} banner featuring {main_products}"

    # 3) Image generation
    image = None
    try:
        generator = get_image_generator(generator_type)
        image = generator.generate_image(banner_prompt)
    except Exception as e:
        logging.error("[Image generation failed]: %s", e)
        text_warnings.append(f"[Image gen '{generator_type}' failed]: {str(e)}")
        image = None

    return image, banner_prompt, text_warnings
