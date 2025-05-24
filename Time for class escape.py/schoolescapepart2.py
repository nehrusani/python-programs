


import turtle

# Initialize screen and player
wn = turtle.Screen()
wn.title("School Escape")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)

player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)

# Initialize revives and reset function
revives = 3
def reset_revives():
    global revives
    revives = 3

# Initialize game state at the start
reset_revives()

# Optionally, display the number of revives on the screen
revive_display = turtle.Turtle()
revive_display.hideturtle()
revive_display.penup()
revive_display.goto(-280, 260)
revive_display.write(f"Revives: {revives}", font=("Arial", 16, "bold"))

def update_revive_display():
    revive_display.clear()
    revive_display.write(f"Revives: {revives}", font=("Arial", 16, "bold"))

# Example: Decrease revives and update display (call this when player loses a life)
def lose_life():
    global revives
    if revives > 0:
        revives -= 1
        update_revive_display()
    else:
        wn.bye()  # End game or handle game over

# Example: Bind a key to lose a life for testing
wn.listen()
wn.onkey(lose_life, "space")

# --- More game logic for a longer file (up to 119 lines) ---

# Obstacles
obstacles = []

def create_obstacle(x, y):
    obs = turtle.Turtle()
    obs.shape("square")
    obs.color("red")
    obs.penup()
    obs.goto(x, y)
    obstacles.append(obs)

# Create some obstacles
for i in range(-200, 201, 100):
    create_obstacle(i, 100)
    create_obstacle(i, 0)
    create_obstacle(i, -100)

# Move player
def move_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + 20)

def move_up():
    y = player.ycor()
    if y < 280:
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -280:
        player.sety(y - 20)

wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")

# Collision detection
def check_collision():
    for obs in obstacles:
        if player.distance(obs) < 20:
            lose_life()
            player.goto(0, -250)
            break

# Goal
goal = turtle.Turtle()
goal.shape("circle")
goal.color("gold")
goal.penup()
goal.goto(0, 250)

def check_goal():
    if player.distance(goal) < 20:
        global best_game
        best_game = "Win"
        wn.bye()

# Main game loop
def game_loop():
    check_collision()
    check_goal()
    wn.ontimer(game_loop, 100)

game_loop()

# Instructions
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(-280, -280)
instructions.write("Arrow keys to move. Reach the gold circle. Space to lose a life.", font=("Arial", 10, "normal"))

wn.mainloop()