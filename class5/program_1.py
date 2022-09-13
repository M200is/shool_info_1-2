import turtle

t = turtle.Turtle()
t.color("blue","yellow")
t.begin_fill()
for a in range(5):
    t.forward(100)
    t.left(144)
t.end_fill()

turtle.exitonclick()