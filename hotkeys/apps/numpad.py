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

'''Module that contains a numpad app'''

from hotkeys.app import App
from hotkeys.button import Button
from adafruit_hid.keycode import Keycode


class Numpad(App):
  '''Numpad app for the hotkeys'''
  title: str = 'Numpad'
  buttons: list[Button] = [
      # 1st row ---------
      Button(title='7    ', color=0x004166, actions=[Keycode.KEYPAD_SEVEN]),
      Button(title='8    ', color=0x004166, actions=[Keycode.KEYPAD_EIGHT]),
      Button(title='9    ', color=0x004166, actions=[Keycode.KEYPAD_NINE]),
      # 2nd row ---------
      Button(title='4    ', color=0x004166, actions=[Keycode.KEYPAD_FOUR]),
      Button(title='5    ', color=0x004166, actions=[Keycode.KEYPAD_FIVE]),
      Button(title='6    ', color=0x004166, actions=[Keycode.KEYPAD_SIX]),
      # 3rd row ---------
      Button(title='1    ', color=0x004166, actions=[Keycode.KEYPAD_ONE]),
      Button(title='2    ', color=0x004166, actions=[Keycode.KEYPAD_TWO]),
      Button(title='3    ', color=0x004166, actions=[Keycode.KEYPAD_THREE]),
      # 4th row ---------
      Button(title='0    ', color=0x004166, actions=[Keycode.KEYPAD_ZERO]),
      Button(title='.    ', color=0x640A66, actions=[Keycode.KEYPAD_PERIOD]),
      Button(title='ENTER', color=0x663F0A, actions=[Keycode.KEYPAD_ENTER])
  ]

  def __init__(self):
    super().__init__(self.title, self.buttons)
