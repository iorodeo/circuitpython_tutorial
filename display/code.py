import time
import board
import collections
import displayio

from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from adafruit_display_shapes import circle

board.DISPLAY.brightness = 1.0

# Create color pallete
color_to_rgb = collections.OrderedDict([ 
    ('black'  , 0x000000), 
    ('white'  , 0xffffff), 
    ('red'    , 0xff0000),
    ('green'  , 0x00ff00),
    ('blue'   , 0x0000ff),
    ('gray'   , 0x999999),
    ('yellow' , 0xffff00),
    ])
color_to_index = {k:i for (i,k) in enumerate(color_to_rgb)}
num_color = len(color_to_rgb)

palette = displayio.Palette(num_color)
for i, palette_tuple in enumerate(color_to_rgb.items()):
    palette[i] = palette_tuple[1]   

# Create bitmap and tile grid for display
bitmap = displayio.Bitmap(
        board.DISPLAY.width, 
        board.DISPLAY.height, 
        num_color
        )
bitmap.fill(color_to_index['black'])
tile_grid = displayio.TileGrid(bitmap,pixel_shader=palette)

# Create header label to display count 
count = 0
font_14pt = bitmap_font.load_font(f'Hack-Bold-14.pcf')
count_label = label.Label(
        font_14pt, 
        text = f'Count: {count}',  
        color = color_to_rgb['green'], 
        scale = 1,
        anchor_point = (0.0, 0.0),
        )
count_label.anchored_position = 10, 10 

# Create a ball to move around on the display 
ball_step = 1
ball = circle.Circle(
        x0 = 0, 
        y0 = board.DISPLAY.width//2, 
        r =10, 
        fill=color_to_rgb['blue'], 
        outline=color_to_rgb['blue']
        )  

# Create display group
group = displayio.Group()
group.append(tile_grid)
group.append(count_label)
group.append(ball)
board.DISPLAY.root_group = group

while True:

    # Update count label and count
    count += 1
    count_label.text = f'Count: {count}'

    # Update ball position
    ball.x0 = ball.x0 + ball_step 
    if ball.x0 >= board.DISPLAY.width:
        ball_step = -1
    if ball.x0 <= 0:
        ball_step = 1

    time.sleep(0.01)

