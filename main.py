from turtle import Turtle, Screen
import time
import random
from snake import Snake
screen = Screen()
screen.title("The Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
screen.update()

screen.listen()
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")

food = Turtle("circle")
food.penup()
food.shapesize(0.5, 0.5)
food.color("red")


def generate_food():
    while True:
        food.goto(random.randrange(-280, 280), random.randrange(-280, 280))
        if food not in snake.start_positions:
            break


generate_food()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.add_segment()
        generate_food()

    # Detect collision with walls
    if abs(snake.head.xcor()) >= 305 or abs(snake.head.ycor()) >= 305:
        print("wall")
        play_again = screen.textinput(title="Want to play again?", prompt="Do you want to play again?")
        if play_again == "y":
            game_on = True
            snake.clear()
            snake = Snake()
            continue
        game_on = False
        break
    # Detect collision with tail
    if snake.head.position() in snake.start_positions:
        print("tail")
        break

screen.exitonclick()
