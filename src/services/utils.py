import re

def remove_text_before_abstract(text):
    """Removes all text before the first occurrence of 'Abstract'."""
    abstract_pattern = re.compile(r"(?i)\babstract\b")
    match = abstract_pattern.search(text)
    return text[match.start():] if match else text

def clean_text(text):
    """Cleans extracted text by removing URLs, references, etc."""
    text = re.sub(r'\[\d+\]', '', text)  
    text = re.sub(r'http[s]?://\S+', '', text)  
    text = re.sub(r'\[.*?\]\(http[s]?://\S+\)', '', text)  
    text = re.sub(r'\n\s*\n+', '\n\n', text).strip()
    return text
