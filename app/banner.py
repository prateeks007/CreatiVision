import google.generativeai as genai
import logging
import os
from dotenv import load_dotenv

load_dotenv()

def generate_banner(filename, offer, theme, color_palette):
    logging.info(f"Generating banner prompt for offer: {offer}")
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    prompt = f"""Create a detailed input for a text-to-image model for a promotional banner design. 
    Product: '{filename}' (assume the product image is available and should remain unchanged).
    Offer: {offer}. 
    Theme: {theme}. 
    Color Palette: {', '.join(color_palette)}.

    Instructions:
    - The banner should be visually appealing and relevant to an Indian audience. 
    - Only modify the background, the color of the product (if applicable), the offer display, and the theme elements. 
    - **Do not change the product image itself; it should remain as it is in the original image.**
    - Make sure the response does not have any double quotes. 
    - Provide text for the banner (e.g., taglines, offers, etc.).

    Negative prompt: Do not alter the product packaging or branding.  


    Example Output: 
    ## Promotional Banner Design Input 
    Product: ... (product image description, e.g., "A bag of Lays potato chips")
    Offer: ... 
    Theme: ... 
    Color Palette: ...
    Banner Design Details: ... (detailed instructions for the banner)
    """

    # print([i for i in genai.list_models()])
    model = genai.GenerativeModel('models/gemini-pro')
    response = model.generate_content(prompt)

    # Process the response
    generated_text = response.text

    print(generated_text)
    return generated_text
