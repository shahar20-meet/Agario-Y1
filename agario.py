import turtle
import time
import random
import math
from ball import Ball
turtle.colormode(255)

#turtle = turtle()
#screen = Screen()
#screen.onscreenclick(turtle.goto)
#turtle.getscreen()._root.mainloop()

global score
score = 0
turtle.tracer(0)
turtle.hideturtle()
running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height  = turtle.getcanvas().winfo_height()/2 

lines = turtle.clone()

lines.penup()
lines.hideturtle()
lines.goto(0, 300)
lines.pendown()
lines.pencolor("red")
lines.write("BOAZ", align='center', font = ("Impact",30,"normal"))
lines.penup()
lines.goto(0, 450)
lines.pendown()
lines.goto(400, 450)
lines.goto(400, -450)
lines.goto(-400, -450)
lines.goto(-400, 450)
lines.goto(0, 450)
lines.penup()
game_over=turtle.clone()
game_over.hideturtle()
game_over.color("red")


#turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=700
SIZE_Y=400
turtle.setup(1000, 1000) #Curious? It's the turtle window  
                             #size. 
turtle.penup()
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)
my_ball = Ball(100,35,21,23,50,random_color())
number_of_balls = 7
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -2
maximum_ball_dx = 2
minimum_ball_dy = -2
maximum_ball_dy = 2
BALLS = []

for i in range(number_of_balls):
    x = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
    y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
    dx = random.randint(minimum_ball_dx , maximum_ball_dx)
    dy = random.randint(minimum_ball_dy , maximum_ball_dy)
    radius = random.randint (minimum_ball_radius , maximum_ball_radius)
    color = random_color()
    Ball1 = Ball(x,y,dy,dx,radius,color)
    BALLS.append(Ball1)
def move_all_balls():
    for ball in BALLS:
        ball.move(screen_width,screen_height)

def check_collision(ball_a,ball_b):
    if ball_a == ball_b:
        return False 
    x1=ball_a.pos()[0]
    x2=ball_b.pos()[0]
    y1=ball_a.pos()[1]
    y2=ball_b.pos()[1]
    if (ball_a.r + ball_b.r) >= math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)):
        return(True)
    else:
        return(False)

#check_collision(ball_a,ball_b)
turtle.update()
t = turtle.clone()
def check_all_balls_collisions():
    global running
    global score
    all_balls=[]
    all_balls.append(my_ball)
    for ball in BALLS:
        all_balls.append(ball)
    for ball_a in all_balls:
        for ball_b in all_balls:
            if check_collision(ball_a,ball_b):
                r1 = ball_a.r
                r2 = ball_b.r
                x = random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
                y = random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
                dx = random.randint(minimum_ball_dx , maximum_ball_dx)
                dy = random.randint(minimum_ball_dy , maximum_ball_dy)
                radius = random.randint (minimum_ball_radius , maximum_ball_radius)
                color = random_color()
                if r1 > r2:
                    ball_b.new_ball(x,y,dx,dy,radius,color)
                    ball_a.r += 2
                    ball_a.shapesize(ball_a.r/10)
                    if my_ball == ball_b:
                        print("end")
                        t.goto(0,0)
                        t.write('GAME OVER',align="center",font =  ('fantasy', 70, 'normal'))
                        quit()
                    if my_ball == ball_a:
                        score += 1
                        
                else:
                    ball_a.new_ball(x,y,dx,dy,radius,color)
                    ball_b.r += 2
                    ball_b.shapesize(ball_b.r/10)
                    if my_ball == ball_a:
                        print("end")
                        t.goto(0,0)
                        t.write('GAME OVER',align="center",font =  ('fantasy', 70, 'normal'))
                        quit()
                    if my_ball == ball_a:
                        score += 1
def movearound():
    my_ball.goto(turtle.getcanvas().winfo_pointerx() - screen_width*2,screen_height - turtle.getcanvas().winfo_pointery()) 

running = True
while running is True:
    screen_width = turtle.getcanvas().winfo_width()/2
    screen_height = turtle.getcanvas().winfo_height()/2

    #turtle.clone = border
    #border.stamp(-screenwidth + 30,-screenheight + 20)
    movearound()
    move_all_balls()
    check_all_balls_collisions()
    t.clear()
    t.goto(-400,300)
    t.write("Score: " + str(score),font =  ('ariel', 20, 'normal'))
    #if my_ball >= turtle.getcanvas().winfo_width()/2():
     #   t.write('YOU WON',align="center",font =  ('fantasy', 70, 'normal'))
                        

    time.sleep(1/120)
    turtle.update()

turtle.update()
turtle.mainloop()
