from time import sleep # import sleep()from time module
from sense_hat import SenseHat
sense = SenseHat()
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
while 1 :	
	sense.set_pixels(img_1)
	sleep(1)
	sense.set_pixels(img_2)
	sleep(1)
	sense.set_pixels(img_3)
	sleep(1)