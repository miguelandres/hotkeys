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

"""This module declares the Button class that represents a single button and
its behavior"""
from hotkeys.action import Action, Sequence


class Button:
  """Class that represents the configuration and status of a button"""

  def __init__(
      self,
      title: str,
      color: int,
      actions: list[Action | int | str],
  ):
    self._title: str = title
    self._color: int = color
    self._action: Action = Sequence(actions)

  @property
  def title(self) -> str:
    '''Gets the current title of this button.'''
    return self._title

  @property
  def color(self) -> int:
    '''Gets the current color of this button's pixel.'''
    return self._color

  @property
  def actions(self) -> Action:
    '''Gets the action that this button executes. The action may have been
    converted from other simpler objects'''
    return self._action


# A button that does nothing and doesn't light up
empty_button = Button('', 0, [])
