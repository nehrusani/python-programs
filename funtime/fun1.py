import time
import random

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("You wake up in a dark, cold room. The only light comes from a flickering candle.")
    slow_print("You hear footsteps echoing in the distance...")
    time.sleep(1)
    slow_print("Do you:")
    slow_print("1. Explore the room")
    slow_print("2. Call out for help")
    slow_print("3. Stay still and listen")

def explore_room():
    slow_print("You feel your way around the room. Your hand brushes against something slimy...")
    slow_print("Suddenly, you hear a whisper: 'Don't touch that...'")
    return random.choice([True, False])

def call_for_help():
    slow_print("You shout for help. The footsteps stop. Silence.")
    slow_print("Then, a voice whispers behind you: 'They can hear you now.'")
    return random.choice([True, False])

def stay_still():
    slow_print("You hold your breath and listen. The footsteps get closer... and closer...")
    slow_print("A cold hand grabs your shoulder!")
    return random.choice([True, False])

def ending(survived):
    if survived:
        slow_print("You manage to escape the room as the door creaks open. You're safe... for now.")
    else:
        slow_print("A shadowy figure emerges from the darkness. You feel icy fingers around your neck...")
        slow_print("Game Over.")

def main():
    intro()
    choice = input("Enter 1, 2, or 3: ")
    survived = False
    if choice == '1':
        survived = explore_room()
    elif choice == '2':
        survived = call_for_help()
    elif choice == '3':
        survived = stay_still()
    else:
        slow_print("You hesitate too long. Something finds you in the dark...")
    ending(survived)

if __name__ == "__main__":
    main()