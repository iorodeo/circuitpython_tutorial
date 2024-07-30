import board
import keypad

class ButtonMonitor:

    def __init__(self):
        self.pad = keypad.ShiftRegisterKeys( 
                clock=board.BUTTON_CLOCK, 
                data=board.BUTTON_OUT, 
                latch=board.BUTTON_LATCH, 
                key_count=8, 
                value_when_pressed=True,
                )

    @property
    def events(self):
        key = None
        event = self.pad.events.get()
        if event is not None:  
            if event.released:
                key = event.key_number
        return key

