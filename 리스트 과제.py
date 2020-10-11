
import random
import turtle


def shape(color,side,num,x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    a=180-(((num-2)*180)//num)
    for _ in range (num+1):
        turtle.left(a)
        turtle.forward(side)
    turtle.end_fill()



slist=["yellow","white","green","blue","red","orange","purple"]




for _ in range (11):
    color=random.choice(slist)
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    side= random.randint(20,100)
    num= random.randint(3,10)

    shape(color,side,num,x,y)
turtle.done()
