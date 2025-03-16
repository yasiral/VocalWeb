import gradio as gr
import trafilatura
from trafilatura import fetch_url, extract
from markitdown import MarkItDown
from langdetect import detect
from services.text_cleaning import extract_and_clean_text
from services.language_detection import detect_language

def fetch_and_display_content(url):
    """
    Fetch and extract text from a given URL (HTML or PDF).
    Extract metadata, clean text, and detect language.
    """
    if url.endswith(".pdf") or "pdf" in url:
        converter = MarkItDown()
        text = converter.convert(url).text_content
    else:
        downloaded = trafilatura.fetch_url(url)
        text = extract(downloaded, output_format="markdown", with_metadata=True, include_tables=False, include_links=False, include_formatting=True, include_comments=False) 
	
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
