# Write your code here :-)
#Ejercicio 1.Neopixel
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.                   #Def quiere decir funciones. El comando wheel recibe un parametro(pos).
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(1)

BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
OFF = (0, 0, 0)


while True:
        color_chase(BLUE, 1)
        color_chase(CYAN, 1)
        color_chase(OFF, 1)