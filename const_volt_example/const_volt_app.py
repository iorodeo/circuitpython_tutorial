import time
from button_monitor import ButtonMonitor
from potentiostat import Potentiostat
from const_volt_display import ConstVoltDisplay

class ConstVoltApp:

    DT = 0.01
    START_BUTTON = 2
    STOP_BUTTON = 3

    def __init__(self):
        self.running = False
        self.t_start = 0.0
        self.setpt_voltage = 0.9
        self.pstat = Potentiostat('100uA')
        self.pstat.connected = False
        self.button_monitor = ButtonMonitor()
        self.display = ConstVoltDisplay()
        self.display.set_running(False)
        self.display.set_time(0.0)
        self.display.set_volt(None)
        self.display.set_curr(0.0)

    def handle_button_press(self):
        button = self.button_monitor.events
        if button is None:
            return
        if button == self.START_BUTTON:
            self.pstat.connected = True
            self.pstat.voltage = self.setpt_voltage
            self.t_start = time.monotonic()
            self.running = True
            self.display.set_running(True)
        if button == self.STOP_BUTTON:
            self.pstat.connected = False
            self.pstat.voltage = 0.0
            self.running = False
            self.display.set_running(False)
            self.display.set_volt(None)
            self.display.set_curr(0.0)

    def run(self):
        while True:
            self.handle_button_press()
            if self.running:
                t = time.monotonic() - self.t_start
                curr_ua = convert_to_ua(self.pstat.current)
                self.display.set_time(t)
                self.display.set_volt(self.setpt_voltage)
                self.display.set_curr(curr_ua)
            time.sleep(self.DT)


# ---------------------------------------------------------------

def convert_to_ua(val):
    return val*1.0e6



