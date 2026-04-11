import google.generativeai as genai
import PIL.Image
import io

def extract_text_from_image(image_bytes: bytes, model) -> str:
    try:
        img = PIL.Image.open(io.BytesIO(image_bytes))
        
        # Powerful Prompt for Clean Extraction
        prompt = """
        Analyze this image and perform the following tasks:
        
        1. **Clean Extraction**: Extract only the meaningful text. Ignore any decorative lines, background noise, or irrelevant symbols. 
        2. **Formatting**: Maintain the logical structure (headings and lists) but remove unnecessary white spaces or broken line breaks.
        3. **Executive Summary**: At the end, provide a brief 2-3 sentence summary of what this document/image is about.

        Structure your response as:
        ---
        [CLEAN TEXT]
        (Place the extracted text here)
        
        ---
        [SUMMARY]
        (Place the brief summary here)
        """
        
        response = model.generate_content([prompt, img])
        return response.text
    except Exception as e:
        return f"OCR Error: {str(e)}"
