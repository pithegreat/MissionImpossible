from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit


mh = Adafruit_MotorHAT(addr=0x60) #creates the PVM to control the DC motors

myLeftMotor = mh.getMotor(1) #creates the DC motor objects
myRightMotor = mh.getMotor(2)

myLeftMotor.setSpeed(255) #sets it to full speed
myRightMotor.setSpeed(255)
    
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

forward(5)
backward(5)
turnRight(5)
turnLeft(5)
turnOffMotors()



 

