# File:     snake-game.py
# Author:   Nerea Salamero Labara
# Date:     august 2023
# Comms:    


import turtle
import random
import time

my_score = 0
highest_score = 0
delay = 0.1

# creating the window screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
# setting the screen size
window.setup(width=600, height=600)

# creating the snake
snake = turtle.Turtle()
snake.color("green")
snake.shape("square")
snake.goto(0, 0)
snake.penup()
snake.direction = "Stop"

# creating the food
food = turtle.Turtle()
food.speed(0)
shapes = random.choice(['triangle','circle'])
food.shape(shapes)
food.color("blue")
food.goto(0, 100)
food.penup()

# printing the title
prnt = turtle.Turtle()
prnt.speed(0)
prnt.shape('square')
prnt.color('white')
prnt.penup()
prnt.hideturtle()
prnt.goto(0, 250)
prnt.write("Your_score: 0 Highest_Score : 0", align="center", 
            font=("Arial", 24, "bold"))



# assigning directions
#   Right   = D
#   Left    = A
#   Up      = W
#   Down    = S
def moveRight():
    if snake.direction != "left":
        snake.direction = "right"

def moveLeft():
    if snake.direction != "right":
        snake.direction = "left"

def moveUp():
    if snake.direction != "down":
        snake.direction = "up"

def moveDown():
    if snake.direction != "up":
        snake.direction = "down"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)

window.listen()
window.onkeypress(moveRight, 'D')
window.onkeypress(moveLeft, 'A')
window.onkeypress(moveUp, 'W')
window.onkeypress(moveDown, 'S')

segments = []

# Main implementation of the game
while True:
    window.update()
    if snake.ycor() > 290 or snake.ycor() < -290 or snake.xcor() > 290 or snake.xcor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "Stop"
        snake.shape("square")
        snake.color("green")

        for s in segments:
            s.goto(1000,1000)
        segments.clear()
        prnt.clear()
        my_score = 0
        delay = 0.1
        prnt.write("Player's_score: {} Highest_score: {}".format(my_score, highest_score), 
                    align="center", font=("Arial", 24, "bold"))

    # eating one piece of food
    if snake.distance(food) < 20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x, y)

        # adding new segment (because I've eaten one piece of food)
        added = turtle.Turtle()
        added.speed(0)
        added.shape("square")
        added.color("white")
        added.penup()
        segments.append(added)
        delay -= 0.001

        # updating scoreboard
        my_score += 5
        if my_score > highest_score:
            highest_score = my_score
        prnt.clear()
        prnt.write("Player's_score: {} Highest_score: {}".format(my_score, highest_score), 
                    align="center", font=("Arial", 24, "bold"))
    
    # checking for collisions
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)
    move()

    for s in segments:
        if s.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            snake.color('white')
            snake.shape('square')

            for s in segments:
                s.goto(1000,1000)
            segments.clear()
            prnt.clear()
            my_score = 0
            delay = 0.1
            prnt.write("Player's_score: {} Highest_score: {}".format(my_score, highest_score), 
                        align="center", font=("Arial", 24, "bold"))
    time.sleep(delay)
window.mainloop()