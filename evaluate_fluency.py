def evaluate_fluency(transcribed_text):
    words = transcribed_text.split()
    total_words = len(words)
    pauses = transcribed_text.count(",") + transcribed_text.count(".")
    fluency_score = round((total_words / (pauses + 1)) * 5, 2)
    return f"Estimated Fluency Score: {fluency_score}/100"
