import google.generativeai as genai
import logging
import os
from dotenv import load_dotenv

load_dotenv()

def generate_banner(filenames, offer, theme, color_palette):
    logging.info(f"Generating banner prompt for offer: {offer}")
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    # Define product_name before using it
    product_name = "Default Product"  # Replace with actual logic to get product name
    
    # Create a list to hold product descriptions
    product_descriptions = []
    
    for filename in filenames:
        # Extract product name from filename
        
        # Generate a brief description of the product image details for multiple images
        initial_prompt = f"Provide key details about the product image '{product_name}' (e.g., type of packaging, material, branding, etc.) for the following images: {', '.join(filenames)}."
        model = genai.GenerativeModel('models/gemini-pro')
        response = model.generate_content(initial_prompt)
        product_image_details = response.text.strip()  # Get the product image details

        product_description = f"""
        - **Image Details:** {product_image_details}  # Use the product image details
        - **Image:** {filename} (assume the product image is available and should remain unchanged)
        - **Type:** [Specify the type, e.g., Snack, Beverage, etc.]
        """
        product_descriptions.append(product_description)

    # Combine all product descriptions into a single string
    products_info = "\n".join(product_descriptions)
    print(products_info)

    # Construct the prompt with detailed product information
    prompt = f"""
    Design a visually appealing promotional banner for an Indian audience.

    Theme: {theme}
    Color Palette: {", ".join(color_palette)}
    Offer: {offer}

    Products:
    {products_info} 

    ## Banner Elements:

    - **Main Heading:** [Provide a catchy main heading relevant to the theme and offer]
    - **Product Taglines:** [Provide engaging taglines for each product, relating them to the theme]
    - **Offer Display:** [Clearly display the offer details]
    - **Call to Action:** [Include a compelling call to action]

    ## Image Instructions:

    - Use high-quality product images (assume images are provided). 
    - Do not alter the product images themselves.
    - Background: Design a background that complements the products and theme.
    - Ensure the banner is culturally appropriate and visually appealing to an Indian audience. 

    ## Important:

    - Do not alter product packaging or branding.
    """

    response = model.generate_content(prompt)
    generated_text = response.text
    print(generated_text)
    return generated_text