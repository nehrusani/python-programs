class nehru_name :
    def __init__(self, g):
        self.g = g
        self.valid = (g == "nehru")

        if self.valid:
           import nehru_math
           h = int(input("Enter first value: "))
           h1 = int(input("Enter second value: "))
           pree = nehru_math.nehru_math(h, h1)
           print(pree.add()) 

            
    def __str__(self):
        if not self.valid:
            return f"Invalid name entered: {self.g}"
        return ""

