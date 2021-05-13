import turtle
import time
import random

# Score, Delay and HighScore
score = 0
delay = 0.1
high_score = 0

# Game Window
wn = turtle.Screen()
wn.title("Snake Game by FelipeS")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food
food = turtle.Turtle()
colors = random.choice(["red", "blue", "green"])
shapes = random.choice(["turtle", "circle"])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# Pen
segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
pen.write("Score: 0 - High Score: 0", align="center", font=("Courier", 12, "bold"))

# Functions


def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)


def go_up():
    if head.direction != "Down":
        head.direction = "Up"


def go_down():
    if head.direction != "Up":
        head.direction = "Down"


def go_right():
    if head.direction != "Left":
        head.direction = "Right"


def go_left():
    if head.direction != "Right":
        head.direction = "Left"


# Binding Buttons
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")


# Main Game Loop
while True:
    wn.update()

    # Snake Border Behaviour
    # Collision with the border.
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {} - High Score: {}".format(score, high_score), align="center", font=("Courier", 12, "bold"))
    # Snake Growth
    if head.distance(food) < 18:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay += 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} - High Score: {}".format(score, high_score), align="center", font=("Courier", 12, "bold"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(["red", "blue", "green"])
            shapes = random.choice(["turtle", "circle"])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {} - High Score: {}".format(score, high_score), align="center", font=("Courier", 12, "bold"))
    time.sleep(delay)

