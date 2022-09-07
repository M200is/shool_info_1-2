import turtle as myTurtle
import random as rand

myTurtle.colormode(255)

t = myTurtle.Pen()
t.shape("classic")
t.speed(0)
t.pensize(3)

r = 255
g = 0
b = 0
i = 0
while i < 500:
    t.color(r, g, b)
    t.forward(rand.randrange(1, 20))
    t.right(rand.randrange(0, i+1))
    if r == 255 and b == 0 and g != 255:
        g += 1
    elif g == 255 and b == 0 and r > 0:
        r -= 1
    elif r == 0 and g == 255 and b < 255:
        b += 1
    elif b == 255 and r == 0 and g > 0:
        g -= 1
    elif g == 0 and b == 255 and r < 255:
        r += 1
    i+=1
    
myTurtle.exitonclick()
