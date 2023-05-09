from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.pu()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def player_move_forward(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def new_level(self):
        self.clear()
        self.goto(STARTING_POSITION)
