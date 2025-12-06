import tkinter
import random
import time
import threading

print("You are in a cursed colony haunted by the infamous Nany Villa...")

root = tkinter.Tk()
root.title("Liv or Die")
root.geometry("400x320")
root.configure(bg="black")

# --- IMAGE (same as yours) ---
image = tkinter.PhotoImage(file="horror.png")
label = tkinter.Label(root, image=image, bg="black")
label.image = image
label.pack()

# --- FLASHING HORROR TEXT ---
scary_text = tkinter.Label(
    root, 
    text="⚠️ ESCAPE IF YOU CAN ⚠️", 
    fg="red", 
    bg="black",
    font=("Arial", 16, "bold")
)
scary_text.pack(pady=10)

def flash_text():
    colors = ["red", "darkred", "black", "yellow"]
    while True:
        for c in colors:
            scary_text.config(fg=c)
            time.sleep(0.2)

t = threading.Thread(target=flash_text, daemon=True)
t.start()

# -----------------------------------
#        MAIN GAME START
# -----------------------------------
def start_game():
    root.destroy()
    game_root = tkinter.Tk()
    game_root.title("Liv or Die - Game")
    game_root.geometry("420x330")
    game_root.configure(bg="black")

    # Creepy intro text
    game_label = tkinter.Label(
        game_root, 
        text="You step inside the haunted villa...\nThe door locks behind you.",
        fg="red", bg="black", 
        font=("Arial", 13, "bold")
    )
    game_label.pack(pady=20)

    # Random creepy whisper messages
    whispers = [
        "you shouldn't be here...",
        "she’s watching you...",
        "don’t turn around...",
        "run... while you still can...",
        "she wants a new soul..."
    ]

    def whisper_loop():
        whisper_label = tkinter.Label(game_root, fg="darkred", bg="black", font=("Arial", 10, "italic"))
        whisper_label.pack()
        while True:
            whisper_label.config(text=random.choice(whispers))
            time.sleep(2)

    threading.Thread(target=whisper_loop, daemon=True).start()

    # Question
    question = tkinter.Label(
        game_root, 
        text="A dark hallway splits into two.\nDo you go left or right?",
        fg="white", bg="black", font=("Arial", 12)
    )
    question.pack(pady=10)

    # Buttons
    left_btn = tkinter.Button(
        game_root, text="Go Left", fg="white", bg="darkred",
        command=lambda: choice("left"), width=20
    )
    left_btn.pack(pady=5)

    right_btn = tkinter.Button(
        game_root, text="Go Right", fg="white", bg="darkred",
        command=lambda: choice("right"), width=20
    )
    right_btn.pack(pady=5)

    # Logic with horror outcomes
    def choice(direction):
        left_outcomes = [
            "You survived… for now.",
            "A shadow passes behind you… but ignores you.",
            "You step on bones… but nothing attacks."
        ]

        right_outcomes = [
            "A scream pierces your ears… GAME OVER!",
            "Something grabs your leg and drags you into darkness!",
            "She found you. You never escape Nany Villa."
        ]

        if direction == "left":
            result = random.choice(left_outcomes)
        else:
            result = random.choice(right_outcomes)

        game_label.config(text=result)
        left_btn.config(state="disabled")
        right_btn.config(state="disabled")


# START BUTTON
start_btn = tkinter.Button(
    root, 
    text="▶️ ENTER THE VILLA ▶️", 
    fg="white", bg="darkred",
    command=start_game, 
    font=("Arial", 12, "bold"),
    activeforeground="yellow", activebackground="darkred",
    relief="raised", bd=3
)
start_btn.pack(pady=10)

root.mainloop()
