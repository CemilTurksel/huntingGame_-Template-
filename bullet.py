from werewolf import *


class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("bullet.gif")
        self.shapesize(0.2)
        self.bullet_position = (-403, -178)

    def place_bullet_in_rifle(self):
        self.penup()
        self.goto(self.bullet_position)

    def reload_bullet(self):
        self.penup()
        self.goto(self.bullet_position)
        self.showturtle()

    def fire_bullet(self):
        self.speed(5)
        self.forward(605)
        self.hideturtle()
