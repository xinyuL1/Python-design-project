import turtle as bob
from random import randint as rint
bob.shape("turtle")
bob.pensize(5)
bob.colormode(255)
bob.bgcolor("black")
bob.tracer(False)
for times in range(500):
     bob.color(rint(0,255),rint(0,255),rint(0,255))
     bob.circle(2*(1+times/4),5)
     bob.speed(20)
     bob.tracer(True)
