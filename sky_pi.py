#current version is not tested and could easily have many errors/bugs

import math

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
from urllib.request import urlopen



mh = Adafruit_MotorHAT(addr=0x60) #creates the PVM to control the DC motors

myLeftMotor = mh.getMotor(1) #creates the DC motor objects
myRightMotor = mh.getMotor(2)

myLeftMotor.setSpeed(255) #sets it to full speed
myRightMotor.setSpeed(255)

def get_pos(): #returns coords of rover
    html = str(urlopen("http://10.144.7.184/coord.txt").read()) #reads in data from website
    coords = html.split(",")
    pos = (int(coords[0][1:]), int(coords[1][:-3])) #puts it into tuple
    return pos
    
def turnOffMotors(): #shuts down motors
	myLeftMotor.run(Adafruit_MotorHAT.RELEASE)
	myRightMotor.run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)

def forward(seconds=None): #forward for number of seconds
    myLeftMotor.run(Adafruit_MotorHAT.FORWARD)
    myRightMotor.run(Adafruit_MotorHAT.FORWARD)
    if seconds is not None:
        time.sleep(seconds)
        turnOffMotors()

def backward(seconds=None): #backward for number of seconds
    myLeftMotor.run(Adafruit_MotorHAT.BACKWARD)
    myRightMotor.run(Adafruit_MotorHAT.BACKWARD)
    if seconds is not None:
        time.sleep(seconds)
        turnOffMotors()

def turnRight(seconds=None): #turn right for number of seconds
    myLeftMotor.run(Adafruit_MotorHAT.FORWARD)
    myRightMotor.run(Adafruit_MotorHAT.BACKWARD)
    if seconds is not None:
        time.sleep(seconds)
        turnOffMotors()

def turnLeft(seconds=None): #turn left for number of seconds
    myLeftMotor.run(Adafruit_MotorHAT.BACKWARD)
    myRightMotor.run(Adafruit_MotorHAT.FORWARD)
    if seconds is not None:
        time.sleep(seconds)
        turnOffMotors()

ang_time = 1 #time it takes to rotate 90 degrees CHANGE VALUE
dis_time = 1 #time it take to move 1 meter CHANGE VALUE

def angle_to_time(angle): #returns the motor turn time for given angle
    return ang_time * (angle/90)

def distance_to_time(dis):
    return dis * dis_time

target = (0,0) #where you want rover to go CHANGE VALUE
delta = 0.1 #how close to target

def heading_calc(dx, deg): #converts heading to 360 value
    if dx < 0:
        return 180 + deg
    if dx > 0:
        return 360 + deg

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

start = get_pos()
turnLeft(angle_to_time(turn_calc(start, target)))
turnOffMotors()
while not(target[0] - delta <= start[0] <= target[0] + delta) or not(target[1] - delta <= start[1] <= target[1] + delta):
   forward(distance_to_time(delta))
   turnOffMotors()
   end = get_pos()
   print(start, end)
   turnLeft(angle_to_time(turn_calc(end,target))) #corrects angle every iteration in case of drift
   turnOffMotors()
   start = get_pos()



