import turtle
import math
import random
# Acceptable methods...forward, left, right, backward, pos
alex = turtle.Turtle()
target = random.randint(-300, 300),random.randint(-300, 300)
alex.penup()

def heading_calc(dx, deg):
    if dx < 0:
        return 180 + deg
    if dx > 0:
        return 360 + deg


alex.goto(target)
alex.stamp()  #put a stamp at the randomly chosen target

delta = 20  #distance travelled between testing of location

alex.left(random.randint(0,360))  #randomly choose direction
alex.penup()
alex.goto(random.randint(-300, 300),random.randint(-300, 300))  #random starting location
alex.pendown()
start = alex.pos()
first = True

def turn_calc(end, target): #figures out how much to turn
    want_dx = target[0] - end[0]
    want_dy = target[1] - end[1]
    if want_dx == 0: #if 90 or 270 degrees
        want_tan = math.pi/2
    else:
        want_tan = want_dy/want_dx
    want_rad = math.atan(want_tan)
    want_deg = (180*want_rad)/(math.pi) #to degrees
    want_deg = heading_calc(want_dx, want_deg) #angle want to go
    alex.forward(5)
    angle_dx = alex.pos()[0] - end[0]
    angle_dy = alex.pos()[1] - end[1]
    if angle_dx == 0:
        tan_angle = math.pi/2 #if 90 or 270 degrees
    else:
        tan_angle = angle_dy/angle_dx
    curr_angle = (180*math.atan(tan_angle))/(math.pi) #angle currently at
    curr_angle = heading_calc(angle_dx, curr_angle)
    return want_deg - curr_angle #angle to turn

alex.left(turn_calc(start, target))

while not(target[0] - delta <= start[0] <= target[0] + delta) or not(target[1] - delta <= start[1] <= target[1] + delta):
   alex.forward(delta)
   end = alex.pos()
   print(start, end)
   alex.left(turn_calc(end,target)) #corrects angle every iteration in case of drift
   start = alex.pos()

turtle.exitonclick()
