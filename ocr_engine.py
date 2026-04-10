import google.generativeai as genai
import PIL.Image
import io

def extract_text_from_image(image_bytes: bytes, model) -> str:
    """
    Image se text nikalne ka modular function.
    """
    try:
        img = PIL.Image.open(io.BytesIO(image_bytes))
        response = model.generate_content(["Extract all text from this image clearly.", img])
        return response.text
    except Exception as e:
        return f"OCR Error: {str(e)}"