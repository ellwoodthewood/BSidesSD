import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import time
import random
#import inspect

NUM_LEDS = 5
pixels = neopixel.NeoPixel(board.APA102_MOSI, NUM_LEDS, auto_write=False, brightness=0.1)

pixdata = [{"H":0,"S":255,"V":0,"dV":0} for i in range(NUM_LEDS)]
print(pixdata)

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
        pixdata[i]["H"] = hue
        pixdata[i]["dV"] = 1
    for j in range(NUM_LEDS):
        color = fancy.CHSV(
            pixdata[j]["H"],
            pixdata[j]["S"],
            pixdata[j]["V"],
        ).pack()
        pixels[j]=color
        pixdata[j]["V"] += fade * pixdata[j]["dV"]
        if pixdata[j]["V"] > 255:
            pixdata[j]["V"] = 255
            pixdata[j]["dV"] = -1
        if(pixdata[j]["V"] <= 0):
            pixdata[j]["V"] = 0
            pixdata[j]["dV"] = 0
    pixels.show()
    time.sleep(1/freq)
    count += 1