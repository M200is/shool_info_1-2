a=10
b=20
print(a+b)

def multi():
    global c
    c=a*b
    print(c)

def plus():
    print(c+a)

multi()
plus()