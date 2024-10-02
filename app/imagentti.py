import os
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
output_file = "image.png"
prompt = """

Create a detailed architecture diagram for the CreatiVision project, an AI-powered marketing asset generator. The diagram should include the following components and their interactions:

1. Frontend (Vue.js Application):
   - Main App component
   - Router
   - Components: Home, BannerGenerator, VideoGenerator

2. Backend (Flask Application):
   - Main app.py file
   - Routes
   - Banner generation module
   - Video generation module (placeholder)
   - Image analysis module

3. External Services:
   - Google Cloud Vision API (for image analysis)
   - Google Generative AI (for prompt generation)
   - Hugging Face API (for image generation)
   - Google Imagen API (alternative for image generation)

4. Hosting:
   - Render (for both frontend and backend)

5. File Storage:
   - Local storage on Render for generated images

Key interactions to highlight:
1. User interaction with the Vue.js frontend hosted on Render
2. API calls between frontend and backend
3. Backend processing requests and interacting with external APIs
4. Data flow for image upload, analysis, and generation
5. Storage and retrieval of generated images

Use appropriate symbols for each component (e.g., rectangles for applications, cylinders for databases, clouds for external services). Use arrows to show the direction of data flow and API calls. Include a legend to explain the symbols used.

The diagram should be clear, visually appealing, and easy to understand for both technical and non-technical audiences. Use color coding to differentiate between frontend, backend, and external services.

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