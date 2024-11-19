import turtle as trtl
import math
import random #was missing earlier, which resulted in errors

s = trtl.Screen()
t = trtl.Turtle()
t.speed(0)

def sand():
    t.penup()
    t.pencolor("blanchedalmond")
    t.goto(-200,-200)
    t.pendown()
    t.fillcolor("blanchedalmond")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

def sky():
    t.penup()
    t.pencolor("lightskyblue")
    t.goto(-200,0)
    t.pendown()
    t.fillcolor("lightskyblue")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.end_fill()

def water():
    t.penup()
    t.pencolor("steelblue")
    t.goto(-200,-100)
    t.pendown()
    t.fillcolor("steelblue")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

def sun():
    t.pencolor("black")
    t.penup()
    t.goto(115,115)
    t.fillcolor("gold")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.penup()

def fish():
    t.pencolor("indianred")
    t.penup()
    t.goto(30,-70)
    t.pendown()
    t.fillcolor("indianred")
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(60,-70)
    t.pendown()
    t.begin_fill()
    t.circle(20,360,3)
    t.end_fill()
    t.penup()
    t.goto(25,-50)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.penup()
    t.goto(225, 0)

def overlaps(newX, newY, firstP, minDistance):
    for x, y in firstP:
        if math.sqrt((newX - x)**2 + (newY - y)**2) < minDistance:
            return True
    return False

#makes the background
sand()
sky()
water()
sun()
fish()

# colors and shapes
shell_colors1 = ["pink", "thistle", "lightyellow", "white", "coral", "lightcoral"]
shell_colors2 = ["pink", "thistle", "lightyellow", "white", "coral", "lightcoral"]
shell_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

#sets up positions to avoid overlapping
shell_positions = []
minDistance = 50

# turtle objects (do i need this?)
shell_turtles = []


# making the seashells
for s in shell_shapes:
    #first set of turtles
    while True:
        newX = random.randint(-180,190)
        newY = random.randint(-180, -100)
        if not overlaps(newX, newY, shell_positions, minDistance):
            break
    ss1 = trtl.Turtle(shape=s)
    shell_turtles.append(ss1)
    ss1.penup()
    ss1.fillcolor(shell_colors1.pop())
    ss1.goto(random.randint(-180,190), random.randint(-180, -100))
    ss1.setheading(0)
    shell_positions.append((newX, newY))


    #second set of turtles
    while True:
        newX = random.randint(-180, 190)
        newY = random.randint(-190, -100)
        if not overlaps(newX, newY, shell_positions, minDistance):
            break
    ss2 = trtl.Turtle(shape=s)
    shell_turtles.append(ss2)
    ss2.penup()
    ss2.fillcolor(shell_colors2.pop())
    ss2.goto(random.randint(-180,190), random.randint(-180, -100))
    ss2.setheading(270)
    shell_positions.append((newX, newY))

trtl.done()
