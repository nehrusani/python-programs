import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        birth_year = int(year_entry.get())
        current_year = datetime.now().year
        age = current_year - birth_year
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Please enter a valid year!")

# Create main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

# Create and pack widgets
title_label = tk.Label(root, text="Age Calculator", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

year_label = tk.Label(root, text="Enter your birth year:")
year_label.pack()

year_entry = tk.Entry(root)
year_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the application
root.mainloop()