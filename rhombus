import turtle

window = turtle.Screen()
window.bgcolor("blue")

#draw pedals
def draw_rhombus(width,angS,ang):
    rhom = turtle.Turtle()
    rhom.shape("turtle")
    rhom.speed(1000)
    rhom.color("yellow")
    rhom.penup()
    rhom.goto(-300,300)
    rhom.pendown()
    rhom.left(ang)
    angL = 180-angS
    rhom.forward(width)
    rhom.left(angS)
    rhom.forward(width)
    rhom.left(angL)
    rhom.forward(width)
    rhom.left(angS)
    rhom.forward(width)

for i in range(1,37):
    draw_rhombus(100,30,i*10)

#draw stems and leaf
leaf = turtle.Turtle()
leaf.shape("turtle")
leaf.color("green")
leaf.speed(200)
leaf.penup()
leaf.goto(-300,300)
leaf.pendown()
leaf.right(90)
leaf.forward(500)
leaf.setheading(30)
leaf.forward(300)
leaf.goto(-300,-200)
leaf.setheading(150)
leaf.forward(300)


window.exitonclick()

