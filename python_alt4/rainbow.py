import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import math
import Defines

HUE_CONVERSION_FACTOR = 0.70833333

rainbowHue = 0

def stepRainbow(pixels):
    global rainbowHue
    for led in range(Defines.NUM_LEDS):
        ledHue = int( (rainbowHue + (51*led)) % 256)
        pixels[led] = fancy.CHSV(ledHue, 255, 255).pack()
    pixels.show()
    rainbowHue = (rainbowHue + 3) % 256