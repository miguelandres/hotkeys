from adafruit_macropad import MacroPad


class Action:
    def run(self, macropad: MacroPad):
        self.begin(macropad)
        self.end(macropad)

    def begin(self, macropad: MacroPad):
        raise NotImplementedError

    def end(self, macropad: MacroPad):
        raise NotImplementedError


class MouseButton(Action):
    def __init__(self, keycode: int):
        self.keycode = keycode

    def begin(self, macropad: MacroPad):
        if self.keycode < 0:
            macropad.mouse.press(self.keycode)
        else:
            macropad.mouse.release(self.keycode)

    def end(self, macropad: MacroPad):
        macropad.mouse.end(self.keycode)


class MouseMove(Action):
    def __init__(self, x: int, y: int, wheel: int):
        self.x = x
        self.y = y
        self.wheel = wheel

    def begin(self, macropad: MacroPad):
        macropad.mouse.move(self.x, self.y, self.wheel)

    def end(self, macropad: MacroPad):
        pass


MIDI_VELOCITY = 127


class Midi(Action):
    def __init__(self, note: int | str):
        self.note = note

    def begin(self, macropad: MacroPad):
        if self.note < 0:
            macropad.midi.send(macropad.NoteOff(self.note, 0))
        else:
            macropad.midi.send(macropad.NoteOn(self.note, MIDI_VELOCITY))

    def end(self, macropad: MacroPad):
        if self.note >= 0:
            macropad.midi.send(macropad.NoteOff(self.note, 0))


class Keyboard(Action):
    def __init__(self, key: int | str):
        self.key = key

    def begin(self, macropad: MacroPad):
        if not isinstance(self.key, int):
            macropad.keyboard_layout.write(self.key)
        elif self.key < 0:
            macropad.keyboard.release(self.key)
        else:
            macropad.keyboard.press(self.key)

    def end(self, macropad: MacroPad):
        if isinstance(self.key, int) and self.key >= 0:
            macropad.keyboard.release(self.key)


class MediaControl(Action):
    def __init__(self, keycode: int):
        self.keycode = keycode

    def begin(self, macropad):
        if self.keycode < 0:
            macropad.consumer_control.release()
        else:
            macropad.consumer_control.press(self.keycode)

    def end(self, macropad):
        macropad.consumer_control.release()


def get_action(item: int | str | Action) -> Action:
    if isinstance(item, Action):
        return item
    else:
        return Keyboard(item)


class Sequence(Action):
    def __init__(self, actions: list[Action | str | int]):
        self.actions: list[Action] = list(map(
            lambda item: get_action(item), actions))

    def begin(self, macropad: MacroPad):
        for action in self.actions:
            action.begin(macropad)

    def end(self, macropad: MacroPad):
        for action in reversed(self.actions):
            action.end(macropad)
