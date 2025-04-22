from collections import Counter
import re

def analyze_text(text):
    # Count paragraphs
    paragraphs = text.strip().split('\n\n')
    paragraph_count = len(paragraphs)

    # Clean and split text into words
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)

    # Find top 5 frequent words
    word_frequencies = Counter(words)
    top_5_words = word_frequencies.most_common(5)

    return {
        'word_count': word_count,
        'paragraph_count': paragraph_count,
        'top_5_words': top_5_words
    }

def load_article_text(filepath):
    from bs4 import BeautifulSoup

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    article_div = soup.find(id="article-content")

    if article_div:
        return article_div.get_text()
    else:
        return ""


if __name__ == "__main__":
    sample_text = """This is a simple test article.

It has a few paragraphs. Each one has a few sentences.
This helps us test the analyzer logic.

This is the third paragraph. It’s short."""
    
    

article_text = load_article_text("articles/article1.html")
analysis = analyze_text(article_text)
for i in range(1, 5):
    print(f"\n--- Analyzing article{i}.html ---")
    article_text = load_article_text(f"articles/article{i}.html")
    analyze_text(article_text)
    print("Word Count:", analysis['word_count'])
    print("Paragraph Count:", analysis['paragraph_count'])
    print("Top 5 Frequent Words:", analysis['top_5_words'])
