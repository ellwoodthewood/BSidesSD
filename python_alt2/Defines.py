import adafruit_fancyled.adafruit_fancyled as fancy

#Color Defines (Hue ranges)
RED = (0, 60)
YELLOW = (61, 120)
GREEN = (121, 180)
CYAN = (181, 240)
BLUE = (241, 300)
PURPLE = (301,360)
color1 = fancy.CHSV(0.08, 1.0, 1.0).pack()
COLOR_CLEAR = fancy.CHSV(0,0,0).pack()

#Num LEDS
NUM_LEDS = 5