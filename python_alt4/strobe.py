import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import math
import random
import time
import Defines


stepHue = 0

def stepStrobe(pixels):
    global stepHue
    for pixel in range(Defines.NUM_LEDS):
        randomValue = random.randint(0,256)
        color = fancy.CHSV(stepHue, 255, randomValue).pack()
        pixels[pixel] = color
    pixels.show()
    time.sleep(0.04)

    
    stepHue = (stepHue + 6) % 256