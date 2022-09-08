import turtle as myTurtle

t= myTurtle.Pen()

line = 20
for i in range(0, 10):
    t.forward(line)
    t.right(90)
    line += 20
    
myTurtle.exitonclick()