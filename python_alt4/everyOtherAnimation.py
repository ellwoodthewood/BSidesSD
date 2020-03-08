import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import Defines
'''
    everyOtherPuse -- Pulses every other LED in the pixel array based on the binary input of ledSelect
                      

    inputHue -- Input hue of the color to fade in and fade out.  
                This is an 8bit value representing the hue value of an HSV (Hue, Saturation, Value) color.
                Hues are represented as a gradient along a circle, so this is an 8bit representation of 360 degrees
    ledSelect -- A value 0 or 1 (Will be mod'd against 2 after input).  Indicates which LED index to start at
'''
def everyOtherPulse(pixelInput, inputHue, ledSelect, numLeds=Defines.NUM_LEDS):
    ledSelect = ledSelect % 2
    for i in range(256):
        color = fancy.CHSV(inputHue, 255, i).pack()

        for pixelId in range(ledSelect, numLeds, 2):
            pixelInput[pixelId] = color
        
        pixelInput.show()
    
    
    for i in range(255, 0, -1):
        color = fancy.CHSV(inputHue, 255, i).pack()
        
        for pixelId in range(ledSelect, numLeds, 2):
            pixelInput[pixelId] = color
        
        pixelInput.show()
    pixelInput.fill(Defines.COLOR_CLEAR)
    pixelInput.show()