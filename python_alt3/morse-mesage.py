import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import time

MESSAGE = "HTTPS LINKEDIN DOT COM SLASH IN SLASH FAITHKENT"

NUM_LEDS = 5
pixels = neopixel.NeoPixel(
  board.APA102_MOSI,
  NUM_LEDS,
  auto_write=False,
  brightness=0.1)

ON = 255
OFF = 0

DOT = 0.1
DASH = 3 * DOT
GAP = DOT
LETTER_END = 3 * DOT
WORD_END = 7 * DOT
MESSAGE_END = 20 * DOT

ALPHABET = {
    "A": [DOT, DASH],
    "B": [DASH, DOT, DOT, DOT],
    "C": [DASH, DOT, DASH, DOT],
    "D": [DASH, DOT, DOT],
    "E": [DOT],
    "F": [DOT, DOT, DASH, DASH],
    "G": [DASH, DASH, DOT],
    "H": [DOT, DOT, DOT, DOT],
    "I": [DOT, DOT],
    "J": [DOT, DASH, DASH, DASH],
    "K": [DASH, DOT, DASH],
    "L": [DOT, DASH, DOT, DOT],
    "M": [DASH, DASH],
    "N": [DASH, DOT],
    "O": [DASH, DASH, DASH],
    "P": [DOT, DASH, DASH, DOT],
    "Q": [DASH, DASH, DOT, DASH],
    "R": [DOT, DASH, DOT],
    "S": [DOT, DOT, DOT],
    "T": [DASH],
    "U": [DOT, DOT, DASH],
    "V": [DOT, DOT, DOT, DASH],
    "W": [DOT, DASH, DASH],
    "X": [DASH, DOT, DOT, DASH],
    "Y": [DASH, DOT, DASH, DASH],
    "Z": [DASH, DASH, DOT, DOT],
    "0": [],
    "1": [DOT, DASH, DASH, DASH, DASH],
    "2": [DOT, DOT, DASH, DASH, DASH],
    "3": [DOT, DOT, DOT, DASH, DASH],
    "4": [DOT, DOT, DOT, DOT, DASH],
    "5": [DOT, DOT, DOT, DOT, DOT],
    "6": [DASH, DOT, DOT, DOT, DOT],
    "7": [DASH, DASH, DOT, DOT, DOT],
    "8": [DASH, DASH, DASH, DOT, DOT],
    "9": [DASH, DASH, DASH, DASH, DOT],
}

def start(message):
  firstWord = True
  for word in message.split(" "):
    if not firstWord:
      print("_W_")
      time.sleep(WORD_END)
    firstWord = False

    firstLetter = True
    for letter in word:
      if not firstLetter:
        print("_L_")
        time.sleep(LETTER_END)
      firstLetter = False

      print(letter),

      firstSymbol = True
      for symbol in ALPHABET[letter]:
        if not firstSymbol:
          print("_S_", end=" ")
          time.sleep(GAP)
        firstSymbol = False

        print('.' if symbol == DOT else '-', end=" ")

        turnlights(ON)
        time.sleep (symbol)
        turnlights(OFF)
  print("_M_")
  time.sleep(MESSAGE_END)

def turnlights(to):
  color = fancy.CHSV(75,255,to).pack()
  pixels.fill(color)
  pixels.show()

while True:
  start(MESSAGE)
