import turtle as myTurtle
import random as rand

t = myTurtle.Pen()

t.pensize(5)
line = 20
for line in range(20, 201, 20):
    t.forward(line)
    t.right(90)
    t.color(rand.random(), rand.random(), rand.random())
    
myTurtle.exitonclick() 