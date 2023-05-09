from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.pu()
        self.random_y = random.randint(-240, 240)
        self.random_x = random.randint(-340, 340)
        self.goto(self.random_x, self.random_y)

    def car_move(self, level):
        if level == 0:
            self.setx(self.xcor() - STARTING_MOVE_DISTANCE)
        else:
            self.setx(self.xcor() - MOVE_INCREMENT * level)

    def car_reset(self):
        self.clear()
        self.random_y = random.randint(-240, 240)
        self.random_x = random.randint(340, 500)
        self.goto(self.random_x, self.random_y)
