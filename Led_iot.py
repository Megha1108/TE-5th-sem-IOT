import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

while True:
    GPIO.output(3,True)
    time.sleep(0.5)
    GPIO.output(3,False)
    
    GPIO.output(5,True)
    time.sleep(0.5)
    GPIO.output(5,False)
    
    GPIO.output(7,True)
    time.sleep(0.5)
    GPIO.output(7,False)
    
    GPIO.output(11,True)
    time.sleep(0.5)
    GPIO.output(11,False)

GPIO.cleanup()
