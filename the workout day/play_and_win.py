import tkinter as tk
import webbrowser

def open_wowki():
    webbrowser.open("https://wokwi.com")

root = tk.Tk()
root.title("Play and Win")
root.geometry("400x400")

button = tk.Button(root, text="Open Wowki", command=open_wowki)
button.pack(pady=20)

root.mainloop()
