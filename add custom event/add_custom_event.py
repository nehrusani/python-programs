from threading import Event
import time
import pygame

class CustomEventHandler:
    def __init__(self):
        self.event = Event()
        pygame.init()
    def wait_for_event(self):
        print("Waiting for event to be triggered...")
        self.event.wait()  # Wait until the event is set
        print("Event has been triggered!")
        
    def trigger_event(self):
        print("Triggering the event")
        self.event.set()  # Set the event
        
    def reset_event(self):
        self.event.clear()  # Reset the event

def main():
    # Create an instance of CustomEventHandler
    handler = CustomEventHandler()
    
    # Start waiting for the event
    print("Program started")
    handler.wait_for_event()
    
    # Simulate some work
    time.sleep(2)
    
    # Trigger the event
    handler.trigger_event()
    
    # Reset the event for future use
    handler.reset_event()

if __name__ == "__main__":
    main()