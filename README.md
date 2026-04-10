# 🌾 AgriVision AI Suite

A high-performance Full-Stack AI application designed to streamline agricultural research and data extraction using **Gemini 2.5 Flash** and **FastAPI**.

## 🚀 Key Features

### 1. 🔍 Image OCR (Optical Character Recognition)
- **Use Case:** Digitizing hand-written field notes, lab receipts, and physical document scans.
- **Tech:** Google Gemini Vision, PIL, and io processing.
- **Capability:** Extracts text from JPG/PNG with high accuracy even in low-quality images.

### 2. 🌾 Agri-Research Q&A (Multi-Document Analyzer)
- **Use Case:** Chatting with complex agricultural reports and data sheets.
- **Supported Formats:** PDF, DOCX, CSV, XLSX (Excel).
- **Long-Context Window:** Leverages Gemini's 1M+ token capacity to analyze entire books or large datasets without information loss (No-RAG fragmentation).
- **Expert Reasoning:** Provides insights on crop yields, soil analysis, and trend forecasting.

### 3. 📧 Outreach Automation (Upcoming)
- Generates personalized cold emails based on research data for consulting firms.

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Interactive UI)
- **Backend:** FastAPI (Modular Architecture)
- **AI Model:** Google Gemini 2.5 Flash / 1.5 Pro
- **Data Handling:** Pandas (Excel/CSV), PyPDF2 (PDF), Python-Docx (Word)

## 📂 Project Structure
- `main.py`: The API hub and traffic controller.
- `ocr_engine.py`: Specialized logic for image processing.
- `agri_engine.py`: Multi-format document parser and expert Q&A logic.
- `.env`: Secure API key management.

---
*Developed by [Moiz] - AI Operations & Backend Developer*
