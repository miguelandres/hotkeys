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

"""Controller for the Hotkeys program, takes user input and calls the model
(apps) and updates the views (pixels and display)"""
from adafruit_macropad import MacroPad
from keypad import Event

from hotkeys.action import Action
from hotkeys.app import App
from hotkeys.apps.numpad import Numpad
from hotkeys.apps.safari import Safari
from hotkeys.display import Display
from hotkeys.pixels import Pixels


class Controller:
  """Controller class that runs the interaction loop and updates the views based
  on user input"""
  macropad: MacroPad = MacroPad()
  display: Display = Display(macropad)
  pixels: Pixels = Pixels(macropad)

  apps: list[App] = [
      Numpad(),
      Safari(),
  ]

  def __init__(self) -> None:
    # If true, the encoder is being used to switch Apps, otherwise used for the
    # specific actions in the app (or volume control if none).
    self.switching_mode: bool = False
    # The last known position of the encoder, starts at 0 when just initialized
    self.last_position: int = 0
    # Index of the app currently in use
    self.app_index: int = 0
    # Current app in use
    self.app: App = self.apps[self.app_index]

  def initialize(self):
    self.display.initialize()
    try:  # Test the USB HID connection
      self.macropad.keyboard.release_all()
    except OSError as err:
      print(err)
      self.display.set_title('No USB Connection')
      while True:
        pass
    self.set_app(0)

  def set_app(self, new_app_index: int) -> None:
    self.app_index = new_app_index % len(self.apps)
    self.macropad.keyboard.release_all()
    self.app = self.apps[self.app_index]
    self.display.set_labels(self.app.title, self.app.button_titles)
    self.pixels.set_all_pixels(self.app.button_colors)

  def run_loop(self) -> None:
    while True:
      # First check whether the encoder has been released to switch from and to
      # app-switching mode
      self.macropad.encoder_switch_debounced.update()
      if self.macropad.encoder_switch_debounced.released:
        self.switching_mode = not self.switching_mode

      # check the current position of the encoder and compare it to the previous
      # one
      position: int = self.macropad.encoder
      if position != self.last_position:
        if self.switching_mode:
          # update the running app.
          # TODO: Figure out the math!
          self.set_app(position)
        else:
          if position > self.last_position:
            self.app.encoder_increase_action.run(self.macropad)
          else:
            self.app.encoder_decrease_action.run(self.macropad)
        self.last_position = position
      event: Event | None = self.macropad.keys.events.get()
      if not event or event.key_number >= 12:
        continue  # No key events, or invalid key event.
      key_number: int = event.key_number
      pressed: bool = event.pressed
      action: Action = self.app[key_number].actions

      # On button press, highlight the button setting it to white, and then
      # run the beginning of the action
      if pressed:
        if key_number < 12:
          self.pixels[key_number] = 0xFFFFFF
        action.begin(self.macropad)

      # On button release, reset the button color, and then run the end of the
      # action
      else:
        action.end(self.macropad)
        self.pixels[key_number] = self.app[key_number].color
