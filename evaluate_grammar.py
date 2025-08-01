def evaluate_grammar(transcribed_text):
    grammar_issues = 0
    
    if not transcribed_text.endswith("."):
        grammar_issues += 1
    if " i " in transcribed_text.lower():
        grammar_issues += 1
    if transcribed_text.count("is") > 3:
        grammar_issues += 1

    score = max(0, 100 - (grammar_issues * 10))
    return f"Grammar Score: {score}/100"
