import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import ocr_engine
import agri_engine

# Load environment
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name='gemini-2.5-flash')
else:
    model = None

# Page config
st.set_page_config(page_title="AI Document Suite", page_icon="🤖", layout="wide")

# Simple header
st.title("🤖 AI Document Suite")
st.write("Extract text from images or analyze agricultural documents")

# Check API key
if not api_key:
    st.error("⚠️ API Key not found. Add GEMINI_API_KEY to .env file")
    st.stop()

# Tabs
tab1, tab2 = st.tabs(["📸 OCR", "🌾 Agricultural Analysis"])

# ============================================
# TAB 1: OCR
# ============================================
with tab1:
    st.header("Extract Text from Images")
    
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp", "gif"])
    
    if st.button("Extract Text"):
        if uploaded_image is None:
            st.error("Please upload an image first")
        else:
            with st.spinner("Extracting text..."):
                image_bytes = uploaded_image.read()
                extracted_text = ocr_engine.extract_text_from_image(image_bytes, model)
                
                if "Error" in extracted_text:
                    st.error(extracted_text)
                else:
                    st.success("Text extracted successfully!")
                    st.text_area("Extracted Text:", value=extracted_text, height=300)
                    
                    st.download_button(
                        label="Download Text",
                        data=extracted_text,
                        file_name=f"extracted_{uploaded_image.name.split('.')[0]}.txt",
                        mime="text/plain"
                    )

# ============================================
# TAB 2: AGRICULTURAL ANALYSIS
# ============================================
with tab2:
    st.header("Analyze Agricultural Documents")
    
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "xlsx", "csv"])
    
    question = st.text_area("Ask a question about the document:", height=100)
    
    if st.button("Analyze"):
        if uploaded_file is None:
            st.error("Please upload a document first")
        elif not question.strip():
            st.error("Please enter a question")
        else:
            with st.spinner("Analyzing..."):
                file_bytes = uploaded_file.read()
                answer = agri_engine.process_agri_document(
                    file_bytes,
                    uploaded_file.name,
                    question,
                    model
                )
                
                if "Error" in answer or "Blocked" in answer:
                    st.error(answer)
                else:
                    st.success("Analysis complete!")
                    st.write(answer)
                    
                    result_text = f"Question: {question}\n\nAnswer:\n{answer}"
                    st.download_button(
                        label="Download Results",
                        data=result_text,
                        file_name=f"analysis_{uploaded_file.name.split('.')[0]}.txt",
                        mime="text/plain"
                    )

st.write("---")
st.write("Simple AI Document Suite | Powered by Google Gemini 2.5")