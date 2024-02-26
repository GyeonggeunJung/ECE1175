from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
d = ["up", "down", "right", "left", "middle"]

r = (255, 0, 0)
b = (0, 0, 255)
g = (0, 255, 0)
n = (0, 0, 0)
w = (255, 255, 255)

img_1 = [ 
n, n, n, n, n, n, n, n,
r, n, n, n, n, n, n, n,
n, r, n, n, r, n, r, n,
n, r, r, r, r, r, r, n,
n, b, b, b, b, b, b, b,
n, b, b, b, b, b, b, n,
n, n, b, n, n, b, n, n,
n, n, n, n, n, n, n, n
]


img_2 = [ 
r, n, n, n, n, n, n, n,
n, r, n, n, r, n, r, n,
n, r, r, r, r, r, r, n,
n, b, b, b, b, b, b, b,
n, b, b, b, b, b, b, n,
n, n, b, n, n, b, n, n,
n, n, n, n, n, n, n, n,
n, n, n, n, n, n, n, n
]


img_3 = [ 
n, n, n, n, n, n, n, n, 
n, r, n, n, n, n, n, n,
n, n, r, n, n, r, n, r,
n, n, r, r, r, r, r, r,
n, n, b, b, b, b, b, b,
n, n, b, b, b, b, b, b,
n, n, n, b, n, n, b, n,
n, n, n, n, n, n, n, n
]
def Task_1() :	
	sense.set_pixels(img_1)
	sleep(1)
	sense.set_pixels(img_2)
	sleep(1)
	sense.set_pixels(img_3)
	sleep(1)
	
while True:
	for event in sense.stick.get_events():
		print(event.direction, event.action)
		direction = event.direction
		if direction == d[0] :
			sense.show_letter("U", r)
			sleep(1)
			sense.clear()
		if direction == d[1] :
			sense.show_letter("D", b)
			sleep(1)
			sense.clear()
		if direction == d[2] :
			Task_1()
			sleep(1)
			sense.clear()
		if direction == d[3] :
			sense.show_letter("L", g)
			sleep(1)
			sense.clear()
		if direction == d[4] :
			sense.show_letter("M", w)
			sleep(1)		
			sense.clear()
