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

KEY_GP_MAP = [
    [board.GP1, Keycode.ONE],
    [board.GP2, Keycode.TWO],
    [board.GP3, Keycode.THREE],
    [board.GP4, Keycode.FOUR],
    [board.GP5, Keycode.FIVE],
    [board.GP6, Keycode.SIX],
    [board.GP7, Keycode.SEVEN],
    [board.GP8, Keycode.EIGHT],
    [board.GP9, Keycode.NINE]
]

buttons = []


for key in KEY_GP_MAP:
    btn = digitalio.DigitalInOut(key[0])
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    buttons.append(btn)


while True:
    time.sleep(0.1)
    for index,btn in enumerate(buttons):
        if btn.value:
            led.value = True
            # print(index)
            # print(KEY_GP_MAP[i][1])
            keyboard.press(KEY_GP_MAP[index][1])
            keyboard.release(KEY_GP_MAP[index][1])
    led.value = False