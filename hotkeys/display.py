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
"""
This module contains the display class to show stuff to the user
"""
import displayio
import terminalio
from adafruit_display_text.label import Label
from adafruit_display_shapes.rect import Rect
from adafruit_macropad import MacroPad
from fontio import BuiltinFont


class Display:
  """Display class"""

  def __init__(self, macropad: MacroPad):
    self.display = macropad.display
    self.display.auto_refresh = False
    self.font: BuiltinFont = terminalio.FONT

  def initialize(self):
    self.group = displayio.Group()
    self.labels: list[Label] = []
    for key_index in range(12):
      # Create each one of the 12 labels for each button
      x: int = key_index % 3
      y: int = key_index // 3
      label = Label(
          self.font,
          text='',
          color=0xFFFFFF,
          anchored_position=(
              (self.display.width - 1) * x / 2,
              self.display.height - 1 - (3 - y) * 12
          ),
          anchor_point=(x / 2, 1.0)
      )
      self.labels.append(label)
      self.group.append(label)
    # Add a white backround for the title
    self.group.append(Rect(0, 0, self.display.width, 12, fill=0xFFFFFF))
    # Add a black text label for the title
    self.title_label: Label = label.Label(
        self.font,
        text='',
        color=0x000000,
        anchored_position=(self.display.width//2, -2),
        anchor_point=(0.5, 0.0)
    )
    self.group.append(self.title_label)
    self.display.show(self.group)

  @property
  def title(self) -> str:
    '''Title to display to the user'''
    return self.title_label.text

  @title.setter
  def set_title(self, title: str) -> None:
    '''Sets the title to display to the user'''
    self.title_label.text = title
    self.display.refresh()

  def __getitem__(self, button_number: int) -> str:
    '''The text of the corresponding button's label'''
    return self.get_button_label(button_number)

  def __setitem__(self, button_number: int, text: str) -> None:
    '''Sets the text of the corresponding button's label'''
    return self.set_button_label(button_number, text)

  def get_button_label(self, button_number: int) -> str:
    '''The text of the corresponding button's label'''
    return self.labels[button_number].text

  def set_button_label(self, button_number: int,  text: str) -> None:
    '''Sets the text of the corresponding button's label'''
    self.labels[button_number].text = text
    self.display.refresh()
