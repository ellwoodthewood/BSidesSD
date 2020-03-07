import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import time
import random

import Defines

from everyOtherAnimation import everyOtherPulse

pixels = neopixel.NeoPixel(board.APA102_MOSI, Defines.NUM_LEDS, auto_write=False, brightness=0.1)



def main():
    pixels.fill(Defines.COLOR_CLEAR)
    pixels.show()
    ledSelects = 0
    while True:
    
    
        randomHue = random.randint(0,255)
        everyOtherPulse(pixels, randomHue, ledSelects)
        ledSelects = (ledSelects + 1) % 2
    
        '''
        Original LED pattern

        for i in range(256):
            color = fancy.CHSV(40,255,i).pack()
            pixels.fill(color)
            pixels.show()
            time.sleep(0.01)
        '''

main()
