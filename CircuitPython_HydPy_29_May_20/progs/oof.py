from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)

while True:
    if cpx.button_a:
        # Type 'abc' followed by Enter (a newline).
        layout.write('\noof\n')
        while cpx.button_a:
            pass



