import turtle as myTurtle
myTurtle.colormode(255)

t = myTurtle.Pen()
t.pensize(2)
t.shape("classic")
t.speed(0)
t.goto(0,0)
r=255
g=0
b=0
for i in range(1275):
    t.color(r,g,b)
    t.forward(100)
    t.goto(0,0)
    t.right(0.2823529411764706)
    if r==255 and b==0 and g!=255:
        g+=1
    elif g==255 and b==0 and r>0:
        r-=1
    elif r==0 and g==255 and b<255:
        b+=1
    elif b==255 and r==0 and g>0:
        g-=1
    elif g==0 and b==255 and r<255:
        r+=1

myTurtle.exitonclick()