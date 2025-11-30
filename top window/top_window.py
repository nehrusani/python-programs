from tkinter import *

ditya = Tk()
ditya.geometry("400x300")
ditya.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top,text = ("This ia a toplevel window!!!"))
    l2.pack()

    top.mainloop()

l = Label(ditya,text="This is a ditya window")
btn = Button(ditya,text="click here to get a toplevel window", command=topwin)

l.pack()
btn.pack()

ditya.mainloop()