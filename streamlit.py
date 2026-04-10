import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import ocr_engine
import agri_engine

# Load environment
load_dotenv()

# Page config
st.set_page_config(page_title="AgriVision Suite v1", page_icon="🌾", layout="wide")

# ============================================
# SIDEBAR: API KEY & VERSIONING
# ============================================
with st.sidebar:
    st.title("⚙️ Configuration")
    st.markdown("### **Project Version: 1.0**") # Version Mentioned
    
    user_api_key = st.text_input("Gemini API Key", type="password", help="Enter your Google AI Studio API Key")
    
    final_api_key = user_api_key if user_api_key else os.getenv("GEMINI_API_KEY")

    if final_api_key:
        try:
            genai.configure(api_key=final_api_key)
            model = genai.GenerativeModel(model_name='gemini-2.5-flash')
            st.success("✅ System Active")
        except Exception as e:
            st.error(f"❌ Connection Error")
            model = None
    else:
        st.warning("⚠️ Waiting for API Key...")
        model = None

    st.write("---")
    # v2 Features Teaser in Sidebar
    st.markdown("### 🚀 Upcoming in v2.0")
    st.write("- 🌐 Web Scraping & RAG")
    st.write("- 🎥 Live YouTube Video OCR")
    st.write("- 📧 Automated Cold Outreach")

# ============================================
# MAIN UI
# ============================================
st.title("🌾 AgriVision AI Suite [v1.0]")
st.info("Professional Agriculture Research & Data Extraction Tool")

if model is None:
    st.info("👈 Please enter your Gemini API Key in the sidebar to activate the tools.")
    st.stop()

# Tabs
tab1, tab2, tab3 = st.tabs(["📸 Field Notes OCR", "🌾 Document Analytics", "🔮 v2.0 Roadmap"])

# --- TAB 1: OCR Logic ---
with tab1:
    st.header("📸 Field Notes OCR (v1)")
    uploaded_image = st.file_uploader("Upload an image of notes", type=["jpg", "png", "jpeg"])
    
    if st.button("Extract Text"):
        if uploaded_image:
            with st.spinner("Scanning handwritten data..."):
                image_bytes = uploaded_image.read()
                text = ocr_engine.extract_text_from_image(image_bytes, model)
                st.text_area("Extracted Text:", text, height=250)
        else:
            st.warning("Please upload an image.")

# --- TAB 2: Agri Analysis ---
with tab2:
    st.header("📊 Document Analysis (v1)")
    uploaded_file = st.file_uploader("Upload Reports (PDF, Excel, CSV)", type=["pdf", "csv", "xlsx", "docx"])
    user_query = st.text_input("Enter your research question:")

    if st.button("Analyze Data"):
        if uploaded_file and user_query:
            with st.spinner("Processing large context..."):
                file_bytes = uploaded_file.read()
                response = agri_engine.process_agri_document(file_bytes, uploaded_file.name, user_query, model)
                st.success("Analysis Complete!")
                st.markdown(response)
        else:
            st.warning("Provide file and question.")

# --- TAB 3: v2 Roadmap (Vision) ---
with tab3:
    st.header("🌟 Future Roadmap: Version 2.0")
    st.markdown("""
    ### 1. Web Scraping & RAG Integration
    - Automatically scrape the latest agricultural research papers from the web.
    - Implement a Vector Database (RAG) for petabyte-scale document searching.

    ### 2. Live Video Text Extraction (OCR)
    - **YouTube Integration:** Users can paste a YouTube link, and the AI will extract real-time data and text while the video plays.
    - **Dynamic Frame Analysis:** Perfect for extracting data from educational agri-webinars.

    ### 3. Automated Automation
    - Integration with Cold Email tools to send reports directly to stakeholders.
    """)
    st.button("V2 is under development...", disabled=True)

st.write("---")
st.caption("© 2026 AgriVision Suite | Built with Gemini 2.5 Flash")
