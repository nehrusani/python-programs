from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

def open_file():
    path = askopenfilename(filetypes=[("text files","=.txt"),("all files","=.=")])
    if not path:return 
    txt.delete(1.0,END)
    with open(path,"r")as f :
        txt.insert(END,f.read())
    win.title(f"text editor-{path}")

def save_file():
    path = asksaveasfilename(defaultextension="txt",filetypes=[("text files","=.txt"),("all files","=.=")])
    if not path:return 
    with open(path,"w")as f :
        f.write(txt.get(1.0,END))
    win.title(f"text editor-{path}")
win = Tk()
win.title("text editor")
win.geometry("600x500")
txt = Text(win)
txt.grid(row=0,column=1,sticky="nsew")
frame = Frame(win,bd=2,relief=RAISED)
frame.grid(row=0,column=0,sticky="ns")
Button(frame,text="open",command=open_file).grid(padx=5,pady=5)
Button(frame,text="save as",command=save_file).grid(padx=5,pady=5)
win.rowconfigure(0,weight=1)
win.columnconfigure(1,weight=1)
win.mainloop()