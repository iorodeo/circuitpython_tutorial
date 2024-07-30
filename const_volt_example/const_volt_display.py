import time
import board
import displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from adafruit_display_shapes import circle
from colors import color_to_rgb
from colors import color_to_index
from colors import num_color

class ConstVoltDisplay:

    RUNNING_STR = 'running'
    STOPPED_STR = 'stopped'
    TIME_STR = 't'
    VOLT_STR = 'V'
    CURR_STR = 'I'

    def __init__(self):
        board.DISPLAY.brightness = 1.0
        font_14pt = bitmap_font.load_font(f'Hack-Bold-14.pcf')
        
        self.palette = displayio.Palette(num_color)
        for i, self.palette_tuple in enumerate(color_to_rgb.items()):
            self.palette[i] = self.palette_tuple[1]   
        
        # Create self.bitmap and tile grid for display
        self.bitmap = displayio.Bitmap(
                board.DISPLAY.width, 
                board.DISPLAY.height, 
                num_color
                )
        self.bitmap.fill(color_to_index['black'])
        self.tile_grid = displayio.TileGrid(self.bitmap,pixel_shader=self.palette)



        # Create runnning label 
        xpos = 1
        ypos = 0
        ystep = 30 
        self.running_label = label.Label(
                font_14pt, 
                text = self.STOPPED_STR,  
                color = color_to_rgb['green'], 
                scale = 1,
                anchor_point = (0.0, 0.0),
                )
        self.running_label.anchored_position = xpos, ypos 
        ypos += ystep

        # Create time label 
        self.time_label = label.Label(
                font_14pt, 
                text = f'{self.TIME_STR} 0.0',  
                color = color_to_rgb['green'], 
                scale = 1,
                anchor_point = (0.0, 0.0),
                )
        self.time_label.anchored_position = xpos, ypos 
        ypos += ystep

        # Create voltage label 
        self.volt_label = label.Label(
                font_14pt, 
                text = f'{self.VOLT_STR} off',  
                color = color_to_rgb['green'], 
                scale = 1,
                anchor_point = (0.0, 0.0),
                )
        self.volt_label.anchored_position = xpos, ypos 
        ypos += ystep

        # Create voltage label 
        self.curr_label = label.Label(
                font_14pt, 
                text = f'{self.CURR_STR}',  
                color = color_to_rgb['green'], 
                scale = 1,
                anchor_point = (0.0, 0.0),
                )
        self.curr_label.anchored_position = xpos, ypos 
        ypos += ystep
        
        # Create display group
        group = displayio.Group()
        group.append(self.tile_grid)
        group.append(self.running_label)
        group.append(self.time_label)
        group.append(self.volt_label)
        group.append(self.curr_label)
        board.DISPLAY.root_group = group

    def set_running(self, value):
        if value:
            self.running_label.text = self.RUNNING_STR 
        else:
            self.running_label.text = self.STOPPED_STR 

    def set_time(self, t):
        self.time_label.text = f'{self.TIME_STR} {t:7.2f}s'

    def set_volt(self, v):
        if v is not None:
            self.volt_label.text = f'{self.VOLT_STR} {v:7.2f}V'
        else:
            self.volt_label.text = f'{self.VOLT_STR}    none'

    def set_curr(self, v):
        self.curr_label.text = f'{self.CURR_STR} {v:7.2f}uA'


