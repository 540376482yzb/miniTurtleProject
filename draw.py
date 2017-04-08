import turtle

window = turtle.Screen()
window.bgcolor("red")


def draw_square(dis,ang):

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color('white')
    brad.speed(100)
    count = 0
    brad.right(ang)
    while(count < 4):
        brad.forward(dis)
        brad.right(90)
        count +=1
    #print(count)


def draw_triangle(dis,ang):

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color('blue')
    angie.speed(100)
    angie.right(ang)
    count = 0
    while(count < 3):
        angie.forward(dis)
        angie.right(120)
        count +=1
    #print(count)

def draw_circle(dis,ang):

    roundy = turtle.Turtle()
    roundy.shape("turtle")
    roundy.color('yellow')
    roundy.speed(100)
    roundy.right(ang)
    roundy.circle(dis)
    
    
count = 360
while count >0:
    draw_square(100,count)
    draw_triangle(150,count)
    draw_circle(100,count)
    count -=10
    
##draw_triangle()
##draw_circle()
window.exitonclick()

