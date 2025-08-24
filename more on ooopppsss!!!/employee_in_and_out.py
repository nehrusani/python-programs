class Employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destructer call")
def create_object():
    print("macking object")
    obJ = Employee()
    print("function end")
    return obJ
print("calling create object method")
obJ = create_object()
print("programm ended") 
