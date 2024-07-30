import time
import board
import digitalio

dout = digitalio.DigitalInOut(board.D0)
dout.direction = digitalio.Direction.OUTPUT
dout.value = False

while True:
    dout.value = not dout.value 
    time.sleep(0.1)



