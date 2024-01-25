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

from adafruit_macropad import MacroPad
from adafruit_macropad import _PixelMapLite


BRIGHTNESS = 0.6


class Pixels:
  """Class to use the neopixels"""

  def __init__(self, macropad: MacroPad) -> None:
    if macropad.pixels is None:
      raise Exception('Macropad.pixels is None')
    self.pixels: _PixelMapLite = macropad.pixels
    self.pixels.auto_write = False
    self.pixels.brightness = BRIGHTNESS

  def get_pixel_color(self, pixel_number: int) -> int:
    return self.pixels[pixel_number]

  def set_pixel_color(self, pixel_number: int, color: int) -> None:
    self.pixels[pixel_number] = color
    self.pixels.show()

  def __getitem__(self, pixel_number: int) -> int:
    return self.get_pixel_color(pixel_number)

  def __setitem__(self, pixel_number: int, color: int) -> None:
    self.set_pixel_color(pixel_number, color)

  def set_all_pixels(self, color: int) -> None:
    for i in range(12):
      self.pixels[i] = color
    self.pixels.show()
