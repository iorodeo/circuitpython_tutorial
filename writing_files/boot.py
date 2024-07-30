# boot.py
# ---------------------------------------------------
import time
import board
import keypad
import storage

pad = keypad.ShiftRegisterKeys( 
        clock=board.BUTTON_CLOCK, 
        data=board.BUTTON_OUT, 
        latch=board.BUTTON_LATCH, 
        key_count=8, 
        value_when_pressed=True,
        )

readonly = False
startup_dt = 3.0
t0 = time.monotonic()

print('startup window')
while time.monotonic() < t0 + startup_dt:
    event = pad.events.get()
    if event is not None: 
        if event.released and event.key_number==2:
            readonly = True
            break

print(time.time())
print('startup done')
print(f'{readonly=}')

storage.remount("/", readonly=readonly)

pad.deinit()
del pad
