import turtle

turtle.bgcolor("Yellow")
turtle.pencolor('Blue')
turtle.title('IST 140')
turtle.write("IST",font = ("Arial",14))
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.right(45)
turtle.forward(70)
turtle.right(90)
turtle.forward(70)

turtle.circle(60, steps=6)

turtle.penup()
turtle.forward(200)
turtle.pendown()
turtle.circle(70, steps=9)

turtle.right(130)
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.circle(100, steps=12)

turtle.right(90)
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.circle(100, steps=12)
