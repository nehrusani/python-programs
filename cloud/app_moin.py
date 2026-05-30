import sys # running python built in function sys

class app_moin:
    def __init__(self, moin=input(()), app=input(())):
        self.moin = sys.intern(moin) # stores value and pass strings through
        self.app = sys.intern(app) # stores value and pass strings through 
    def cover_up(self):
        if self.moin is self.app:
            print("you enter the write passwor wich you did " \
            "before")
sparrow = app_moin()
sparrow.cover_up()