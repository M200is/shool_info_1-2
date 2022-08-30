from ctypes.wintypes import RGB
import turtle as myTurtle

t=myTurtle.Pen()
myTurtle.colormode()

t.shape("triangle")

t.forward(50)
t.left(90)
t.color("#59ddf7")
t.forward(40)
t.pendown()
t.left(20)
t.forward(100)
t.begin_fill()
t.circle(100)
t.end_fill()
myTurtle.exitonclick()