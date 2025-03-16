# Gradio app entry point

import gradio as gr
from services.text_extraction import fetch_and_display_content
from services.tts_generation import generate_audio_kokoro
from services.ner_extraction import extract_entities_with_gliner
from services.summarization import hierarchical_summarization
from services.wordcloud_generation import generate_wordcloud
from services.language_detection import detect_language
from config.nltk_setup import download_nltk_dependencies

download_nltk_dependencies()

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# 🌍 Web-to-Audio Converter 🎙️")
    url_input = gr.Textbox(label="Enter URL", placeholder="https://example.com/article")
    
    voice_selection = gr.Dropdown(AVAILABLE_VOICES, label="Select Voice", value="bm_george")
    tts_option = gr.Radio(["TTS based on Summary", "TTS based on Raw Data"], value="TTS based on Summary", label="Select TTS Source")
	
	with gr.Row():
        process_text_button = gr.Button("Fetch Text & Detect Language",scale = 1)
        process_audio_button = gr.Button("Generate Audio", visible=False,scale = 1)
        process_ner_button = gr.Button("Extract Entities", visible=False,scale = 1)  
		
	with gr.Row():
        extracted_text = gr.Textbox(label="Extracted Content", visible=False, interactive=False, lines=15)
        metadata_output = gr.JSON(label="Article Metadata", visible=False)
        wordcloud_output = gr.Image(label="Word Cloud", visible=False)
		
	    
    detected_lang = gr.Textbox(label="Detected Language", visible=False)
    summary_output = gr.Textbox(label="Summary", visible=True, interactive=False)
    full_audio_output = gr.Audio(label="Generated Audio", visible=True)
    ner_output = gr.Textbox(label="Extracted Entities", visible=True, interactive=False)  
    
	default_entity_types = gr.Textbox(label="Default Entity Types", value="PERSON, ORGANIZATION, LOCATION, DATE, PRODUCT, EVENT", interactive=True)
    custom_entity_types = gr.Textbox(label="Custom Entity Types", placeholder="Enter additional entity types (comma-separated)", interactive=True)
	
	
    process_text_button.click(
        fetch_and_display_content,
        inputs=[url_input],
        outputs=[
            extracted_text, 
            metadata_output, 
            detected_lang, 
            wordcloud_output, 
            process_audio_button, 
            process_ner_button, 
            extracted_text, 
            metadata_output
        ]
    )
	
	 # Word Cloud Generation
    extracted_text.change(
        generate_wordcloud,
        inputs=[extracted_text],
        outputs=[wordcloud_output],
		show_progress=True
    )

    # Summarization
    extracted_text.change(
        hierarchical_summarization,
        inputs=[extracted_text],
        outputs=[summary_output],
		show_progress=True
    )

	# Audio Generation
    process_audio_button.click(
        lambda text, summary, lang, voice, tts_choice: (
		    None,  # Clear previous audio
			generate_audio_kokoro(
                summary if tts_choice == "TTS based on Summary" else text, lang, voice
            )
        ),
        inputs=[extracted_text, summary_output, detected_lang, voice_selection, tts_option],
        outputs=[full_audio_output, full_audio_output],  # Clear first, then display new audio
        show_progress=True
    )

    # NER Extraction
    process_ner_button.click(
        extract_entities_with_gliner,
		inputs=[extracted_text, default_entity_types, custom_entity_types],
        outputs=[ner_output]
    )

demo.launch()
