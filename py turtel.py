import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Drawing Pi Symbol")

# Create a turtle
pi_turtle = turtle.Turtle()
pi_turtle.color("green")
pi_turtle.pensize(5)

# Draw the Pi symbol
pi_turtle.penup()
pi_turtle.goto(-50, 0)
pi_turtle.pendown()
pi_turtle.left(90)
pi_turtle.forward(100)
pi_turtle.right(90)
pi_turtle.forward(50)
pi_turtle.right(90)
pi_turtle.forward(100)
pi_turtle.penup()
pi_turtle.goto(-50, 50)
pi_turtle.pendown()
pi_turtle.forward(50)
pi_turtle.penup()
pi_turtle.goto(0, 0)
pi_turtle.pendown()
pi_turtle.circle(25, 180)

# Add some finishing touches for realism
pi_turtle.penup()
pi_turtle.goto(-50,0)
pi_turtle.pendown()
pi_turtle.circle(25, -180)

# Hide the turtle and display the window
pi_turtle.hideturtle()
turtle.done()
