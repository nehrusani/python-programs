import time

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("You wake up in a dark, cold room. The only light comes from a flickering candle.")
    slow_print("There are two doors: one to your left, and one to your right.")
    slow_print("Which door do you choose? (left/right)")

def left_room():
    slow_print("You open the left door. It creaks loudly.")
    slow_print("Inside, you see a shadow move across the wall.")
    slow_print("Do you investigate or run away? (investigate/run)")

def right_room():
    slow_print("You open the right door. The air is colder here.")
    slow_print("A whisper calls your name. Do you follow the voice or hide? (follow/hide)")

def investigate():
    slow_print("You step closer to the shadow. Suddenly, it lunges at you!")
    slow_print("GAME OVER.")

def run_away():
    slow_print("You run back to the main room, heart pounding.")
    slow_print("But the doors are now gone. You're trapped forever.")
    slow_print("GAME OVER.")

def follow_voice():
    slow_print("You follow the whisper. It leads you to a hidden staircase.")
    slow_print("You escape the house. You survived!")
    slow_print("YOU WIN.")

def hide():
    slow_print("You hide behind a dusty curtain. The whisper grows louder until it’s right behind you.")
    slow_print("GAME OVER.")

def main():
    intro()
    choice = input("> ").strip().lower()
    if choice == "left":
        left_room()
        choice2 = input("> ").strip().lower()
        if choice2 == "investigate":
            investigate()
        elif choice2 == "run":
            run_away()
        else:
            slow_print("You hesitate and the darkness consumes you.")
            slow_print("GAME OVER.")
    elif choice == "right":
        right_room()
        choice2 = input("> ").strip().lower()
        if choice2 == "follow":
            follow_voice()
        elif choice2 == "hide":
            hide()
        else:
            slow_print("You freeze in fear. The whisper finds you.")
            slow_print("GAME OVER.")
    else:
        slow_print("Unable to decide, you remain in the darkness forever.")
        slow_print("GAME OVER.")

if __name__ == "__main__":
    main()