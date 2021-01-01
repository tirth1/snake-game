from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.title("The Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.update()
screen.title("Welcome to the turtle zoo!")
screen.listen()
screen.onkeypress(fun=snake.move_left, key="Left")
screen.onkeypress(fun=snake.move_right, key="Right")
screen.onkeypress(fun=snake.move_up, key="Up")
screen.onkeypress(fun=snake.move_down, key="Down")


game_on = True
score_board.show_score()
while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score_board.clear()
        score_board.show_score()
        snake.add_segment()
        food.generate_food()

    # Detect collision with walls
    if abs(snake.head.xcor()) >= 305 or abs(snake.head.ycor()) >= 305:
        score_board.game_over()
        game_on = False
        break

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            game_on = False
            break

screen.exitonclick()
