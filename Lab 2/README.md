# Sense HAT 
## Task 1
- Show simple animation on LED matrix.
- Loop a series of static images to achieve dynamic.
  - Use set_pixel(), set_pixels(), sleep(), clear()
<p align="center"><img width="672" alt="image" src="https://github.com/GyeonggeunJung/ECE1175/assets/113646015/7954e675-93a2-4292-a830-c51f56e4a29c"></p>

## Task 2
- Different reactions to five Joystick operations.
- Display different types of sensor readings according to your joystick operations (up, down, right, left, middle).
- Detect joystick events in an endless loop.
  - Use if-elif-else to conduct different reactions.
  - Use stick.get_events()

## Task 3
- Display a moving line on LED matrix.
- The moving direction of the line should be the same as tilting directionof your board.
- Use different colors for each movement.
  - Detect tilting directions using accelerometer readings in an endless loop.
  - Create moving line animations according to the tilting directions.
  - Use get_accelerometer_raw(), set_pixel(), sleep(), clear(), etc.
 
<p align="center"><img width="672" alt="image" src="https://github.com/GyeonggeunJung/ECE1175/assets/113646015/99de1f81-e05c-4f96-8b6c-598d0dab578a"></p>

## Task 4
- Display a moving line on LED matrix.
- The line should move along the matrix diagonal.
- Change your color for each movement.
<p align="center"><img width="672" alt="image" src="https://github.com/GyeonggeunJung/ECE1175/assets/113646015/52c72c9d-de0b-4964-8013-7c61276886fd"></p>  

# Interrupt

## Task 5
- Use C to write a system-call-based interrupt on Raspberry Pi OS.
- Set a timer using setitimer(). A SIGALRM/SIGVTALRM signal will automatically be generated in each expiration of the timer.
- Use sigaction()to detect the SIGALRM/SIGVTALRM signal and execute your signal handler
- Include head files sys/time.hand signal.h
- Use the given code template to trigger an interrupt
