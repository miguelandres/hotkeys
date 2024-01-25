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


class Safari(App):
  '''Numpad app for the hotkeys'''
  title: str = 'Safari'
  # pylint: disable=line-too-long
  buttons: list[Button] = [
      # 1st row ---------
      Button(title='< Back', color=0x0A2B5E, actions=[Keycode.COMMAND, '[']),
      Button(title='Fwd >', color=0x0A2B5E, actions=[Keycode.COMMAND, ']']),
      Button(title='Up', color=0x5E4001, actions=[Keycode.SHIFT, ' ']),
      # 2nd row ---------
      Button(title='< Tab', color=0x095E06, actions=[
             Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
      Button(title='Tab >', color=0x095E06, actions=[
             Keycode.CONTROL, Keycode.TAB]),
      Button(title='Down', color=0x5E4001, actions=[' ']),
      # 3rd row ---------
      Button(title='Reload', color=0x5E143E, actions=[Keycode.COMMAND, 'r']),
      Button(title='Insta', color=0x5E143E, actions=[
             Keycode.COMMAND, 'n', -Keycode.COMMAND, 'http://instagram.com/\n']),
      Button(title='Private', color=0x5E143E, actions=[Keycode.COMMAND, 'N']),
      # 4th row ---------
      Button(title='Github', color=0x01255E, actions=[
             Keycode.COMMAND, 'n', -Keycode.COMMAND, 'http://github.com/\n']),
      Button(title='Twitter', color=0x01255E, actions=[Keycode.KEYPAD_PERIOD]),
      Button(title='Youtube', color=0x01255E, actions=[
             Keycode.COMMAND, 'n', -Keycode.COMMAND, 'http://youtube.com/\n'])
  ]

  def __init__(self):
    super().__init__(self.title, self.buttons)
