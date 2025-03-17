from gliner import GLiNER

# Initialize GLiNER model
gliner_model = GLiNER.from_pretrained("urchade/gliner_base")

def extract_entities_with_gliner(text, default_entity_types, custom_entity_types):
    """
    Extract entities using GLINER with default and custom entity types.
    """
    entity_types = default_entity_types.split(",") + [
        etype.strip() for etype in custom_entity_types.split(",") if custom_entity_types
    ]
    entity_types = list(set([etype.strip() for etype in entity_types if etype.strip()]))

    entities = gliner_model.predict_entities(text, entity_types)

    formatted_entities = "\n".join([f"{i+1}: {ent['text']} --> {ent['label']}" for i, ent in enumerate(entities)])
    return formatted_entities


