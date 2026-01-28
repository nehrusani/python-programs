import time
def text_breack():
    time.sleep(8)
    
print("you are alone in your school no one likes you because of you skin color")
print("do you want to skip")
text_breack()
g = str(input())
for char in g:
    time.sleep(2)
if g == "yes":
    exit()
else:
    print("ok fine")
    print("will you be " \
    "\n a. nervous" \
    "\n b. ignoring")
    text_breack()
    i = str(input())
    if i == "a":
        print("ok so")
        print("you want in to a new school and there every one bullied you")
        print("and you left the and when there was no one to tacke care of you")
        print("you are poor")
        text_breack()
    elif i == "b":
        print("so you did not lose now you went ahead and studied harder")
        print("you now get an a+ and then ... ")
        print("thank you for enjoying " \
        "\n and always it does not matter how you are it dependce " \
        "\n how much sucess you get in your life and your self " \
        "\n you will get friends by your courage and sucess")
        print("please play our next game !!!")
        text_breack()
        exit()
    else:
        print("please enter a vaild input")
        text_breack()
        exit()