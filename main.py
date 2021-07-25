from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time

# Screen object definition
screen = Screen()
screen.bgcolor("#f1c40f")
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# Player object definition
player = Player()

# Turtle control
screen.listen()
screen.onkey(player.move_forward, "Up")

# Car object definition
car = Car()

# Scoreboard object definition
score = Scoreboard()

# While loop for the game
end_game = False
while not end_game:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_cars()
    print(car.cars)
    # Detect collision with the car
    for each_car in car.cars:
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
