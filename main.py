import board
import time
import digitalio
import usb_hid
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from lib.adafruit_hid.keycode import Keycode
from adafruit_debouncer import Debouncer

time.sleep(1)


class Button:
    _keyboard = Keyboard(usb_hid.devices)

    def __init__(
        self, board_pin, keycodes, debounce_interval=0.01, pull=digitalio.Pull.DOWN
    ):
        self._board_pin = board_pin
        self._keycodes = keycodes
        self._pin = digitalio.DigitalInOut(board_pin)
        self._pin.direction = digitalio.Direction.INPUT
        self._pin.pull = pull
        self._debouncer = Debouncer(self._pin, debounce_interval)
        if pull == digitalio.Pull.DOWN:
            self._rose_action = Button._keyboard.press
            self._fell_action = Button._keyboard.release
        else:
            self._fell_action = Button._keyboard.press
            self._rose_action = Button._keyboard.release

    def update(self):
        debouncer = self._debouncer
        debouncer.update()
        if debouncer.fell:
            self._fell_action(*self._keycodes)
        elif debouncer.rose:
            self._rose_action(*self._keycodes)


buttons = [
    Button(board.GP1, [Keycode.ONE]),
    Button(board.GP2, [Keycode.TWO]),
    Button(board.GP3, [Keycode.THREE]),
    Button(board.GP4, [Keycode.FOUR]),
    Button(board.GP5, [Keycode.FIVE]),
    Button(board.GP6, [Keycode.SIX]),
    Button(board.GP7, [Keycode.SEVEN]),
    Button(board.GP8, [Keycode.EIGHT]),
    Button(board.GP9, [Keycode.NINE])
]
while True:
    for b in buttons:
        b.update()
