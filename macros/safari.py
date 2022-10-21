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

"""MACROPAD Hotkeys: Safari web browser for Mac"""

from adafruit_hid.keycode import Keycode

app = {
    'name': 'MacOS Safari',
    'order': 0,
    'macros': [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0A2B5E, '< Back ', [Keycode.COMMAND, '[']),
        (0x0A2B5E, 'Fwd >  ', [Keycode.COMMAND, ']']),
        (0x5E4001, 'Up     ', [Keycode.SHIFT, ' ']),
        # 2nd row ----------
        (0x095E06, '< Tab  ', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x095E06, 'Tab >  ', [Keycode.CONTROL, Keycode.TAB]),
        (0x5E4001, 'Down   ', ' '),
        # 3rd row ----------
        (0x5E143E, 'Reload ', [Keycode.COMMAND, 'r']),
        (0x5E143E, 'Home   ', [Keycode.COMMAND, 'H']),
        (0x5E143E, 'Private', [Keycode.COMMAND, 'N']),
        # 4th row ----------
        (0x01255E, 'GitHub ', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                               'https://github.com/notifications\n']),
        (0x01255E, 'AWS    ', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                               'http://console.aws.amazon.com\n']),
        (0x01255E, 'Feedly ', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                               'https://feedly.com/\n'])
    ]
}
