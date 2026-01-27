import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)

while True:
    pixels[0]=(255, 0, 0)
    pixels[1]=(0, 255, 0)
    pixels[2]=(0, 0, 255)
    pixels[3]=(150,30,25)
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5) 
