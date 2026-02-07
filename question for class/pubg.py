class PUBGEligibility:
    def __init__(self, age):
        self.age = age
    
    def can_play_pubg(self):
        return self.age >= 13
    
    def get_answer(self):
        if self.can_play_pubg():
            return f"You are {self.age} years old. You CAN play PUBG!"
        else:
            return f"You are {self.age} years old. You CANNOT play PUBG. Minimum age is 13."