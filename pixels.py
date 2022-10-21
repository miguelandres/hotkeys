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

"""Module to use the neopixels on each macropad button"""

from app import App
from adafruit_macropad import MacroPad


BRIGHTNESS = 0.6


class Pixels:
  """Class to use the neopixels"""

  def __init__(self, macropad: MacroPad):
    self.pixels = macropad.pixels
    self.pixels.auto_write = False
    self.pixels.brightness = BRIGHTNESS

  def set_app(self, app: App):
    self.macros = app.macros

    for i in range(12):
      if i < len(self.macros):
        self.pixels[i] = self.macros[i][0]
      else:
        self.pixels[i] = 0
    self.pixels.show()

  def sleep(self):
    self.pixels.brightness = 0.0
    self.pixels.show()

  def resume(self):
    self.pixels.brightness = BRIGHTNESS
    self.pixels.show()

  def highlight(self, key_number: int, color: int):
    self.pixels[key_number] = color
    self.pixels.show()

  def reset(self, key_number: int):
    self.pixels[key_number] = self.macros[key_number][0]
    self.pixels.brightness = BRIGHTNESS
    self.pixels.show()

  def reset_all(self, key_number: int):
    self.pixels[key_number] = self.macros[key_number][0]
    self.pixels.brightness = BRIGHTNESS
    self.pixels.show()
