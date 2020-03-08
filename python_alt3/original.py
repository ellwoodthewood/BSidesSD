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

while True:
    for i in range(256):
        color = fancy.CHSV(i,255,255).pack()
        pixels.fill(color)
        pixels.show()
        time.sleep(0.01)