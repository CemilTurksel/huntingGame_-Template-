from turtle import *
from defender import Defender
from bullet import Bullet
from cave import Cave
from grass import Grass
from werewolf import Werewolf
from eagle import Eagle


# Screen settings
screen = Screen()
screen.setup(1000, 500)
screen.addshape("man_with_dog.gif")
screen.addshape("bullet.gif")
screen.addshape("cave.gif")
screen.addshape("fullmoon.gif")
screen.addshape("werewolf.gif")
screen.addshape("eagle.gif")
screen.listen()
#screen.tracer(0)

# Defender object
defender = Defender()
defender.place_defender()

# Grass object
grass = Grass()
grass.place_grass()

# Bullet object
bullet = Bullet()
bullet.place_bullet_in_rifle()
screen.onkey(fun=bullet.fire_bullet, key="space")
screen.onkey(fun=bullet.reload_bullet, key="r")

# Cave object
cave = Cave()
cave.place_cave()

# Fullmoon
fullmoon = Turtle()
fullmoon.shape("fullmoon.gif")
fullmoon.penup()
fullmoon.goto(0, 100)

# Werewolf
werewolf = Werewolf()
werewolf.place_werewolf()
werewolf.left(180)

# Eagle
eagle = Eagle()
eagle.place_eagle()

# Eagle nest
nest = Turtle()
nest.shape("square")
nest.shapesize(stretch_len=5, stretch_wid=1)
nest.penup()
nest.goto(-450, -100)

# Game loop
is_game_on = True
while is_game_on:
    screen.update()
    werewolf.move_werewolf()
    if bullet.xcor() > werewolf.xcor():
        werewolf.hideturtle()
        werewolf.goto(werewolf.werewolf_starting_position)
        werewolf.showturtle()
        bullet.reload_bullet()
    werewolf.move_werewolf()





screen.exitonclick()

