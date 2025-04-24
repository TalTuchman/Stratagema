from bs4 import BeautifulSoup

def load_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    article_div = soup.find(id="article-content")
    return article_div.get_text() if article_div else ""
