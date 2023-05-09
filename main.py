import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

NUMBER_OF_CARS = 20


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = []
for i in range(0, NUMBER_OF_CARS):
    car = CarManager()
    cars.append(car)
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.player_move_forward, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for rand_car in cars:
        rand_car.car_move(scoreboard.level)
        if rand_car.xcor() < -380:
            rand_car.car_reset()
        if rand_car.distance(x=player.xcor(), y=player.ycor()) <= 24:
            rand_car.xcor()
            scoreboard.end_game()
            game_is_on = False
    if player.finish():
        player.new_level()
        scoreboard.next_level()

screen.exitonclick()
