def evaluate_pronunciation(transcribed_text):
    vowels = "aeiou"
    vowel_count = sum(1 for char in transcribed_text.lower() if char in vowels)
    score = min(100, vowel_count * 2)
    return f"Pronunciation Score: {score}/100"
