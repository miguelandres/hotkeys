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
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect


class Display:
  """Display class"""

  def __init__(self, macropad):
    self.display = macropad.display
    self.display.auto_refresh = False

  def initialize(self):
    self.group = displayio.Group()
    for key_index in range(12):
      x = key_index % 3
      y = key_index // 3
      self.group.append(
          label.Label(
              terminalio.FONT,
              text='',
              color=0xFFFFFF,
              anchored_position=(
                  (
                      self.display.width - 1) * x / 2,
                  self.display.height - 1 - (3 - y) * 12
              ),
              anchor_point=(x / 2, 1.0)
          )
      )
    self.group.append(Rect(0, 0, self.display.width, 12, fill=0xFFFFFF))
    self.group.append(
        label.Label(
            terminalio.FONT,
            text='',
            color=0x000000,
            anchored_position=(self.display.width//2, -2),
            anchor_point=(0.5, 0.0)
        )
    )
    self.display.show(self.group)

  def sleep(self):
    self.display.auto_brightness = False
    self.display.brightness = 0
    self.display.show(displayio.Group())
    self.display.refresh()

  def resume(self):
    self.display.brightness = 1
    self.display.auto_brightness = True
    self.display.show(self.group)
    self.display.refresh()

  def set_app(self, app):
    self.group[13].text = app.name
    for i in range(12):
      if i < len(app.macros):
        self.group[i].text = app.macros[i][1]
      else:
        self.group[i].text = ''
    self.display.refresh()

  def set_title(self, text):
    self.group[13].text = text
    for i in range(12):
      self.group[i].text = ''
    self.display.refresh()
