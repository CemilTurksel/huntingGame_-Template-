from turtle import Turtle

class Cave(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("cave.gif")
        self.cave_position = (385, -190)

    def place_cave(self):
        self.penup()
        self.goto(self.cave_position)