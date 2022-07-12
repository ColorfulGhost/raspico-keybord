import board
import time
import digitalio
import usb_hid
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from lib.adafruit_hid.keycode import Keycode

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
keyboard = Keyboard(usb_hid.devices)

layout=KeyboardLayoutUS(keyboard)
keyboard.send(Keycode.WINDOWS,Keycode.R)
time.sleep(0.11)
layout.write("cmd\n")

while True:
    time.sleep(1)
    led.value = True
    time.sleep(1)
    # keyboard.press()
    # keyboard.press(Keycode.ONE)
    led.value = False

# if __name__ == '__main__':
