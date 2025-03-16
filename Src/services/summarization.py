from transformers import BartForConditionalGeneration, BartTokenizer
import torch
from nltk.tokenize import sent_tokenize
from config.nltk_setup import download_nltk_dependencies

# Ensure NLTK dependencies are downloaded
download_nltk_dependencies()

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def split_text_with_optimized_overlap(text, max_tokens=1024, overlap_tokens=25):
    """Splits text into optimized overlapping chunks."""
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0
    previous_chunk_text = ""
    
    for sentence in sentences:
        tokenized_sentence = tokenizer.encode(sentence, add_special_tokens=False)
        token_length = len(tokenized_sentence)
        
        if current_length + token_length > max_tokens:
            chunks.append(previous_chunk_text + " " + " ".join(current_chunk))
            previous_chunk_text = " ".join(current_chunk)[-overlap_tokens:]
            current_chunk = [sentence]
            current_length = token_length
        else:
            current_chunk.append(sentence)
            current_length += token_length
    
    if current_chunk:
        chunks.append(previous_chunk_text + " " + " ".join(current_chunk))
        
    return chunks

def summarize_text(text, max_input_tokens=1024, max_output_tokens=200):
    """Summarizes text using BART model."""
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=max_input_tokens, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_output_tokens, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def hierarchical_summarization(text):
    """Performs hierarchical summarization by chunking content first."""
    chunks = split_text_with_optimized_overlap(text)
    chunk_summaries = [summarize_text(chunk) for chunk in chunks]
    final_summary = " ".join(chunk_summaries)
    return final_summary
