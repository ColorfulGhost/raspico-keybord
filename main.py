import board
import time
import digitalio
import usb_hid
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from lib.adafruit_hid.keycode import Keycode
from adafruit_debouncer import Debouncer

time.sleep(1)

key_combination = None


class Button:

    _keyboard = Keyboard(usb_hid.devices)
    _layout = KeyboardLayoutUS(_keyboard)

    def __init__(
        self, board_pin, keycodes, write_content, debounce_interval=0.01, pull=digitalio.Pull.DOWN
    ):
        self._record_btn_state = False
        self._write_content = write_content
        self._layout = Button._layout
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

    # def key_combination(self,):

    def update(self):
        debouncer = self._debouncer
        debouncer.update()
        if debouncer.rose:
            self._layout.write(*self._write_content)
            # self._rose_action(*self._keycodes)
        elif debouncer.fell:
            self._layout.write(' ')
            # self._fell_action(*self._keycodes)


buttons = [
    Button(board.GP1, [Keycode.ONE], ['wocaonima xiaobizaizi santianzhineishaleni \n']),
    Button(board.GP2, [Keycode.TWO], ['233 ']),
    Button(board.GP3, [Keycode.THREE], ['`exec slam6`']),
    Button(board.GP4, [Keycode.FOUR], ['wocaonima ']),
    Button(board.GP5, [Keycode.FIVE], ['wocaonima ']),
    Button(board.GP6, [Keycode.SIX], ['wocaonima ']),
    Button(board.GP7, [Keycode.SEVEN], ['wocaonima ']),
    Button(board.GP8, [Keycode.EIGHT], [' ']),
    Button(board.GP9, [Keycode.NINE], [' '])
]

while True:
    for b in buttons:
        b.update()
