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

"""MACROPAD Hotkeys: Zoom Hotkeys"""

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from action import MediaControl

app = {
    'name': 'Zoom',
    'order': 1,
    'macros': [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Audio  ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.A]),
        (0x544408, 'Screen ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.S]),
        (0x04541B, 'Video  ', [Keycode.COMMAND, Keycode.SHIFT, Keycode.V]),
        # 2nd row ----------
        (0x000754, 'Control', [Keycode.CONTROL,
         Keycode.OPTION, Keycode.COMMAND, Keycode.H]),
        (0x000000, '       ', []),
        (0x000754, 'Leave  ', [Keycode.COMMAND, Keycode.W]),
        # 3rd row ----------
        (0x000000, '       ', []),
        (0x095E06, 'Play/Pause',
         [MediaControl(ConsumerControlCode.PLAY_PAUSE)]),
        (0x000000, '       ', []),
        # 4th row ----------
        (0x080F54, 'Vol-   ',
         [MediaControl(ConsumerControlCode.VOLUME_DECREMENT)]),
        (0x000000, '       ', []),
        (0x080F54, 'Vol+   ',
         [MediaControl(ConsumerControlCode.VOLUME_INCREMENT)])
    ]
}
