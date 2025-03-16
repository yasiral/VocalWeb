import re
import json

def extract_and_clean_text(data):
    """
    Extracts metadata, removes everything before 'Abstract', and cleans text.
    Returns two dictionaries:
    - `metadata_dict`: Extracted metadata
    - `cleaned_text`: Cleaned and structured text
    """
    metadata_dict = {}

    # Step 1: Extract metadata enclosed between "---" at the beginning
    metadata_pattern = re.match(r"^---(.*?)---", data, re.DOTALL)
    if metadata_pattern:
        metadata_raw = metadata_pattern.group(1).strip()
        data = data[metadata_pattern.end():].strip()  # Remove metadata from text

        # Convert metadata into dict
        metadata_lines = metadata_raw.split("\n")
        for line in metadata_lines:
            if ": " in line:
                key, value = line.split(": ", 1)
                if value.startswith("[") and value.endswith("]"):
                    try:
                        value = json.loads(value)  # Convert JSON-like metadata into a Python object
                    except json.JSONDecodeError:
                        pass
                metadata_dict[key.strip()] = value.strip()

    # Step 2: Remove everything before the 'Abstract' section
    def remove_text_before_abstract(text):
        """Removes all text before the first occurrence of 'Abstract'."""
        abstract_pattern = re.compile(r"(?i)\babstract\b")
        match = abstract_pattern.search(text)
        return text[match.start():] if match else text

    data = remove_text_before_abstract(data)

    # Step 3: Clean the extracted text
    def clean_text(text):
        text = re.sub(r'\[\d+\]', '', text)  # Remove citation numbers like [1], [2], etc.
        text = re.sub(r'http[s]?://\S+', '', text)  # Remove URLs
        text = re.sub(r'\[.*?\]\(http[s]?://\S+\)', '', text)  # Remove markdown-style links
		
		patterns = [r'References\b.*', r'Bibliography\b.*', r'External Links\b.*', r'COMMENTS\b.*']
        for pattern in patterns:
            text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r'\n\s*\n+', '\n\n', text).strip()  # Fix excessive blank lines
		
        return text

    return metadata_dict, clean_text(data)
