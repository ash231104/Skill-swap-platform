def validate_skill_text(text):
    banned_words = ["spam", "fake", "scam"]
    return not any(word in text.lower() for word in banned_words)