import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(7,GPIO.IN)

while True:
	var =GPIO.input(7)
	print(var)
	
	if(var==0):
		GPIO.output(26,False)
	else:
		GPIO.output(26,True)
