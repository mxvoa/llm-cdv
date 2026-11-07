def chunk_text(text, max_words):
    """Split text into consecutive chunks of at most max_words words."""
    if max_words <= 0:
        raise ValueError("max_words must be greater than zero")

    words = text.split()
    return [
        " ".join(words[i:i + max_words])
        for i in range(0, len(words), max_words)
    ]
