from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
from PIL import Image

def generate_wordcloud(text, save_path=None):
    """Generates a WordCloud image.
    
    - If `save_path` is provided, saves the WordCloud as a `.png` file.
    - If `save_path` is `None`, returns a PIL image (for Gradio).
    """
    if not text.strip():
        raise ValueError("❌ Text is empty or invalid for WordCloud generation.")

    # Generate WordCloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Save as PNG for CLI mode
    if save_path:
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
        plt.close()  # Prevent memory leaks

        print(f"✅ WordCloud saved at: {save_path}")
        return None  # No need to return the image when saving in CLI mode

    # For Gradio display (PIL image)
    buf = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    buf.seek(0)

    image = Image.open(buf)
    plt.close()
    return image
