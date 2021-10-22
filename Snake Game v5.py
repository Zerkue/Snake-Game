# Line 181 make bad food apear every 10 score

import turtle
import time
import random

delay = 0.11

# Score Variables
current_score = 0
highest_score = 0

# Segments And Bad Food Preset
segments = []
bad_foods = []

# Death Function
def death():
    # At Death
    wn.bgcolor("red")
    time.sleep(1)
    head.goto(0, 0)
    pen.clear()
    pen.write("Score: " + str(current_score) + "    High Score: " + str(highest_score), align="center", font=("courier", 24, "normal"))

    # Food Relocation
    move_food()

    # After Death
    wn.bgcolor("green")
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)

    # Clear the segments list
    segments.clear()

    # Hide The Bad Food
    for bad_food in bad_foods:
        bad_food.goto(1000, 1000)

    # Clear The Bad Food List
    bad_foods.clear()

    # Re-Spawn A Bad Food
    bad_food = turtle.Turtle()
    bad_food.speed(0)
    bad_food.shape("triangle")
    bad_food.color("purple")
    bad_food.penup()
    bad_foods.append(bad_food)

    x2 = random.randint(-14, 14) * 20
    y2 = random.randint(-14, 14) * 20
    bad_food.goto(x2, y2)


# Move Food And Bad Food To Random locations
def move_food():
    x = random.randint(-14, 14) * 20
    y = random.randint(-14, 14) * 20
    food.goto(x, y)

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Venom")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
move_food()

# Making bad food
bad_food = turtle.Turtle()
bad_food.speed(0)
bad_food.shape("triangle")
bad_food.color("purple")
bad_food.penup()
bad_foods.append(bad_food)

#Move Bad Food To Random location
def move_bad_food():
    x2 = random.randint(-14, 14) * 20
    y2 = random.randint(-14, 14) * 20
    bad_food.goto(x2, y2)
move_bad_food()

# Write score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Score: " + str(current_score) + "    High Score: " + str(highest_score), align="center", font=("courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with border and effects
    if head.xcor()>290 or head.ycor()>290 or head.xcor()<-290 or head.ycor()<-290:
        death()
        current_score = 0
        delay = 0.11
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(current_score, highest_score), align="center",
                  font=("courier", 24, "normal"))

    # check for a collision with food
    if head.distance(food) < 20:
        # Move food to random spot on the screen
        move_food()

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment .speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        # Spawn In A New Bad Food Item
        bad_food = turtle.Turtle()
        bad_food.speed(0)
        bad_food.shape("triangle")
        bad_food.color("purple")
        bad_food.penup()
        bad_foods.append(bad_food)

        move_bad_food()

        #shorten Delay
        delay -= 0.001

        # Increase The Score
        current_score += 1
        if current_score > highest_score:
            highest_score = current_score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(current_score, highest_score), align="center", font=("courier", 24, "normal"))

    # Check for a collision with bad food
    for bad_food in bad_foods:
        if head.distance(bad_food) < 20:
            if current_score > 0:
                current_score -= 1
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(current_score, highest_score), align="center",
                          font=("courier", 24, "normal"))

                move_bad_food()


                segments.pop().goto(1000, 1000)


                # Add New Bad Food Items Every Time A Collision With Ba Food Happens
                bad_food = turtle.Turtle()
                bad_food.speed(0)
                bad_food.shape("triangle")
                bad_food.color("purple")
                bad_food.penup()
                bad_foods.append(bad_food)

                move_bad_food()

                bad_food = turtle.Turtle()
                bad_food.speed(0)
                bad_food.shape("triangle")
                bad_food.color("purple")
                bad_food.penup()
                bad_foods.append(bad_food)

                move_bad_food()

            # Deals With Death Casued By Bad Food
            else:
                death()
                current_score = 0
                delay = 0.11
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(current_score, highest_score), align="center",
                          font=("courier", 24, "normal"))

    # move the end segments first in reversal order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            death()
            current_score = 0
            delay = 0.11
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(current_score, highest_score), align="center",
                      font=("courier", 24, "normal"))
    if len(segments) > 0:
        if head.distance(segments[0]) < 20:
            death()
            current_score = 0
            delay = 0.11
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(current_score, highest_score), align="center",
                      font=("courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()