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

"""This module declares the App class which can declare different behaviors of
the macropad """
from adafruit_hid.consumer_control_code import ConsumerControlCode
from hotkeys.action import Action, MediaControl, Sequence
from hotkeys.button import Button


class App:
  """Class that defines the behavior of each button for a particular macropad
  configuration"""

  def __init__(
      self,
      title: str,
      buttons: list[Button],
      encoder_increase_actions: list[int, str, Action] | Action =
          MediaControl(ConsumerControlCode.VOLUME_INCREMENT),
      encoder_decrease_actions: list[int, str, Action] | Action = MediaControl(
          ConsumerControlCode.VOLUME_DECREMENT)
  ):
    self._title: str = title
    self._buttons: list[Button] = buttons
    if len(self._buttons) != 12:
      raise ValueError(f'App {self.title} does not contain 12 buttons!')
    self._encoder_increase_action: Action = (
        encoder_increase_actions if isinstance(encoder_increase_actions, Action)
        else Sequence(encoder_increase_actions)
    )
    self._encoder_decrease_action: Action = (
        encoder_decrease_actions if isinstance(encoder_decrease_actions, Action)
        else Sequence(encoder_decrease_actions)
    )

  @property
  def title(self) -> str:
    return self._title

  def get_button(self, button_number: int) -> Button:
    return self._buttons[button_number]

  def __getitem__(self, button_number: int) -> Button:
    return self.get_button(button_number)

  @property
  def button_titles(self) -> list[str]:
    return list(map(lambda button: button.title, self._buttons))

  @property
  def button_colors(self) -> list[int]:
    return list(map(lambda button: button.color, self._buttons))

  @property
  def encoder_increase_action(self) -> Action:
    return self._encoder_increase_action

  @property
  def encoder_decrease_action(self) -> Action:
    return self._encoder_decrease_action
