from turtle import Turtle, Screen


class Snake(Turtle):

    start_positions = [(0, 0), (-20, 0), (-40, 0)]
    move_distance = 20
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.start_positions:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.goto(position)
            new_segment.color("white")
            self.segments.append(new_segment)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)

        self.segments[0].fd(self.move_distance)

    def move_up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def move_down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def move_right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def move_left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_x = self.segments[len(self.segments) - 1].xcor()
        new_y = self.segments[len(self.segments) - 1].ycor()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)