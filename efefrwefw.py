import turtle
bob = turtle.Pen()
turtle.bgcolor("black")
sides = 7
color =["red","orange","yellow","green","cyan","blue","purple"]
for times in range(120):
     bob.pencolor(color[times%sides])
     bob.forward(times*3/sides+times)
     bob.left(360/sides+1)
     bob.width(times*sides/200)
