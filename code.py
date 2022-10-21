import time
from action import Sequence
from adafruit_macropad import MacroPad
from app import App, load_all_apps
from display import Display
from pixels import Pixels
from adafruit_hid.consumer_control_code import ConsumerControlCode

MACRO_FOLDER = '/macros'

macropad = MacroPad()
screen = Display(macropad)
pixels = Pixels(macropad)
last_position = None
switching_mode = False
sleeping = False
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0

screen.initialize()
apps: list[App] = load_all_apps(MACRO_FOLDER)


if not apps:
    screen.setTitle('NO MACRO FILES FOUND')
    while True:
        pass

try:  # Test the USB HID connection
    macropad.keyboard.release_all()
except OSError as err:
    print(err)
    screen.setTitle('NO USB CONNECTION')
    while True:
        pass


def setApp(new_app_index: int):
    app_index = new_app_index % len(apps)
    macropad.keyboard.release_all()
    screen.setApp(apps[app_index])
    pixels.setApp(apps[app_index])


last_position = 0
setApp(0)

while True:
    macropad.encoder_switch_debounced.update()
    if macropad.encoder_switch_debounced.released:
        switching_mode = not switching_mode
    position = macropad.encoder
    if position != last_position:
        if switching_mode:
            setApp(position)
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
