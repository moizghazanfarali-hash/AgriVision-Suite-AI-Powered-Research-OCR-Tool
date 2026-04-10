import PyPDF2
import io
import pandas as pd
from docx import Document

def process_agri_document(file_bytes, file_name, question, model):
    try:
        extracted_text = ""
        file_extension = file_name.split('.')[-1].lower()

        # --- Data Extraction ---
        if file_extension == 'pdf':
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes), strict=False)
            for page in pdf_reader.pages:
                extracted_text += page.extract_text() + "\n"

        elif file_extension in ['docx', 'doc']:
            doc = Document(io.BytesIO(file_bytes))
            for para in doc.paragraphs:
                extracted_text += para.text + "\n"

        elif file_extension in ['xlsx', 'xls']:
            df = pd.read_excel(io.BytesIO(file_bytes))
            extracted_text = df.to_string()

        elif file_extension == 'csv':
            df = pd.read_csv(io.BytesIO(file_bytes))
            extracted_text = df.to_string()

        if not extracted_text.strip():
            return "File is empty or could not be read."

        # --- Gemini 2.5 Logic ---
        context = extracted_text[:200000] # Increased for Gemini 2.5
        prompt = f"Expert Agriculture Analyst Context:\n{context}\n\nQuestion: {question}"

        response = model.generate_content(prompt)

        # CRITICAL FIX: Response check
        # Agar candidates khali hain (Block hone ki waja se)
        if not response.candidates or not response.candidates[0].content.parts:
            # Check for block reason
            reason = "Blocked by Safety Filter"
            if hasattr(response, 'prompt_feedback'):
                reason = str(response.prompt_feedback.block_reason)
            return f"AI Response was blocked. Reason: {reason}. Try a different file name or content."

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"