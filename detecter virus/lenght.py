import tkinter as tk
from tkinter import ttk

def convert():
    try:
        inches = float(entry_inches.get())
        
        # Convert to other units
        centimeters = inches * 2.54
        feet = inches / 12
        meters = inches * 0.0254
        
        # Display results
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"{inches} inches = \n\n")
        result_text.insert(tk.END, f"{centimeters:.2f} cm\n")
        result_text.insert(tk.END, f"{feet:.2f} feet\n")
        result_text.insert(tk.END, f"{meters:.2f} meters")
        result_text.config(state=tk.DISABLED)
    except ValueError:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a valid number")
        result_text.config(state=tk.DISABLED)

# Create window
root = tk.Tk()
root.title("Inches Converter")
root.geometry("300x300")

# Input label and entry
tk.Label(root, text="Enter inches:", font=("Arial", 12)).pack(pady=10)
entry_inches = tk.Entry(root, font=("Arial", 12), width=20)
entry_inches.pack(pady=5)

# Convert button
tk.Button(root, text="Convert", command=convert, bg="blue", fg="white", font=("Arial", 11)).pack(pady=10)

# Result display
result_text = tk.Text(root, height=8, width=30, state=tk.DISABLED)
result_text.pack(pady=10)

root.mainloop()