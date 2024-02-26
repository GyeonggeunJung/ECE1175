from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = (255, 0, 0)
o = (255, 125, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
n = (0, 125, 125)
p = (255, 0, 255)
w = (255, 255, 255)
colors = [r, o, y, g, b, n, p, w]

while 1 :
	for i in range(0, 8) :
		for j in range(0, i+1):
			sense.set_pixel(j, i-j, colors[i])
		sleep(0.5)
		sense.clear()
	for i in range(8, 15) :
		for j in range(0, i):
			if i-j < 8 :
				if j <8 :
					sense.set_pixel(j, i-j, colors[14-i])
		sleep(0.5)
		sense.clear()
