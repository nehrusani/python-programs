import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Calculator")
screen.setup(width=400, height=600)
screen.tracer(0)

# Global variables
current = ""
operator = ""
operand = ""
result = ""

# Draw display
display = turtle.Turtle()
display.hideturtle()
display.penup()
display.goto(-180, 220)
display.pendown()

def draw_display(text):
    display.clear()
    display.penup()
    display.goto(-180, 220)
    display.pendown()
    display.fillcolor("white")
    display.begin_fill()
    for _ in range(2):
        display.forward(360)
        display.right(90)
        display.forward(60)
        display.right(90)
    display.end_fill()
    display.penup()
    display.goto(-170, 180)
    display.pendown()
    display.color("black")
    display.write(text, font=("Arial", 24, "normal"))

# Button class
class Button:
    def __init__(self, x, y, w, h, label, callback):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.label = label
        self.callback = callback
        self.draw()

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.fillcolor("lightgray")
        t.begin_fill()
        for _ in range(2):
            t.forward(self.w)
            t.right(90)
            t.forward(self.h)
            t.right(90)
        t.end_fill()
        t.penup()
        t.goto(self.x + self.w/2 - 10, self.y - self.h/2 - 10)
        t.pendown()
        t.write(self.label, font=("Arial", 20, "bold"))
        t.penup()
        t.goto(0, 0)
        t.pendown()

    def is_clicked(self, x, y):
        return self.x <= x <= self.x + self.w and self.y - self.h <= y <= self.y

# Button callbacks
def button_click(label):
    global current, operator, operand, result
    if label in "0123456789":
        current += label
        draw_display(current)
    elif label in "+-*/":
        if current:
            operand = current
            operator = label
            current = ""
            draw_display(operator)
    elif label == "=":
        if operand and operator and current:
            try:
                result = str(eval(operand + operator + current))
            except Exception:
                result = "Error"
            draw_display(result)
            current = result
            operator = ""
            operand = ""
    elif label == "C":
        current = ""
        operator = ""
        operand = ""
        result = ""
        draw_display("")

# Create buttons
buttons = []
labels = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]
start_x, start_y = -150, 100
w, h = 80, 60

for row in range(4):
    for col in range(4):
        label = labels[row][col]
        x = start_x + col * (w + 10)
        y = start_y - row * (h + 10)
        buttons.append(Button(x, y, w, h, label, lambda l=label: button_click(l)))

# Mouse click handler
def on_click(x, y):
    for btn in buttons:
        if btn.is_clicked(x, y):
            btn.callback(btn.label)
            break

draw_display("")
screen.onclick(on_click)
screen.listen()
screen.mainloop() 