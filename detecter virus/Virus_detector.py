# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.title("Virus Scanner")
root.geometry("300x200")

# Function for displaying warning message
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", font=("Arial", 12), command=msg)
button.place(x=90, y=80)

# Entering main event loop
root.mainloop()
