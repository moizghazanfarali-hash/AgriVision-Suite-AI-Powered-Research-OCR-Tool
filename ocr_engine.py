import google.generativeai as genai
import PIL.Image
import io

def extract_text_from_image(image_bytes: bytes, model) -> str:
    try:
        img = PIL.Image.open(io.BytesIO(image_bytes))
        
        prompt = """
        Analyze this image and perform the following:
        1. **Clean Extraction**: Extract only meaningful text. Ignore lines, noise, or irrelevant symbols.
        2. **Formatting**: Keep headings and lists clear. Remove extra spaces.
        3. **Executive Summary**: Provide a 2-3 sentence summary at the end.
        
        Format:
        [EXTRACTED TEXT]
        ...
        ---
        [SUMMARY]
        (place the brief  professional summary)
        """
        
        response = model.generate_content([prompt, img])
        return response.text
        
    except Exception as e:
        err = str(e).lower()
        if "429" in err or "quota" in err or "limit" in err:
            return "❌ **API Limit Reached**: Your Gemini free tier limit is exhausted. Please wait a minute or use a different API key in the sidebar."
        return f"OCR Error: {str(e)}"
