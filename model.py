def analyze_text(text):
    words = text.lower().split()
    word_count = len(words)
    paragraph_count = text.count('\n\n')

    word_freq = {}
    for word in words:
        word = word.strip(".,!?()[]\"'")
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        "word_count": word_count,
        "paragraph_count": paragraph_count,
        "top_words": top_words
    }
