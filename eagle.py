from turtle import Turtle


class Eagle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("eagle.gif")

    def place_eagle(self):
        self.penup()
        self.goto(-450, -50)
