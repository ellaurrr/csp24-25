#imports
import turtle as trtl
t = trtl.Turtle()
t.speed(0)

c = trtl.Turtle()
c.speed(0)
c.penup()
c.pencolor("red")
c.goto(-200, 200)
c.fillcolor("red")

def drawBlackBackground():
    t.penup()
    t.pencolor("black")
    t.goto(-200,-200)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.left(90)
        t.forward(400)
        t.left(90)
    t.end_fill()
def drawColumns(num):
    squareLength = 400/(num)
    START_X, START_Y = -200, 200
    for row in range(num):
        if (row%2 == 0):
            c.goto(START_X, START_Y - (row * squareLength))
        elif (row%2 == 1):
            c.goto(START_X + squareLength, START_Y - (row * squareLength))

        sq = int(num/2)
        for col in range(sq):
            drawSquare(squareLength)
            c.forward(2*squareLength)

def drawSquare(size):
    c.pendown()
    c.begin_fill()
    for side in range(4):
        c.forward(size)
        c.right(90)
    c.end_fill()
    c.penup()

#main
drawBlackBackground()

dimensions = int(input("what dimensions for the checkerboard do you want? ex: 4 gives you 4x4 "))
drawColumns(dimensions)

wn = trtl.Screen()
wn.mainloop()