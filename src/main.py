# CLI/standalone entry point
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
import argparse
from src.services.text_extraction import fetch_and_display_content
from src.services.language_detection import detect_language
from src.services.summarization import hierarchical_summarization
from src.services.ner_extraction import extract_entities_with_gliner
from src.services.tts_generation import generate_audio_kokoro
from src.services.wordcloud_generation import generate_wordcloud
from src.config.nltk_setup import download_nltk_dependencies
import IPython.display as display
import matplotlib.pyplot as plt

download_nltk_dependencies()

def main():
	
    parser = argparse.ArgumentParser(description="Web-to-Audio Converter CLI")
    parser.add_argument("--url", required=True, help="Enter URL for content extraction")
    parser.add_argument("--voice", default="bm_george", help="Select voice for TTS")
    parser.add_argument("--ner", action="store_true", help="Enable Named Entity Recognition")
    parser.add_argument("--summarize", action="store_true", help="Enable Summarization")
    parser.add_argument("--wordcloud", action="store_true", help="Generate Word Cloud")
    
    args = parser.parse_args()

    # Fetch text content
    text, metadata, detected_lang, *_ = fetch_and_display_content(args.url)
    print(f"\nExtracted Content:\n{text}\n")
    print(f"Detected Language: {detected_lang.upper()}")

    # Display Metadata
    if metadata:
        print(f"\nMetadata:\n{metadata}\n")
    else:
        print("\nNo metadata found.\n")

    # Summarization
    if args.summarize:
        summary = hierarchical_summarization(text)
        print(f"\nSummary:\n{summary}\n")

    # NER
    if args.ner:
        entities = extract_entities_with_gliner(text, "PERSON, ORGANIZATION, DATE", "")
        print(f"\nNamed Entities:\n{entities}\n")

    # Word Cloud
    if args.wordcloud:
        print("✅ Starting Word Cloud Generation...")
    
        # Define a unique filename with timestamp
        wordcloud_file = f"wordcloud_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        # Save the WordCloud in the root directory
        generate_wordcloud(cleaned_text, save_path=wordcloud_file)
    
        print(f"✅ WordCloud saved successfully at: {os.path.abspath(wordcloud_file)}")

    # TTS Generation
    audio_file = generate_audio_kokoro(text, detected_lang, args.voice)
    print(f"\nAudio saved at: {audio_file}")

if __name__ == "__main__":
    main()
