from tkinter import *

window = Tk()
window.title('login app')
window.geometry('400x400')
def display():
    textbox.insert(END,f"Hey {name_entry.get()}\n congratuelations for your new acount")
Label(window,text="full name",bg="#00FFE5",fg='black',width=12).place(x=20,y=20)
Label(window,text="email id",bg="#00FFE5",fg='black',width=12).place(x=20,y=80)
Label(window,text="password",bg="#00FFE5",fg='black',width=12).place(x=20,y=140)
name_entry= Entry(window); name_entry.place(x=150,y=20)
email_entry= Entry(window); email_entry.place(x=150,y=20)
pass_entry = Entry(window,show="*"); pass_entry.place(x=150,y=140)
textbox = Text(frame, height=3, width=40)

btn = Button(frame, text="Create Account", command=display, bg="red")

# Place widgets using absolute positioning
frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=60)
email_entry.place(x=150, y=60)
lbl3.place(x=20, y=100)
pass_entry.place(x=150, y=100)
btn.place(x=130, y=150)
textbox.place(x=20, y=200)


window.mainloop()