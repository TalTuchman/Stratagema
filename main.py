from controller import load_article
from model import analyze_text
from presenter import show_analysis

for i in range(1, 5):
    filename = f"articles/article{i}.html"
    content = load_article(filename)
    result = analyze_text(content)
    show_analysis(filename, result)
