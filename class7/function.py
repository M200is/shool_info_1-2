import turtle as myTurtle

t=myTurtle.Turtle()

def f(c):
    t.forward(100)
    t.left(c)
    
def h():
    for i in range(6):
        f(60)

def g(a):
    h()
    t.forward(100)
    t.right(a)

for i in range(6):
    g(60)
    
myTurtle.exitonclick()