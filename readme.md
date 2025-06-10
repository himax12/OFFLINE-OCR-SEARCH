# Offline OCR Search Engine

A Python-based offline OCR search engine that can extract text from images and PDFs, index the content, and provide full-text search capabilities.

## Features

- OCR support for images (PNG, JPG, JPEG) and PDF files
- Full-text search functionality
- Web interface built with Streamlit
- Offline operation - no internet required after setup
- Interactive search results with highlighted matches

## Installation

1. Create conda environment:

```sh
conda env create -f env.yml
conda activate ocr-search
```

2. Install Tesseract OCR:

- Windows: Download and install from https://github.com/UB-Mannheim/tesseract/wiki
- Linux: `sudo apt-get install tesseract-ocr`
- Mac: `brew install tesseract`

## Usage

### Web Interface

Run the Streamlit web app:

```sh
streamlit run ocr_search_app.py
```

Then:

1. Upload PDF/image files using the interface
2. Click "Build Index" to process documents
3. Enter search terms to find matching content

### Command Line

Process a single file:

```sh
python app.py path/to/file.pdf
```

Build search index for a folder:

```sh
python index_builder.py path/to/folder
```

## Project Structure

- `app.py` - Command line OCR tool
- `ocr_engine.py` - Core OCR functionality
- `index_builder.py` - Creates searchable index
- `search_engine.py` - Search implementation
- `ocr_search_app.py` - Web interface

## Dependencies

- pytesseract - OCR engine
- pdf2image - PDF processing
- whoosh - Full-text indexing and search
- streamlit - Web interface
- OpenCV - Image processing

## Notes

- Supported file types: PDF, PNG, JPG, JPEG
- OCR results are cached in the `indexdir` folder
- Search results show document title and highlighted matches

## Future Scope 🚀

### Core Features

- 🔍 **Enhanced OCR**: Improved text extraction using advanced OCR engines
- 🧾 **Summarization**: Auto-generate document summaries using local LLMs (Mistral-7B/Phi-2)
- 🏷️ **Smart Keywords**: Extract key topics and terms automatically
- 🔎 **Semantic Search**: Implement vector-based similarity search

### Advanced Features

- ❓ **Q&A System**: Ask questions about document content
- 📥 **Data Extraction**: Pull structured data (dates, names, amounts)
- 📁 **Auto Classification**: Group similar documents automatically
- 🌐 **Text Enhancement**: Fix OCR errors and support translations
- 💬 **Natural Queries**: Search using conversational language
- 📊 **Analytics Dashboard**: Document insights and statistics

### Key Benefits

- 🔐 **Fully Offline**: Uses lightweight local models
- ⚡ **Fast Processing**: No cloud dependencies
- 🛡️ **Private**: All data stays on your machine
