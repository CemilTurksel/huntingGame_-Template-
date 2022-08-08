from turtle import Turtle

class Defender(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("man_with_dog.gif")
        self.defender_position = (-445, -205)

    def place_defender(self):
        self.penup()
        self.goto(self.defender_position)
