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

"""Entry point to the code for the Hotkeys program"""
from action import Sequence
from adafruit_macropad import MacroPad
from app import App, load_all_apps
from display import Display
from pixels import Pixels

MACRO_FOLDER = '/macros'

macropad: MacroPad = MacroPad()
screen: Display = Display(macropad)
pixels: Pixels = Pixels(macropad)
last_position: int = 0
switching_mode: bool = False
app_index: int = 0

screen.initialize()


apps: list[App] = load_all_apps(MACRO_FOLDER)

if not apps:
  screen.set_title('NO MACRO FILES FOUND')
  while True:
    pass

try:  # Test the USB HID connection
  macropad.keyboard.release_all()
except OSError as err:
  print(err)
  screen.set_title('NO USB CONNECTION')
  while True:
    pass


def set_app(new_app_index: int):
  global app_index
  app_index = new_app_index % len(apps)
  macropad.keyboard.release_all()
  screen.set_app(apps[app_index])
  pixels.set_app(apps[app_index])


last_position = 0
set_app(0)

while True:
  macropad.encoder_switch_debounced.update()
  if macropad.encoder_switch_debounced.released:
    switching_mode = not switching_mode
  position = macropad.encoder
  if position != last_position:
    if switching_mode:
      set_app(position)
    else:
      if position > last_position:
        apps[app_index].encoder_increase_action.run(macropad)
      else:
        apps[app_index].encoder_decrease_action.run(macropad)
    last_position = position
  event = macropad.keys.events.get()
  if not event or event.key_number >= len(apps[app_index].macros):
    continue  # No key events, or no corresponding macro, resume loop
  key_number = event.key_number
  pressed = event.pressed

  sequence = Sequence(apps[app_index].macros[key_number]
                      [2] if key_number < 12 else [])
  if pressed:
    if key_number < 12:
      pixels.highlight(key_number, 0xFFFFFF)
    sequence.begin(macropad)

  else:
    sequence.end(macropad)
