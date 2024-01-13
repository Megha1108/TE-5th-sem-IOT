import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.OUT)

while True:
    var=GPIO.input(3)
    print(var)
    
    if (var==1):
        GPIO.output(5,True)
    else:
        GPIO.output(5,False)
        
