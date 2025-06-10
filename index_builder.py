# index_builder.py

from whoosh import index
from whoosh.fields import Schema, TEXT, ID
import os
from ocr_engine import extract_text_from_pdf, extract_text_from_image

INDEX_DIR = "indexdir"

def create_schema():
    return Schema(
        title=ID(stored=True, unique=True),
        content=TEXT(stored=True)
    )

def build_index(doc_folder):
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)
        ix = index.create_in(INDEX_DIR, create_schema())
    else:
        ix = index.open_dir(INDEX_DIR)

    writer = ix.writer()

    for fname in os.listdir(doc_folder):
        fpath = os.path.join(doc_folder, fname)
        if not os.path.isfile(fpath):
            continue

        print(f"[INFO] Processing: {fname}")
        if fname.lower().endswith(('.png', '.jpg', '.jpeg')):
            content = extract_text_from_image(fpath)
        elif fname.lower().endswith('.pdf'):
            content = extract_text_from_pdf(fpath)
        else:
            print(f"[WARN] Skipping unsupported file: {fname}")
            continue

        writer.update_document(title=fname, content=content)

    writer.commit()
    print("[INFO] Index build complete.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Index documents in a folder")
    parser.add_argument("folder", help="Folder containing images/PDFs for OCR and indexing")
    args = parser.parse_args()

    build_index(args.folder)
