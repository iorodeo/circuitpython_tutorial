import math
import time
from potentiostat import Potentiostat

# Output parameters for cosine
dt = 0.01
period = 5.0
amplitude = 0.5

# Create potentiosat object and connect electrode
pstat = Potentiostat(current_range='100uA')
pstat.connected = True 

t0 = time.monotonic()
while True:

    # Set output voltage 
    t = time.monotonic() - t0
    vout = amplitude*math.cos(2.0*math.pi*t/period)
    pstat.voltage = vout

    # Read current and convert to uA
    curr = pstat.current
    curr_ua = curr*1.0e6

    # Display results
    print(f'{vout:1.2f}V, {curr_ua:1.2f}uA')
    time.sleep(dt)
    



