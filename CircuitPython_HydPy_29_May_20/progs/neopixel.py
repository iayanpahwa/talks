import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL,10)

led.brightness = 1

while True:
    led[0] = (0,0,100)
    led[3] = (0,100,0)
    led[6] = (100,0,0)


