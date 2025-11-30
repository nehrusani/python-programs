import re
import tkinter as tk

def check_password_strength(password):
    score = 0
    feedback = []
    
    checks = [
        (len(password) >= 8, "❌ At least 8 characters"),
        (len(password) >= 12, ""),
        (re.search(r"[a-z]", password), "❌ Add lowercase"),
        (re.search(r"[A-Z]", password), "❌ Add uppercase"),
        (re.search(r"\d", password), "❌ Add numbers"),
        (re.search(r"[!@#$%^&*()_+\-=\[\]{};:'\",./<>?]", password), "❌ Add special chars"),
    ]
    
    for check, msg in checks:
        if check:
            score += 1
        elif msg:
            feedback.append(msg)
    
    strengths = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return {"score": score, "strength": strengths[min(score, 5)], "feedback": feedback}

def check():
    result = check_password_strength(password_entry.get())
    strength_label.config(text=f"Strength: {result['strength']} ({result['score']}/6)")
    feedback_text.config(state=tk.NORMAL)
    feedback_text.delete(1.0, tk.END)
    feedback_text.insert(tk.END, "\n".join(result['feedback']) or "✅ Excellent!")
    feedback_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
tk.Label(root, text="=== Password Strength Checker ===", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Enter Password:").pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)
tk.Button(root, text="Check Strength", command=check).pack(pady=10)
strength_label = tk.Label(root, text="Strength: ", font=("Arial", 12))
strength_label.pack(pady=5)
tk.Label(root, text="Feedback:").pack()
feedback_text = tk.Text(root, height=6, width=40, state=tk.DISABLED)
feedback_text.pack(pady=5)
root.mainloop()
