import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import time

NUM_LEDS = 5
pixels = neopixel.NeoPixel(board.APA102_MOSI, NUM_LEDS,
                           auto_write=False, brightness=1.0)

# palette for sunrise and sunset
sunset = [fancy.CRGB(0, 0, 0),
              fancy.CRGB(255, 0, 0),
              fancy.CRGB(255, 255, 0),
              fancy.CRGB(0, 0, 255),
              fancy.CRGB(0, 0, 255),
              fancy.CRGB(255, 255, 0),
              fancy.CRGB(255, 0, 0),
              fancy.CRGB(0, 0, 0)
              ]

offset = 0
while True:
    for i in range(NUM_LEDS):
        o = offset + (i*0.03)
        if o > 1:
            o = o - 1
        color = fancy.palette_lookup(sunset,o)
        color = fancy.gamma_adjust(color, brightness=1.0)
        pixels[i] = color.pack()
    offset = offset + 0.005
    if offset > 1.0:
        offset = 0
    pixels.show()
    time.sleep(0.01)
