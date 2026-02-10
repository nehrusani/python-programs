import time

def time_counter(seconds):
    """
    Perform a countdown timer that displays remaining time in seconds.
    
    This function counts down from a specified number of seconds to zero,
    printing the remaining time to the console in real-time. Each second,
    the display updates on the same line using carriage return. When the
    countdown completes, a "Time's up!" message is displayed.
    
    Args:
        seconds (int): The number of seconds to count down from.
                      Should be a positive integer.
    
    Returns:
        None
    
    Example:
        >>> time_counter(3)
        Time remaining: 1 seconds
        Time's up!
    
    Note:
        Requires the 'time' module to be imported.
        The function uses time.sleep(1) to create one-second intervals.
    """
    """A simple countdown timer"""
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds", end="\r")
        time.sleep(1)
    print("Time's up!                    ")

if __name__ == "__main__":
    duration = int(input("Enter countdown duration in seconds: "))
    time_counter(duration)