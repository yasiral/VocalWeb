from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
from PIL import Image

def generate_wordcloud(text):
    """Generates a word cloud from text."""
    if not text:
        return None

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    plt.close()

    image = Image.open(buf)
    return image
