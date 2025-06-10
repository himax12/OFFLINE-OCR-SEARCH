import pytesseract
from pdf2image import convert_from_path
import cv2
import os
import tempfile
import numpy as np
from PIL import Image

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

def extract_text_from_pdf(pdf_path):
    text = ""
    images = convert_from_path(pdf_path)
    
    for img in images:
        if not isinstance(img, Image.Image):
            print(f"[ERROR] Expected PIL.Image, got {type(img)}")
            continue

        cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        page_text = pytesseract.image_to_string(cv_img)
        text += page_text + "\n"

        img.close()
    
    return text.strip()
