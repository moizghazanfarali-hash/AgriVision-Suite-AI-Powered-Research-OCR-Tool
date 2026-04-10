from fastapi import FastAPI, UploadFile, File, Form
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold # Naya Import
import os
from dotenv import load_dotenv

import ocr_engine
import agri_engine

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- Safety Settings Configure Karein ---
# Isse AI sensitive data ko block nahi karega
# main.py mein model initialize aise karein:
# Safety settings define karein
safety_settings = {
    "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
    "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
    "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
    "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
}

# Model ko safety settings ke saath initialize karein
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    safety_settings=safety_settings
)

app = FastAPI(title="AI Document Suite")

@app.get("/")
def read_root():
    return {"status": "Online"}

@app.post("/ocr")
async def ocr_route(file: UploadFile = File(...)):
    content = await file.read()
    result = ocr_engine.extract_text_from_image(content, model)
    return {"extracted_text": result}

@app.post("/agri-chat")
async def agri_route(question: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()
    answer = agri_engine.process_agri_document(content, file.filename, question, model)
    return {
        "filename": file.filename,
        "answer": answer
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)