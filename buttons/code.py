import board
import keypad

pad = keypad.ShiftRegisterKeys( 
        clock=board.BUTTON_CLOCK, 
        data=board.BUTTON_OUT, 
        latch=board.BUTTON_LATCH, 
        key_count=8, 
        value_when_pressed=True,
        )

while True:
    event = pad.events.get()
    if event is not None:  
        key = event.key_number
        print(f'{key=}, ', end='')
        if event.pressed:
            print('pressed')
        if event.released:
            print('released')



