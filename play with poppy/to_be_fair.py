from tkinter import Tk
from tkinter import Button

gool = Tk()
gool.geometry("500x700")
gool.title("learn")
gool.config(bg= "blue")
def button_time():
    letsgo = Tk()
    letsgo.geometry("500x700")
    letsgo.title("welcome back")
    letsgo.config(bg="pink")
    letsgo.mainloop()
button=Button(gool,text="start", command=button_time)
button.pack()
gool.mainloop()