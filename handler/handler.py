from tkinter import *

window = Tk()
window.title("event handler")
window.geometry("400x400")

def handler_express(event):
    print(event.char)

window.bind("<Key>" , handler_express)

def handle_clickevent(event):
    print("\nThe button was clicked!")

button = Button(text="click me")
button.pack()

button.bind("<Button-1>",handle_clickevent)

window.mainloop()