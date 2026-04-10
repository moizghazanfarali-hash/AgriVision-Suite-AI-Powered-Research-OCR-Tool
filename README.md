# 🤖 AI Document Suite - Streamlit UI

A beautiful, professional Streamlit application for OCR (Optical Character Recognition) and Agricultural Document Analysis powered by Google Gemini 2.5.

## ✨ Features

### 📸 OCR Extraction
- Extract text from images (JPG, PNG, BMP, GIF)
- High-quality text recognition using Gemini Vision API
- Download extracted text as file

### 🌾 Agricultural Document Analysis
- Support for multiple formats: PDF, DOCX, XLSX, CSV
- Intelligent Q&A system for agricultural documents
- Context-aware analysis using Gemini 2.5
- Download analysis results

### 🎨 Beautiful UI
- **Animated gradient background** with smooth transitions
- **Floating particle effects** for visual appeal
- Glassmorphism design with blur effects
- Responsive layout for all devices
- Smooth hover animations on buttons and cards

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.8+
- Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Setup

Create a `.env` file in the project directory:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the Application

```bash
streamlit run streamlit_app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📖 Usage Guide

### OCR Extraction Tab
1. Click on the **📸 OCR Extraction** tab
2. Upload an image file (JPG, PNG, BMP, or GIF)
3. Click **🚀 Extract Text** button
4. View and download the extracted text

### Agricultural Analysis Tab
1. Click on the **🌾 Agricultural Analysis** tab
2. Upload a document (PDF, DOCX, XLSX, or CSV)
3. Type your question in the text area
4. Click **🔍 Analyze & Answer** button
5. View the AI-powered analysis
6. Download results if needed

## 🎨 Customization

### Change Colors
Edit the CSS in `streamlit_app.py` - look for these gradient colors:
- Primary: `#667eea` (Blue-Purple)
- Secondary: `#764ba2` (Dark Purple)
- Accent: `#f093fb` (Pink)

### Adjust Animations
- **Background animation speed**: Change `15s` in `@keyframes gradientShift`
- **Floating effect**: Change `20s` in `@keyframes float`
- **Slide animation**: Change `0.8s` in `@keyframes slideIn`

## 📁 Project Structure

```
.
├── streamlit_app.py       # Main Streamlit application
├── agri_engine.py         # Agricultural processing logic
├── ocr_engine.py          # OCR extraction logic
├── main.py                # Original FastAPI server (optional)
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
└── README.md              # This file
```

## 🔧 Technical Details

### Technologies Used
- **Streamlit**: Modern web UI framework
- **Google Gemini 2.5**: AI model for text/image understanding
- **PyPDF2**: PDF processing
- **python-docx**: DOCX document handling
- **Pandas**: Excel/CSV data handling
- **Pillow**: Image processing

### Safety Features
- Disabled harmful content restrictions for agricultural content analysis
- Error handling with user-friendly messages
- Safe file processing with size limits

## 🎯 Performance Tips

1. **Optimize Images**: Reduce image file size for faster processing
2. **Document Size**: Keep documents under 200k characters for best results
3. **Caching**: Streamlit automatically caches results (refresh to clear)

## 🐛 Troubleshooting

### "Import Error" messages
```bash
pip install --upgrade -r requirements.txt
```

### Gemini API errors
- Verify your API key is correct in `.env`
- Check your API quota on Google Cloud Console
- Ensure you have the correct permissions

### Slow response times
- Reduce document/image size
- Check internet connection
- Verify Gemini API service status

## 📝 API Keys & Security

⚠️ **NEVER commit `.env` file to version control!**

Add to `.gitignore`:
```
.env
__pycache__/
*.pyc
```

## 📞 Support

For issues or improvements, check:
1. Google Gemini documentation
2. Streamlit documentation: https://docs.streamlit.io/
3. Common issues in troubleshooting section above

## 📄 License

This project is provided as-is for educational and commercial use.

---

**Created with ❤️ for Agricultural Intelligence** 🌾
