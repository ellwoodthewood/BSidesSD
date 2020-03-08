import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import time
import random
#import inspect

NUM_LEDS = 5
pixels = neopixel.NeoPixel(board.APA102_MOSI, NUM_LEDS, auto_write=False, brightness=0.1)

hues = [0 for i in range(5)]
brights = [0 for i in range(5)]
dirs = [0 for i in range(5)]
print(brights)

i = 0
dir = 1
count = 0
ratio = 10
freq = 2000
fade = 28
while True:
    if count % ratio == 0:
        i = i + dir
        if(i >= NUM_LEDS):
            i = NUM_LEDS - 2
            dir = -dir
        if(i < 0):
            i = 1
            dir = -dir
        hue = 255
        hues[i] = hue
        dirs[i] = 1
    for j in range(NUM_LEDS):
        color = fancy.CHSV(hues[j], 255, brights[j]).pack()
        pixels[j]=color
        brights[j] += fade * dirs[j]
        if brights[j] > 255:
            brights[j] = 255
            dirs[j] = -1
        if(brights[j] <= 0):
            brights[j] = 0
            dirs[j] = 0
    pixels.show()
    time.sleep(1/freq)
    count += 1