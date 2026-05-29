class big_bucket:
    def __init__(self):
        self.bigbucket = int(input())
        self.putti = int(input())

    def carvup(self):
        if self.bigbucket <= 98:
            return complex(self.bigbucket, self.putti)
        return None

if __name__ == "__main__": # this line means to run the file directly 
    core = big_bucket()
    result = core.carvup()
    if result is not None:
        print(result)