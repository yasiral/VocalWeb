from langdetect import detect

SUPPORTED_TTS_LANGUAGES = {
    "en": "a",
    "fr": "f",
    "hi": "h",
    "it": "i",
    "pt": "p",
}

def detect_language(text):
    """
    Detects the language of the given text.
    Defaults to English if detection fails or language is unsupported.
    """
    try:
        lang = detect(text)
        return lang if lang in SUPPORTED_TTS_LANGUAGES else "en"
    except:
        return "en"
