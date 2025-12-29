l = 3
print("YTOHPN")
x = str(input("enter the word :"))
if x == "python" or x == "PYTHON":
    print("correct answer lets swicht to the next question")
    l = l + 1
    print("your life is",l)
else:
    print("this is incorrect : python")
    l = l - 1
    print("you have to improve",l)
print("PTINR")
z = str(input("enter the correct word : "))
if z == "PRINT" or z == "print" :
    print("exelent")
    l = l + 1
    print(l)
else :
    print("improve more : print")
    l = l - 1
    print(l)
if l == 0 :
    breakpoint()
print("this is you last chance to win ")
print("NEACPUESLIOTN")
g = str(input("enter the correct word : "))
if g == "ENCAPSUELATION" or g == "encapsuelation" :
    print("you won!!!")
else:
    print("sorry")
print("🥇")


