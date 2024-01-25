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
from hotkeys.button import Button, empty_button
from adafruit_hid.keycode import Keycode


class IntelliJ(App):
  '''IntelliJ app for the hotkeys'''
  title: str = 'IntelliJ'
  # pylint: disable=line-too-long
  buttons: list[Button] = [
      # 1st row ---------
      Button(title='Build', color=0x0A2B5E,
             actions=[Keycode.COMMAND, Keycode.F9]),
      Button(title='Rebuild', color=0x0A2B5E, actions=[
             Keycode.COMMAND, Keycode.SHIFT, Keycode.F9]),
      Button(title='Up', color=0x5E4001, actions=[
             Keycode.OPTION, Keycode.SHIFT, Keycode.UP_ARROW]),
      # 2nd row ---------
      Button(title='Rename', color=0x095E06, actions=[
             Keycode.SHIFT, Keycode.F6]),
      Button(title='Refactor', color=0x095E06, actions=[
             Keycode.CONTROL, Keycode.T]),
      Button(title='Dn', color=0x5E4001, actions=[
             Keycode.OPTION, Keycode.SHIFT, Keycode.DOWN_ARROW]),
      # 3rd row ---------
      Button(title='Move', color=0x095E06, actions=[
             Keycode.F6]),
      Button(title='Del', color=0x095E06, actions=[
             Keycode.COMMAND, Keycode.DELETE]),
      empty_button,
      # 4th row ---------
      Button(title='Reload', color=0x5E143E, actions=[
             Keycode.COMMAND, 'A', - Keycode.COMMAND, 'Reload all gradle projects\n']),
      Button(title='Format', color=0x5E143E, actions=[
             Keycode.COMMAND, Keycode.OPTION, Keycode.L]),
      Button(title='Imports', color=0x5E143E, actions=[
             Keycode.CONTROL, Keycode.OPTION, Keycode.O]),

  ]

  encoder_increase_action = [Keycode.CONTROL, Keycode.RIGHT_ARROW]
  encoder_decrease_action = [Keycode.CONTROL, Keycode.LEFT_ARROW]

  def __init__(self):
    super().__init__(
        title=self.title,
        buttons=self.buttons,
        encoder_increase_actions=self.encoder_increase_action,
        encoder_decrease_actions=self.encoder_increase_action)
