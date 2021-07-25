from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
from roaddivider import RoadDivider
import time

# Screen object definition
screen = Screen()
screen.bgcolor("#f1c40f")
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# Road Divider object definition
road_divider = RoadDivider()

# Player object definition
player = Player()

# Turtle control
screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

# Car object definition
car = Car()

# Scoreboard object definition
score = Scoreboard()

# While loop for the game
end_game = False
while not end_game:
    time.sleep(0.1)
    screen.update()
    car.generate_left_lane_car()
    car.move_cars_left_lane()
    car.generate_right_lane_car()
    car.move_cars_right_lane()
    # Detect collision with the car
    for each_car in car.left_lane_cars:
        if each_car.distance(player) < 20:
            score.game_over()
            end_game = True
    for each_car in car.right_lane_cars:
        if each_car.distance(player) < 20:
            score.game_over()
            end_game = True
    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        score.increase_score()
        car.level_up()

# Screen exit
screen.exitonclick()
