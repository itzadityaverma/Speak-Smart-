import tkinter as tk
from tkinter import filedialog
from asr_module import transcribe_audio
from evaluate_pronunciation import evaluate_pronunciation
from evaluate_fluency import evaluate_fluency
from evaluate_grammar import evaluate_grammar
from feedback_generator import generate_feedback

def process_audio():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    transcript = transcribe_audio(file_path)
    pron_score = evaluate_pronunciation(transcript)
    fluency_score = evaluate_fluency(transcript)
    grammar_score = evaluate_grammar(transcript)

    feedback = generate_feedback(pron_score, fluency_score, grammar_score)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Transcript:\n{transcript}\n\n{feedback}")

# GUI setup
root = tk.Tk()
root.title("Spoken Language Proficiency Assessment")
root.geometry("600x500")

upload_btn = tk.Button(root, text="Upload Audio", command=process_audio)
upload_btn.pack(pady=10)

result_text = tk.Text(root, wrap=tk.WORD)
result_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

root.mainloop()
