from turtle import Turtle
import random

COLORS = ["#192a56", "#44bd32", "#0097e6", "#341f97", "#10ac84", "#1B1464", "#006266", "#6F1E51", "#2c2c54"]
CAR_SPEED = 5


class Car:
    def __init__(self):
        self.left_lane_cars = []
        self.right_lane_cars = []
        self.car_speed = CAR_SPEED

    def generate_left_lane_car(self):
        random_interval = random.randint(1, 10)
        if random_interval == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 0)
            new_car.goto(300, random_y)
            self.left_lane_cars.append(new_car)

    def generate_right_lane_car(self):
        random_interval = random.randint(1, 10)
        if random_interval == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(80, 250)
            new_car.goto(-300, random_y)
            self.right_lane_cars.append(new_car)

    def move_cars_left_lane(self):
        for car in self.left_lane_cars:
            car.backward(self.car_speed)
            if car.xcor() < -340:
                self.left_lane_cars.remove(car)

    def move_cars_right_lane(self):
        for car in self.right_lane_cars:
            car.forward(self.car_speed)
            if car.xcor() > 340:
                self.right_lane_cars.remove(car)

    def level_up(self):
        self.car_speed += 2
