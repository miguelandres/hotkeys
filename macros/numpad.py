# # License and Copyright
#
# Copyright for portions of this project are held by John Ellis, 2001 as part of
# deckerego/Macropad_Hotkeys, licensed under an MIT license.
#
# All other copyright for in this project is held by Miguel Barreto, 2022, also
# licensed under an MIT License
#
# ## MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""MACROPAD Hotkeys: Universal Numpad"""

from adafruit_hid.keycode import Keycode

app = {
    'name': 'Numpad',
    'order': 2,
    'macros': [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004166, '7    ', [Keycode.KEYPAD_SEVEN]),
        (0x004166, '8    ', [Keycode.KEYPAD_EIGHT]),
        (0x004166, '9    ', [Keycode.KEYPAD_NINE]),
        # 2nd row ----------
        (0x004166, '4    ', [Keycode.KEYPAD_FOUR]),
        (0x004166, '5    ', [Keycode.KEYPAD_FIVE]),
        (0x004166, '6    ', [Keycode.KEYPAD_SIX]),
        # 3rd row ----------
        (0x004166, '1    ', [Keycode.KEYPAD_ONE]),
        (0x004166, '2    ', [Keycode.KEYPAD_TWO]),
        (0x004166, '3    ', [Keycode.KEYPAD_THREE]),
        # 4th row ----------
        (0x004166, '0    ', [Keycode.KEYPAD_ZERO]),
        (0x640A66, '.    ', [Keycode.KEYPAD_PERIOD]),
        (0x663F0A, 'ENTER', [Keycode.KEYPAD_ENTER])
    ]
}
