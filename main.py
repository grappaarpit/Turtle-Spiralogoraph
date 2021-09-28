import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
t.speed(10)
t.width(4)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
for i in range(0,36):
  t.circle(100)
  t.color(random_color())
  t.left(10)



