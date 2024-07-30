import time
import board
import analogio

VREF = 3.3
UINT16_MAX = 2**16-1

def ain_to_volt(value):
    return VREF*value/UINT16_MAX

ain = analogio.AnalogIn(board.A0)

while True:
    ival = ain.value
    volt = ain_to_volt(ain.value)
    print(f'ival: {ival}')
    print(f'volt: {volt:1.3f}')
    time.sleep(0.1)



