from turtle import *
tracer(0)
down()
screensize(1920,1080)
m = 20
goto(-3*m,1*m)
for _ in range(5):
    fd(5*m)
    rt(45)
rt(30)
fd(16*m)
up()
for x in range(-15,20):
    for y in range(0,20):
        goto(x*m,y*m)
        dot(5, 'red')
update()
