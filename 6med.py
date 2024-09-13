from turtle import *
tracer(0)
down()
lt(180)
m = 20
for _ in range(2):
    fd(10*m)
    rt(90)
    fd(17*m)
    rt(90)
up()
bk(7*m)
lt(90)
fd(6*m)
rt(90)
down()
for _ in range(2):
    fd(15*m)
    rt(90)
    fd(9*m)
    rt(90)
up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*m,y*m)
        dot(3, 'red')
update()
