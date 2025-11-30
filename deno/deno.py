from tkinter import *
from tkinter import messagebox
from PIL import image,imagetk
root = Tk()
root.title("denominater curiculem")
root.configure(bg="light blue")
root.geometry("650x400")
upload = image.open("holo.png")
upload=upload.resize((300,300))
image = imagetk.photoimage(upload)
label = Label(root,image=image,bg = "lightblue")
label.place(x=180,y=20)
label1 = 