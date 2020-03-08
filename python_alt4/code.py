import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import time
import random

from digitalio import DigitalInOut, Direction, Pull

import Defines

from everyOtherAnimation import everyOtherPulse
import rainbow
import strobe

pixels = neopixel.NeoPixel(board.APA102_MOSI, Defines.NUM_LEDS, auto_write=False, brightness=0.1)



def main():
    pixels.fill(Defines.COLOR_CLEAR)
    pixels.show()
    ledSelects = 0

    #Pin 2 pulled up to 3.3v will enable "every other pulse"
    pickAnimation1 = DigitalInOut(board.D2)
    pickAnimation1.direction = Direction.INPUT
    pickAnimation1.pull = Pull.DOWN

    #Pin 3 pulled up to 3.3v will enable "strobe" animation
    pickAnimation2 = DigitalInOut(board.D3)
    pickAnimation2.direction = Direction.INPUT
    pickAnimation2.pull = Pull.DOWN

    #Pin 4 pulled up to 3.3v will enable "default" animation
    pickAnimation3 = DigitalInOut(board.D4)
    pickAnimation3.direction = Direction.INPUT
    pickAnimation3.pull = Pull.DOWN

    while True:
    
        randomHue = random.randint(0,255)

        #every other LED for PIN2 pulled up to 3.3v
        if pickAnimation1.value:
            everyOtherPulse(pixels, randomHue, ledSelects)
            ledSelects = (ledSelects + 1) % 2
        #Strobe animation for pin 3 pulled up to 3.3v
        elif pickAnimation2.value:
            strobe.stepStrobe(pixels)
        #Original LED pattern
        elif pickAnimation3.value:
            for i in range(256):
                color = fancy.CHSV(i,255,255).pack()
                pixels.fill(color)
                pixels.show()
                time.sleep(0.01)
        else:
            rainbow.stepRainbow(pixels)

main()
