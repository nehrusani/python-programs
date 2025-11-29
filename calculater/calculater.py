import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        p = float(entry_principal.get())
        r = float(entry_rate.get())
        t = float(entry_time.get())
        
        interest = (p * r * t) / 100
        messagebox.showinfo("Result", f"Interest: ${interest:.2f}\nTotal: ${p + interest:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("400x250")

for label in ["Principal ($):", "Rate (%):", "Time (Years):"]:
    tk.Label(root, text=label, font=("Arial", 10)).pack(pady=5)
    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)
    if label.startswith("P"): entry_principal = entry
    elif label.startswith("R"): entry_rate = entry
    else: entry_time = entry

tk.Button(root, text="Calculate", command=calculate_interest, bg="blue", fg="white").pack(pady=20)
root.mainloop()
