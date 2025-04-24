def show_analysis(filename, result):
    print(f"\n--- Analysis of {filename} ---")
    print(f"Total words: {result['word_count']}")
    print(f"Paragraphs: {result['paragraph_count']}")
    print("Top 5 words:")
    for word, count in result['top_words']:
        print(f"  - {word}: {count}")
