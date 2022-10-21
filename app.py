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
import os
from action import Action, MediaControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


class App:
  """Class that defines the behavior of each button for a particular macropad
  configuration"""

  def __init__(
      self,
      appdata,
      encoder_increase_macro: Action =
          MediaControl(ConsumerControlCode.VOLUME_INCREMENT),
      encoder_decrease_macro: Action = MediaControl(
          ConsumerControlCode.VOLUME_DECREMENT)
  ):
    self.name = appdata['name']
    self.order = appdata['order']
    self.macros = appdata['macros']
    self.encoder_increase_action: Action = encoder_increase_macro
    self.encoder_decrease_action: Action = encoder_decrease_macro


def load_all_apps(directory: str) -> list[App]:
  apps: list[App] = []

  try:
    files = os.listdir(directory)
  except OSError as err:
    print(err)
    return apps

  for filename in files:
    if filename.endswith('.py'):
      try:
        module = __import__(directory + '/' + filename[:-3])
        apps.append(App(module.app))
      except (
          SyntaxError, ImportError, AttributeError,
          KeyError, NameError, IndexError, TypeError
      ) as err:
        print(err)
        pass

  apps.sort(key=lambda m: m.order)
  return apps
