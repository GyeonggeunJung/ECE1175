from sense_hat import SenseHat
from time import sleep
r = (255, 0, 0)
o = (255, 125, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
n = (0, 125, 125)
p = (255, 0, 255)
w = (255, 255, 255)
colors = [r, o, y, g, b, n, p, w]

def x_plus() :
	for j in range(0, 8) :
		for i in range(0, 8) :
			sense.set_pixel(j, i, colors[j])
		sleep(0.5)
		sense.clear()
			
def x_minus() :
	for j in reversed(range(0, 8)) :
		for i in range(0, 8) :
			sense.set_pixel(j, i, colors[7-j])
		sleep(0.5)
		sense.clear()
def y_plus() :
	for j in range(0, 8) :
		for i in range(0, 8) :
			sense.set_pixel(i, j, colors[j])
		sleep(0.5)
		sense.clear()
				
def y_minus():
    for j in reversed(range(8)):
        for i in range(8):
            sense.set_pixel(i, j, colors[7-j])
        sleep(0.5)
        sense.clear()

sense = SenseHat()

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']
    # Determine the direction and display the pattern
	if x > 0.5:
		x_plus()
	elif x < -0.5:
		x_minus()
	elif y > 0.5:
		y_plus()
	elif y < -0.5:
		y_minus()
	elif z > 0.5:
		sense.show_message("Stable", text_colour=w)
	else:
		print("Pi is fliped.")
    
	sleep(1) 
