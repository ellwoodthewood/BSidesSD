import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import time

NUM_LEDS = 5
pixels = neopixel.NeoPixel(board.APA102_MOSI, NUM_LEDS, auto_write=False, brightness=0.1)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
color1 = fancy.CHSV(0.08, 1.0, 1.0).pack()

hue = 0
hue2 = 128
index = 0
index2 = NUM_LEDS-1
while True:
    hue = (hue +3) % 256
    hue2 = (hue2 + 3) % 256
    index = (index + 1) % 5
    index2 = index2 -1 
    if index2 < 0:
        index2 = NUM_LEDS-1
    color = fancy.CHSV(hue,255,255).pack()
    color2 = fancy.CHSV(hue2,255,255).pack()

    for i in range(NUM_LEDS) :
        pixels[i] = (0,0,0)
    pixels[index] = color
    pixels[index2] = color2
    pixels.show()
    time.sleep(0.06)