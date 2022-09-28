import turtle as myTurtle

t=myTurtle.Pen()

def fc(r,g,b,ra):
    t.color(r,g,b)
    t.begin_fill()
    t.circle(ra)
    t.end_fill()

def fw(r):
    t.up()
    t.forward(r)
    t.down()
    
fc(0.6,1,0.4,30)
fw(100)
fc(1,0.3,1,50)
fw(150)
fc(0,1,1,70)

myTurtle.exitonclick()