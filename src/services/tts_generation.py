import os
import numpy as np
import soundfile as sf
import tempfile
import torch
from kokoro import KPipeline

#Automatically select GPU if available, else fallback to CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"✅ Using device: {device.upper()} for TTS generation")
kokoro_tts = KPipeline(lang_code='a', device=device)  

SUPPORTED_TTS_LANGUAGES = {
    "en": "a",  
    "fr": "f",  
    "hi": "h",  
    "it": "i",  
    "pt": "p",
}

AVAILABLE_VOICES = [
    'af_bella', 'af_sarah', 'am_adam', 'am_michael',
    'bf_emma', 'bf_isabella', 'bm_george', 'bm_lewis',
    'af_nicole', 'af_sky'
]

def generate_audio_kokoro(text, lang, selected_voice):
    """Generate speech using KokoroTTS for supported languages."""
    
    lang_code = SUPPORTED_TTS_LANGUAGES.get(lang, "a")
    generator = kokoro_tts(text, voice=selected_voice, speed=1, split_pattern=r'\n+')

    audio_data_list = [audio for _, _, audio in generator]
    full_audio = np.concatenate(audio_data_list)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        sf.write(temp_file, full_audio, 24000, format='wav')
        return temp_file.name
