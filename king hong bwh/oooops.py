import winsound
from tkinter import *
from PIL import Image, ImageTk

def play_sound():
    winsound.PlaySound("gin.mp3", winsound.SND_FILENAME)

main = Tk()
button = Button(
    main,
    text="Play Song",
    command=play_sound
)
button.pack(pady=20)
bg = "divi.png"
main.geometry("600x600")
main.title("Divija birth day")
image = Image.open(bg)
photo = ImageTk.PhotoImage(image)
label = Label(main, image=photo)
label.image = photo
label.pack()
text_label = Label(main, text="place is Bahnstraße 72, 40210 Düsseldorf pavitra restaurent",font="Arial")
text_label.pack(pady=20)
main.mainloop()
