class bird :
    def __init__(self):
        print("bird is raedy")
    def who_is_this(self):
        print("bird")
    def swimm(self):
        print("swimm faster")
class panguin(bird) :
    def __init__(self):
        super().__init__()
        print("panguin is ready")
    def who_is_this(self):
        print("panguin")
    def run(self):
        print("run faster")
birdherro = panguin()
birdherro.run()
birdherro.swimm()
birdherro.who_is_this()