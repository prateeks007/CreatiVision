import os
from google.cloud import vision
from dotenv import load_dotenv
import vertexai
from vertexai.vision_models import ImageTextModel
from PIL import Image

load_dotenv()

def analyze_image(path):
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform multiple detections
    response = client.annotate_image({
        'image': image,
        'features': [
            {'type_': vision.Feature.Type.LABEL_DETECTION},
            {'type_': vision.Feature.Type.OBJECT_LOCALIZATION},
            {'type_': vision.Feature.Type.IMAGE_PROPERTIES},
            {'type_': vision.Feature.Type.TEXT_DETECTION},
            {'type_': vision.Feature.Type.LOGO_DETECTION},
        ]
    })

    # Process the results
    labels = response.label_annotations
    objects = response.localized_object_annotations
    colors = response.image_properties_annotation.dominant_colors.colors
    texts = response.text_annotations
    logos = response.logo_annotations

    # Construct a detailed description
    description = "This image shows "

    # Add main objects
    if objects:
        object_names = [obj.name.lower() for obj in objects[:3]]
        description += f"{', '.join(object_names)}. "

    # Add color information
    if colors:
        main_color = colors[0].color
        rgb = f"RGB({main_color.red}, {main_color.green}, {main_color.blue})"
        description += f"The dominant color is {rgb}. "

    # Add label information
    if labels:
        label_names = [label.description.lower() for label in labels[:5]]
        description += f"It contains or represents {', '.join(label_names)}. "

    # Add text information
    if texts[1:]:  # Skip the first one as it contains all text
        text_content = ' '.join([text.description for text in texts[1:3]])
        description += f"The image includes text: '{text_content}'. "

    # Add logo information
    if logos:
        logo_names = [logo.description for logo in logos]
        description += f"Logos detected: {', '.join(logo_names)}. "

    # Return a structured result
    return {
        'description': description,
        'labels': [label.description for label in labels],
        'objects': [obj.name for obj in objects],
        'dominant_color': rgb,
        'text': text_content,
        'logos': [logo.description for logo in logos]
    }

# def run_test(image_path):
#     detailed_description = analyze_image(image_path)
    
#     vertexai.init(project="gen-lang-client-0497992847", location="us-central1")
#     model = ImageTextModel.from_pretrained("imagetext@001")
#     source_img = Image.load_from_file(location=image_path)

#     answers = model.ask_question(
#         image=source_img,
#         question="what is in the image? expand on the description of the image, thing like color of packaging, the product name etc.",
#         number_of_results=1,
#     )
    
#     return {
#         'detailed_description': detailed_description,
#         'answers': answers
#     }