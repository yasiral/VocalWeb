
# 🌍 Web-to-Audio Converter 🎙️

A powerful and versatile **Web-to-Audio Converter** that extracts text from web articles (HTML or PDF), summarizes content, and converts it into high-quality speech using **Gradio**, **Transformers**, and **Kokoro TTS**.

---

## 📖 About the Project
The **Web-to-Audio Converter** is designed to simplify content consumption by turning lengthy web articles, PDFs, and documents into clear, engaging audio.

Whether you're a researcher, a student, or someone who prefers listening over reading, this app offers a seamless way to consume content efficiently.

This application leverages state-of-the-art NLP models like **BART**, **GLiNER**, and **Kokoro TTS** for advanced text processing, summarization, and audio generation.

---

## 🚀 Key Features
### 🔍 1. Text Extraction & Cleaning
- Extracts text from **HTML** and **PDF** URLs.
- Uses **Trafilatura** for web scraping and **MarkItDown** for PDF conversion.
- Metadata such as author, publication date, and keywords are automatically extracted.
- Cleans extracted text by:
  - Removing excessive white spaces.
  - Removing unwanted content like references, links, and unnecessary comments.
- Automatically identifies the **language** of the extracted text.

---

### 📋 2. Summarization
- Powered by **Facebook's BART Large CNN** model for high-quality text summarization.
- Handles **large documents** using an optimized chunking strategy that preserves content flow.
- Generates concise summaries with clear, structured highlights.

---

### 🗣️ 3. Text-to-Speech (TTS)
- Uses **Kokoro TTS** for high-quality voice synthesis.
- Supports multiple languages:
  - **English**, **French**, **Hindi**, **Italian**, and **Portuguese**.
- Offers a variety of voice styles to suit different content types (e.g., storytelling, documentaries, etc.).
- Provides the option to generate audio from:
  - **Summarized content** for concise narration.
  - **Original raw content** for full-length audio playback.

---

### 🧠 4. Named Entity Recognition (NER)
- Uses **GLiNER** for advanced entity extraction.
- Identifies key entities such as:
  - **Persons**
  - **Organizations**
  - **Dates**
  - **Events**
  - Custom entities defined by the user.

---

### 🌩️ 5. Word Cloud Generator
- Provides a **visual representation** of frequently used words in the extracted text.
- Helps identify dominant themes and key ideas in large content.

---

### 🔥 6. Flexible User Interface
- Fully interactive **Gradio UI** for easy usage with buttons, controls, and visual outputs.
- Includes a **Command Line Interface (CLI)** for advanced users who prefer terminal-based interactions.

---

## 🖥️ How to Use the Application

### 🚀 1. Gradio Interface (Recommended for Beginners)
1. Run the following command:
   ```
   python src/app.py
   ```

2. Access the interactive UI by visiting the displayed URL (e.g., `http://localhost:7860`).  
3. Follow these steps in the Gradio UI:
   - **Enter the URL** for the web article or PDF.
   - Click **"Fetch Text & Detect Language"**.
   - Optionally select:
     - **"TTS based on Summary"** or **"TTS based on Raw Data"** for audio generation.
     - Enable **Named Entity Recognition** for entity extraction.
   - Click **"Generate Audio"** or **"Extract Entities"** as desired.
4. The extracted text, metadata, summary, word cloud, and audio outputs will be displayed.

---

### 🚀 2. Command-Line Interface (CLI)
For advanced users who prefer terminal commands:

✅ **Extract Text Only**
```
python src/main.py --url "https://example.com/article"
```

✅ **Extract Text + Summarization**
``` 
python src/main.py --url "https://example.com/article" --summarize
```

✅ **Extract Text + Audio Generation**
``` 
python src/main.py --url "https://example.com/article" --voice "bm_george"
```

✅ **Extract Text + Named Entity Recognition**
``` 
python src/main.py --url "https://example.com/article" --ner
```

✅ **Extract Text + Word Cloud**
``` 
python src/main.py --url "https://example.com/article" --wordcloud
```

---

## ⚙️ Installation Guide
### Step 1: Clone the Repository
``` 
git clone https://github.com/username/web-to-audio.git
cd web-to-audio
```

### Step 2: Create a Virtual Environment (Recommended)
``` 
python -m venv venv
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate         # On Windows
```

### Step 3: Install Dependencies
``` 
pip install -r requirements.txt
```

### Step 4: Download NLTK Dependencies
Run the following command to ensure required resources are available:

``` 
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
```

---

## 📂 Project Structure
```
web2audio/
├── src/
│   ├── app.py
│   ├── main.py
│   ├── services/
│   │   ├── text_extraction.py
│   │   ├── language_detection.py
│   │   ├── summarization.py
│   │   ├── ner_extraction.py
│   │   ├── tts_generation.py
│   │   ├── wordcloud_generation.py
│   │   └── utils.py
├── tests/
├── assets/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── pyproject.toml
├── setup.py
└── CONTRIBUTING.md
```

---

## 📜 License
This project is licensed under the **MIT License**.  
Feel free to modify and distribute as per the license terms.

---

## 💬 Contact & Support
For questions, suggestions, or issues, please open a **GitHub Issue** or start a **Discussion**.

---

## ⭐ Show Your Support
If you find this project helpful, please consider giving it a **star ⭐** on GitHub!

---

🎧 **"Listen to Your Web Content on the Go!"**
