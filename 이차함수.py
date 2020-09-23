import turtle

x=0
def math (x):
    for x in range(0,100,1):
        y=x**2+1
    
        
    
        turtle.goto(x,0.01*y)
        
        
        if 0.01*y>=100:
            
            break



turtle.shape("turtle")

turtle.goto(100,0)
turtle.goto(0,0)
turtle.goto(0,100)
turtle.goto(0,0)
math(x)
    

turtle.done()