class putti_command:
    def __init__(self, putti=int(input())):
        self.putti = putti

    def covoro(self):
        # if putti is 32 or greater, deny; otherwise accept
        if self.putti >= 32:
            print("no way!!!")
        else:
            print("you have been accepted!!!")


jojobi = putti_command()
jojobi.covoro()