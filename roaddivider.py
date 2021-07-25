from turtle import Turtle


class RoadDivider:
    def __init__(self):
        self.divider_segments = []
        self.create_divider()

    def create_divider(self):
        x_cor = 280
        for _ in range(8):
            divider = Turtle("square")
            divider.color("#2C3A47")
            divider.shapesize(stretch_wid=0.5, stretch_len=2)
            divider.penup()
            divider.goto(x_cor, 40)
            x_cor -= 80
            self.divider_segments.append(divider)
