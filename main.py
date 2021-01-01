from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
screen = Screen()
screen.title("The Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()

screen.update()

screen.listen()
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.add_segment()
        food.generate_food()

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
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            break

screen.exitonclick()
