
"""
 Ping Pong Game Using Python lang.. & turtle model

 ** Created by Abdullah EL-Yamany **

 Channal => Codezilla
 Link Video of Project => https://youtu.be/xzuguCSizWw
"""


    #Imported turtle module
import turtle as tr


wind = tr.Screen()      # Show The Window  # Intialize Screen
wind.title("Ping Pong") # Title of Window
wind.bgcolor("black")   # Background Color of Window
#wind.setup(width=600, height=400) # Size of Window
wind.tracer(0)          # Window Refresh Control  # Stops The Window From updating automatically


    # madrab1
madrab1 = tr.Turtle()    # Intializes Turtle Object
madrab1.speed(0)         # Speed of Animation
madrab1.shape("square")  # Shape of Object
madrab1.shapesize(stretch_wid=7, stretch_len=1) # Size of Object >  Stretches The Shape
madrab1.color("blue")    # Color of Shape
madrab1.penup()          # Stop The Object From drawing lines
madrab1.goto(-915, 0)    # Position of The Object

    # madrab2
madrab2 = tr.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.shapesize(stretch_wid=7, stretch_len=1)
madrab2.color("red")
madrab2.penup()
madrab2.goto(915, 0)

    # ball
ball = tr.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4


    # Score
score1 = 0
score2 = 0
score = tr.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 520)
score.write(f"Player1: {score1} | Player2: {score2}", align="center", font=("Courier", 15, "normal"))


    # Function

def madrab1_up():
    y = madrab1.ycor() # Give Me Value of y
    y += 20    # y increase be 20
    madrab1.sety(y) # Change y Value to New Value

def madrab1_down():
    y = madrab1.ycor()
    y -= 20    # y decrease be 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y) 






    # Keyboard bindings

wind.listen()    # tell the window to expect keyboard input
wind.onkeypress(madrab1_up, "w")    # Pressing W => The Function madrab1_up is Run 
wind.onkeypress(madrab1_down, "s")  #......

wind.onkeypress(madrab2_up, "Up")   #......
wind.onkeypress(madrab2_down, "Down") #.....




    # Main Game Loop 
while True:

    wind.update() # Updates The Screen Everytime The Loop Run

      # Move The Ball
    ball.setx(ball.xcor() + ball.dx) # Ball Starts at 0 and Everytime Loop Run --> +3.3
    ball.sety(ball.ycor() + ball.dy) # Ball Starts at 0 and Everytime Loop Run --> +3.3

      # Dorder Check  ,  Top border +570px, bottom border -570px, ball is 20px
    if ball.ycor() > 570 :  # if Ball is at top border
        ball.sety(570)   # y coordinate +570
        ball.dy *= -1    # Reverse Direction, making +3.3 --> -3.3

    if ball.ycor() < -570 : # if Ball is at bottom border
        ball.sety(-570)
        ball.dy *= -1

    if ball.xcor() > 960 : # if Ball is at Right border
        ball.goto(0, 0)  # Return ball to direction
        ball.dx *= -1   # Reverse the x Direction
        score1 += 1
        score.clear()
        score.write(f"Player1: {score1} | Player2: {score2}", align="center", font=("Courier", 15, "normal"))

    if ball.xcor() < -960 : # if Ball is at Left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player1: {score1} | Player2: {score2}", align="center", font=("Courier", 15, "normal"))


      # madrab and Ball
    if (ball.xcor() > 905 and ball.xcor() < 915) and (ball.ycor() < madrab2.ycor() + 65 and ball.ycor() > madrab2.ycor() - 65) :
        ball.setx(905)
        ball.dx *= -1

    if (ball.xcor() < -905 and ball.xcor() > -915) and (ball.ycor() < madrab1.ycor() + 65 and ball.ycor() > madrab1.ycor() - 65) :
        ball.setx(-905)
        ball.dx *= -1

 