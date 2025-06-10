import argparse
from ocr_engine import extract_text_from_image, extract_text_from_pdf

parser = argparse.ArgumentParser(description="Offline OCR tool")
parser.add_argument("path", help="Path to image or PDF file")
args = parser.parse_args()

if args.path.lower().endswith((".jpg", ".jpeg", ".png")):
    output = extract_text_from_image(args.path)
elif args.path.lower().endswith(".pdf"):
    output = extract_text_from_pdf(args.path)
else:
    raise ValueError("Unsupported file type")

print("\n--- OCR Output ---\n")
print(output)
