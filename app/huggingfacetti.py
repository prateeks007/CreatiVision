from app.banner import generate_banner
from app.utils import save_uploaded_file, allowed_file
from PIL import Image
import io, os, time, logging

def generate_and_save_banner(
    files, offer, theme, color_palette, generator_type, format="PNG", size=None
):
    # 1) Save uploads
    filenames = []
    for file in files:
        if not allowed_file(file.filename):
            return {"error": "Invalid file type"}
        filenames.append(save_uploaded_file(file))

    # 2) Generate prompt + image object + warnings
    try:
        image_obj, prompt, warnings = generate_banner(
            filenames, offer, theme, color_palette, generator_type
        )
    except Exception as e:
        logging.error("[Banner pipeline failed]: %s", e)
        prompt = f"{offer} - {theme} banner"
        warnings = [f"[Pipeline failed]: {str(e)}"]
        image_obj = None

    # 3) If no image_obj, try fallback simple generator
    if image_obj is None:
        from app.banner import get_image_generator
        gen = get_image_generator(generator_type)
        try:
            image_obj = gen.generate_image(prompt)
        except Exception as e:
            logging.error("[Fallback image gen failed]: %s", e)
            warnings.append(f"[Final image gen failed]: {str(e)}")

    # 4) Convert to PIL
    if hasattr(image_obj, "_image_bytes"):
        pil = Image.open(io.BytesIO(image_obj._image_bytes))
    elif isinstance(image_obj, Image.Image):
        pil = image_obj
    else:
        return {
            "prompt": prompt,
            "fallback_used": True,
            "warnings": warnings,
            "error": "Unsupported image format; banner could not be generated.",
        }

    # 5) Resize
    if size:
        pil = pil.resize(size)

    # 6) Save file
    ts = int(time.time())
    fname = f"generated_banner_{ts}.{format.lower()}"
    out_path = os.path.join("static", "generated", fname)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    pil.save(out_path, format=format)

    return {
        "message": "Banner generated",
        "prompt": prompt,
        "image_path": f"/static/generated/{fname}",
        "format": format,
        "fallback_used": any("No providers available" in w or "failed" in w for w in warnings),
        "warnings": warnings,
    }
