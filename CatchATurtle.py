#imports
import turtle as trtl
import random as r

#initialize turtle objects
t = trtl.Turtle()
sct = trtl.Turtle()
tmr = trtl.Turtle()
score_writer = trtl.Turtle()

#set turtle speeds
t.speed(0)
sct.speed(0)
tmr.speed(0)
score_writer.speed(0)

#set turtle appearance
t.shape("turtle")
t.shapesize(2)
t.fillcolor("pink")
colors = ["plum", "medium aquamarine", "light yellow", "light slate gray", "coral", "light coral"]
i=0

#initialize score/timer variables
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False

#game functions
def countdown():
    global timer, timer_up
    tmr.clear()
    if timer <= 0:
        tmr.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        tmr.write(f"Timer: {timer}", font=font_setup)
        timer -= 1
        tmr.getscreen().ontimer(countdown, counter_interval)

def t_clicked(x,y):
    change_position()
    update_score()
    global i
    t.fillcolor(colors[i])
    i += 1
    if (i == 5):
        i = 0

def change_position():
    new_xCoor = r.randint(-350,350)
    new_yCoor = r.randint(-250,250)
    t.penup()
    t.hideturtle()
    t.goto(new_xCoor, new_yCoor)
    t.showturtle()
    t.pendown()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.penup()
    score_writer.goto(-200, 200)
    score_writer.pendown()
    score_writer.write(f"Score: {score}", font=font_setup)
    if (timer == 0):
        t.hideturtle()

#actual gameplay
countdown()
t.onclick(t_clicked)
wn = trtl.Screen()
wn.mainloop()
