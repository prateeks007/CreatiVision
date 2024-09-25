import google.generativeai as genai
import logging
import os
from dotenv import load_dotenv
from app.analyze_image import analyze_image

load_dotenv()

def generate_banner(filenames, offer, theme, color_palette):
    logging.info(f"Generating banner prompt for offer: {offer}")
    
    product_descriptions = []
    for filename in filenames:
        image_analysis = analyze_image(filename)
        main_product = image_analysis['labels'][0]  # Get the main product label
        product_description = f"Product: {main_product}"
        product_descriptions.append(product_description)

    products_info = "\n".join(product_descriptions)

    prompt = f"""
    Design a professional promotional banner for an Indian audience.

    Theme: {theme}
    The theme should guide the overall design.

    Color Palette: {", ".join(color_palette)}
    Offer: {offer}

    Products:
    {products_info}

    Banner Elements:
    1. Main Heading: Create a clear headline incorporating the theme "{theme}".
    2. Product Showcase: Prominently display the main product(s): {', '.join([desc.split(': ')[1] for desc in product_descriptions])}.
    3. Offer Display: Present the offer "{offer}" clearly.
    4. Taglines: Create brief, relevant taglines for each product (5-7 words each).
    5. Call to Action: Include a clear call to action.
    6. Background: Design a background that complements the theme.

    Design Guidelines:
    - Use the provided color palette throughout the banner
    - Maintain a clear visual hierarchy
    - Ensure all text is legible
    - Optimize the layout for quick comprehension

    Important:
    - The design should be culturally appropriate for an Indian audience
    - Do not alter product packaging or branding
    - Maintain a professional and clear message

    Provide a concise description of the banner design, focusing on:
    1. How the theme influences the overall design
    2. The layout and arrangement of key elements
    3. Use of the color palette
    4. Any notable design elements
    """

    model = genai.GenerativeModel('models/gemini-pro')
    response = model.generate_content(prompt)
    generated_text = response.text if hasattr(response, 'text') else str(response)
    print(generated_text)
    return generated_text