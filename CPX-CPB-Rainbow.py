import time
import board
import neopixel

# The number 10 represents how many neopixels are going to be used 
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    # This combination of colors changes the LED to turn Red
    # The number between the [] brackets represent the neopixel that's being turned that color
    # There are 10 neopixels, but the numbers start at 0
    pixels[0]=(255, 0, 0)
    pixels[1]=(255, 0, 0)
    # This combination of colors changes the LED to turn Yellow 
    pixels[2]=(155, 100, 0)
    pixels[3]=(155, 100, 0)
    # This combination of colors changes the LED to turn Green 
    pixels[4]=(0, 255, 0)
    pixels[5]=(0, 255, 0)
    # This combination of colors changes the LED to turn Blue 
    pixels[6]=(0, 0, 255)
    pixels[7]=(0, 0, 255)
    # This combination of colors changes the LED to turn Purple
    pixels[8]=(120, 0, 135)
    pixels[9]=(120, 0, 135)
    time.sleep(.5) 
