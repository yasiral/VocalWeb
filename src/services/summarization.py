from transformers import BartForConditionalGeneration, BartTokenizer
import torch
import os
from nltk.tokenize import sent_tokenize
from src.config.nltk_setup import download_nltk_dependencies
import nltk

nltk.download('punkt')
nltk.download("punkt_tab")

# Ensure NLTK dependencies are downloaded
download_nltk_dependencies()

# Select device based on hardware availability
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "facebook/bart-large-cnn"

try:
    tokenizer = BartTokenizer.from_pretrained(model_name, cache_dir=os.path.join(os.getcwd(), ".cache"))
    model = BartForConditionalGeneration.from_pretrained(model_name, cache_dir=os.path.join(os.getcwd(), ".cache")).to(DEVICE)

except Exception as e:
    raise RuntimeError(f"Error loading BART model: {e}")

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
	print(f"✅ Summarization will run on: {DEVICE.upper()}")
	
    if len(text) > 10000:
        print("⚠️ Warning: Large input text detected. Summarization may take longer than usual.")

    chunks = split_text_with_optimized_overlap(text)
	#Tokenize the input cleaned text
    encoded_inputs = tokenizer(
        ["summarize: " + chunk for chunk in chunks],
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=1024
    ).to(DEVICE)
	
	#Generate the summary
    summary_ids = model.generate(
        encoded_inputs["input_ids"],
        max_length=200,
        min_length=50,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    
	#decode the summary generated in above step
	chunk_summaries = [tokenizer.decode(ids, skip_special_tokens=True) for ids in summary_ids]
    final_summary = " ".join(chunk_summaries)
    return final_summary
