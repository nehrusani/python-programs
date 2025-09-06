class StringReverser:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text[::-1]

# Example usage:
if __name__ == "__main__":
    s = StringReverser("Hello World")
    print(s)