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

"""This module defines all possible actions that the Macropad can emulate"""

from adafruit_macropad import MacroPad


class Action:
  """Base class for all actions, each action must at least implement the begin
  and end methods here."""

  def run(self, macropad: MacroPad) -> None:
    self.begin(macropad)
    self.end(macropad)

  def begin(self, macropad: MacroPad) -> None:
    raise NotImplementedError

  def end(self, macropad: MacroPad) -> None:
    raise NotImplementedError


class MouseButton(Action):
  """Action that represents a mouse click."""

  def __init__(self, keycode: int) -> None:
    self.keycode: int = keycode

  def begin(self, macropad: MacroPad) -> None:
    if self.keycode < 0:
      macropad.mouse.press(self.keycode)
    else:
      macropad.mouse.release(self.keycode)

  def end(self, macropad: MacroPad) -> None:
    macropad.mouse.end(self.keycode)


class MouseMove(Action):
  """Action that represents a mouse movement."""

  def __init__(self, x: int, y: int, wheel: int) -> None:
    self.x: int = x
    self.y: int = y
    self.wheel: int = wheel

  def begin(self, macropad: MacroPad) -> None:
    macropad.mouse.move(self.x, self.y, self.wheel)

  def end(self, macropad: MacroPad) -> None:
    pass


MIDI_VELOCITY = 127


class Midi(Action):
  """Action that represents a Midi event being sent (default velocity set to
  127)."""

  def __init__(self, note: int | str, velocity: int = MIDI_VELOCITY) -> None:
    self.note: int | str = note
    self.velocity: int = velocity

  def begin(self, macropad: MacroPad) -> None:
    if self.note < 0:
      macropad.midi.send(macropad.NoteOff(self.note, 0))
    else:
      macropad.midi.send(macropad.NoteOn(self.note, self.velocity))

  def end(self, macropad: MacroPad) -> None:
    if self.note >= 0:
      macropad.midi.send(macropad.NoteOff(self.note, 0))


class Keyboard(Action):
  """
  Action that represents a keyboard key being pressed/released or a text being
  written in the current keyboard layout"""

  def __init__(self, key: int | str) -> None:
    self.key: int | str = key

  def begin(self, macropad: MacroPad) -> None:
    if not isinstance(self.key, int):
      macropad.keyboard_layout.write(self.key)
    elif self.key < 0:
      macropad.keyboard.release(self.key)
    else:
      macropad.keyboard.press(self.key)

  def end(self, macropad: MacroPad) -> None:
    if isinstance(self.key, int) and self.key >= 0:
      macropad.keyboard.release(self.key)


class MediaControl(Action):
  """Action for pressing a media control button"""

  def __init__(self, keycode: int) -> None:
    self.keycode: int = keycode

  def begin(self, macropad) -> None:
    if self.keycode < 0:
      macropad.consumer_control.release()
    else:
      macropad.consumer_control.press(self.keycode)

  def end(self, macropad) -> None:
    macropad.consumer_control.release()


def get_action(item: int | str | Action) -> Action:
  """Converts keycodes or strings into actions if necessary."""
  if isinstance(item, Action):
    return item
  else:
    return Keyboard(item)


class Sequence(Action):
  """Represents a sequence of actions to be performed for a macro, it is an
  action itself"""

  def __init__(self, actions: list[Action | str | int]):
    self.actions: list[Action] = list(map(
        get_action, actions))

  def begin(self, macropad: MacroPad):
    for action in self.actions:
      action.begin(macropad)

  def end(self, macropad: MacroPad):
    for action in reversed(self.actions):
      action.end(macropad)
