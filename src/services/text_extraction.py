import gradio as gr
import trafilatura
from trafilatura import fetch_url, extract
from markitdown import MarkItDown
from langdetect import detect
from src.services.text_cleaning import extract_and_clean_text
from src.services.language_detection import detect_language


def fetch_and_display_content(url):
    """
    Fetch and extract text from a given URL (HTML or PDF).
    Extract metadata, clean text, and detect language.
    """
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        raise ValueError(f"❌ Failed to fetch content from URL: {url}")
  
    # Check if the content is a potential PDF
    if "/pdf/" in url or url.endswith(".pdf"):
        converter = MarkItDown(enable_plugins=False)
        try:
            text = converter.convert(url).text_content
        except Exception as e:
            raise RuntimeError(f"❌ Error converting PDF with MarkItDown: {e}")
    else:
        text = extract(downloaded, output_format="markdown", with_metadata=True, include_tables=False, include_links=False, include_formatting=True, include_comments=False)
  
    if not text or len(text.strip()) == 0:
        raise ValueError("❌ No content found in the extracted data.")
        
	
    metadata, cleaned_text = extract_and_clean_text(text)
    detected_lang = detect_language(cleaned_text)

    # Add detected language to metadata
    metadata["Detected Language"] = detected_lang.upper()

    return (
        cleaned_text, 
        metadata, 
        detected_lang,
        gr.update(visible=True),  # Show Word Cloud
        gr.update(visible=True),  # Show Process Audio Button
        gr.update(visible=True),  # Show Process NER Button
        gr.update(visible=True),  # Show Extracted Text
        gr.update(visible=True)   # Show Metadata Output
    )
