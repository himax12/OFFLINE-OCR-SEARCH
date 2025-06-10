import streamlit as st
import os
from ocr_engine import extract_text_from_image, extract_text_from_pdf
from index_builder import build_index
from search_engine import search_index
from pdf2image import convert_from_path
import cv2
import numpy as np
import tempfile

SAMPLES_DIR = "samples"
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR'  # no trailing \tessdata
import pytesseract

st.set_page_config(page_title="Offline OCR Search", layout="centered")
st.title("📄 Offline OCR-Based Search Engine")

st.header("1️⃣ Upload PDFs or Images")
uploaded_files = st.file_uploader("Upload files", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    os.makedirs(SAMPLES_DIR, exist_ok=True)
    for file in uploaded_files:
        filepath = os.path.join(SAMPLES_DIR, file.name)
        with open(filepath, "wb") as f:
            f.write(file.getvalue())
        st.success(f"Saved: {file.name}")

st.header("2️⃣ Build Index")
if st.button("📚 Build Index"):
    if os.listdir(SAMPLES_DIR):
        build_index(SAMPLES_DIR)
        st.success("Index built successfully.")
    else:
        st.warning("No documents to index. Please upload first.")

st.header("3️⃣ Search OCR Text")
query = st.text_input("🔍 Enter your search query")

if query:
    st.subheader("Results:")
    results = search_index(query)
    if results:
        for doc, snippet in results:
            st.markdown(f"**📄 {doc}**")
            st.write(snippet)
            st.markdown("---")
    else:
        st.info("No matches found.")
