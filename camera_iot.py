from picamera import Picamera
from time import sleep
camera=piCamera()
camera.rotation=180
camera.start_preview()
for i in range(2):
	sleep(1)
	camera.capture('/home/pi/Desktop/img%s.jpg' %i)

camera.stop_preview()
