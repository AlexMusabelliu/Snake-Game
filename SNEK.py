#Snake
#Implement Death
from turtle import Screen, Turtle
from random import randint
from time import sleep

def Start():
    global t, creater, omega, score, direction, s, bodyParts, canMove, wait, point, started, SCORE_TIMER, DEAD
    t = Turtle('circle')
    t.pu()
    t.ht()
    t.shapesize(0.5)
    
    creater = Turtle('circle')
    creater.pu()
    creater.ht()
    creater.color('yellow')
    omega = False
    started = False
    
    s = Screen()
    s.tracer(False)
    s.screensize(500, 500)
    
    score = Turtle()
    score.ht()
    score.pu()
    score.goto(-325, 350)
    score.color('green')
    
    direction = (10, 0)
    point = None
    wait = True
    canMove = True
    DEAD = 0
    
    SCORE_TIMER = 50
    bodyParts = []
    started = True
    score.clearstamps()
   # s.clearscreen()
    for x in range(3):
        t.goto(x * 10, 0)
        bodyParts.append((t.pos(), t.stamp()))
        
    #bodyParts.reverse()




def Move():
    global bodyParts, wait, omega
    first = True
    used = []

    nu = []
    if canMove:
        for x in bodyParts:
            if direction != (0, -10):
                s.onkey(Up, "Up")
            else:
                s.onkey(None, "Up")
            if direction != (0, 10):
                s.onkey(Down, "Down")
            else:
                s.onkey(None, "Down")
            if direction != (10, 0):
                s.onkey(Left, "Left")
            else:
                s.onkey(None, "Left")
            if direction != (-10, 0):
                s.onkey(Right, "Right")
            else:
                s.onkey(None, "Right")
                
            if first:
                #(x[0][0] + direction[0])
                first = False
                t.clearstamp(x[1])
                if direction[1] == 0:
                    if x[0][0] + direction[0] > 400:
                        t.goto(-400, x[0][1] + direction[1])
                    elif x[0][0] + direction[0] < -400:
                        t.goto(400, x[0][1] + direction[1])   
                    else:
                        t.goto(x[0][0] + direction[0], x[0][1] + direction[1])
                if direction[0] == 0:
                    if x[0][1] + direction[1] > 400:
                        t.goto(x[0][0] + direction[0], -400)  
                    elif x[0][1] + direction[1] < -400:
                        t.goto(x[0][0] + direction[0], 400)
                    else:   
                        t.goto(x[0][0] + direction[0], x[0][1] + direction[1])
    
                nu.append((t.pos(), t.stamp()))
            else:
                t.goto(bodyParts[bodyParts.index(x) - 1][0])
                t.clearstamp(x[1])
                nu.append((t.pos(), t.stamp()))
    
        bodyParts = nu
        #print(t.distance(bodyParts[2][0]))
        s.update()
        if omega == True:
            for x in bodyParts:
                t.goto(x[0])
                if t.pos() in used:
                    die()
                used.append(x[0])
        else:
            omega = True
        s.ontimer(Move, 100)

def Score():
    global started, DEAD
    if DEAD:
        score.clear()
    score.clear()
    numScore = len(bodyParts) - 3 
    if started and not DEAD: 
        score.write("Score: " + str(numScore), False, align = 'right', font = ("Arial", 25, 'bold'))
    s.ontimer(Score, SCORE_TIMER)
  
def Up():
    global direction
    s.onkey(None, "Up")
    direction = (0, 10)
    #print(direction)
    s.onkey(Up, "Up") 

def Down():
    global direction
    s.onkey(None, "Down")
    direction = (0, -10)
    #print(direction)
    s.onkey(Down, "Down") 
    
def Left():
    global direction
    s.onkey(None, "Left")
    direction = (-10, 0)
    #print(direction)
    s.onkey(Left, "Left") 
    
def Right():
    global direction
    s.onkey(None, "Right")
    direction = (10, 0)
    #print(direction)
    s.onkey(Right, "Right")    
    
def Create():
    global point
    if not point:
        random = randint(0, 300)
        random2 = randint(0, 300)
        creater.goto(random, random2)
        point = creater.stamp()
        
    if creater.distance(bodyParts[0][0]) < 20:
        bodyParts.append(((t.xcor() - 10, t.ycor()), t.stamp()))
        creater.clearstamp(point)
        creater.goto(randint(0, 200), randint(0, 200))
        point = None
        
    s.ontimer(Create, 50)
    
def die():
    global canMove, SCORE_TIMER, DEAD
    s.reset()
    s.clearscreen()
    canMove = False
    #SCORE_TIMER = 100000
    DEAD = 1
    s.ontimer(Score, SCORE_TIMER)
    t.write("YOU DIED")
    sleep(2)
    s.clearscreen()
    Start()
    DEAD = 0
   # s.clearscreen()
    
    
Start() 
s.listen()
Score()
s.ontimer(Create, 50)
Move()
s.mainloop()