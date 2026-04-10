import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import ocr_engine
import agri_engine

# Load environment (for local testing)
load_dotenv()

# Page config
st.set_page_config(page_title="AgriVision AI Suite", page_icon="🌾", layout="wide")

# ============================================
# SIDEBAR: API KEY MANAGEMENT
# ============================================
with st.sidebar:
    st.title("⚙️ Settings")
    st.write("Enter your Google Gemini API Key to start.")
    
    # User se key lena
    user_api_key = st.text_input("Gemini API Key", type="password", help="Get your key from: https://aistudio.google.com/app/apikey")
    
    # Priority: 1. User Input, 2. .env file
    final_api_key = user_api_key if user_api_key else os.getenv("GEMINI_API_KEY")

    if final_api_key:
        try:
            genai.configure(api_key=final_api_key)
            # Gemini 2.5 Flash setup
            model = genai.GenerativeModel(model_name='gemini-1.5-flash') # Currently 1.5 is standard, use 2.5 if available
            st.success("✅ API Key Connected!")
        except Exception as e:
            st.error(f"❌ Invalid Key: {e}")
            model = None
    else:
        st.warning("⚠️ Please enter an API Key to continue.")
        model = None

    st.write("---")
    st.info("Note: Your key is not stored and is only used for this session.")

# ============================================
# MAIN UI
# ============================================
st.title("🤖 AgriVision AI Suite")
st.write("Digitize field notes and analyze complex agricultural datasets instantly.")

# Agar model ready nahi hai toh app block kar dein
if model is None:
    st.info("👈 Sidebar mein apni API Key enter karein taake tool activate ho sakay.")
    st.stop()

# Tabs
tab1, tab2 = st.tabs(["📸 Image OCR", "🌾 Agri-Research Analysis"])

# --- TAB 1: OCR Logic ---
with tab1:
    st.header("📸 Field Notes OCR")
    st.write("Upload an image of handwritten notes or printed reports.")
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
    if st.button("Extract Text"):
        if uploaded_image:
            with st.spinner("Processing image..."):
                image_bytes = uploaded_image.read()
                text = ocr_engine.extract_text_from_image(image_bytes, model)
                st.text_area("Extracted Result:", text, height=250)
        else:
            st.warning("Please upload an image.")

# --- TAB 2: Agri Logic ---
with tab2:
    st.header("🌾 Agri-Document Chat")
    st.write("Analyze PDF, Excel, or CSV files using AI.")
    uploaded_file = st.file_uploader("Upload Document", type=["pdf", "csv", "xlsx", "docx"])
    user_query = st.text_input("Ask a question about this data:")

    if st.button("Run Analysis"):
        if uploaded_file and user_query:
            with st.spinner("Analyzing document..."):
                file_bytes = uploaded_file.read()
                response = agri_engine.process_agri_document(file_bytes, uploaded_file.name, user_query, model)
                st.markdown("### 🤖 AI Response:")
                st.write(response)
        else:
            st.warning("Please upload a file and enter a question.")
