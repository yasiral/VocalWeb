from gliner import GLiNER
import re

# Initialize GLiNER model
gliner_model = GLiNER.from_pretrained("urchade/gliner_base")

def chunk_text_with_overlap(text, max_tokens=500, overlap_tokens=50):
    """Splits text into overlapping chunks for large document processing."""
    sentences = re.split(r'(?<=[.!?])\s+', text)  # Split on sentence boundaries
    chunks = []
    current_chunk = []
    current_length = 0
    previous_chunk_text = ""

    for sentence in sentences:
        token_length = len(sentence.split())
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

def extract_entities_with_gliner(text, default_entity_types, custom_entity_types, batch_size=4):
    """
    Extract entities using GLINER with efficient chunking, sliding window, and batching.
    """
    # Entity types preparation
    entity_types = default_entity_types.split(",") + [
        etype.strip() for etype in custom_entity_types.split(",") if custom_entity_types
    ]
    entity_types = list(set([etype.strip() for etype in entity_types if etype.strip()]))

    # Chunk the text to avoid overflow
    chunks = chunk_text_with_overlap(text)

    # Process each chunk individually for improved stability
    all_entities = []
    for i, chunk in enumerate(chunks):
        try:
            entities = gliner_model.predict_entities(chunk, entity_types)
            all_entities.extend(entities)
        except Exception as e:
            print(f"⚠️ Error processing chunk {i}: {e}")

    # Format the results
    formatted_entities = "\n".join(
        [f"{i+1}: {ent['text']} --> {ent['label']}" for i, ent in enumerate(all_entities)]
    )

    return formatted_entities
