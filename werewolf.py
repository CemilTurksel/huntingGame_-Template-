from turtle import Turtle
import time


class Werewolf(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("werewolf.gif")
        self.werewolf_starting_position = (210, -200)
        self.werewolf_x = self.xcor()
        self.message = Turtle()

    def place_werewolf(self):
        self.penup()
        self.goto(self.werewolf_starting_position)

    def move_werewolf(self):
        self.forward(20)
        time.sleep(1)

    def werewolf_auch(self):
        self.message.goto(0, 0)
