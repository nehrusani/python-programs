from tkinter  import * 

main = Tk()
main.geometry("400x600")
main.title("hungry king")
label = Label(main, text="click here !!!!", font=("comic", 30))
label.pack()
button = Button(main, text="Click Me", command=lambda: open_window())
button.pack()

def open_window():
    new_window = Toplevel(main)
    new_window.geometry("300x400")
    new_window.title("New Window")
    label = Label(new_window, text="you are a genius", font=("comic", 20))
    label.pack()

button = Button(main, text="Click Me", command=open_window)
mainloop()
