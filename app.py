import os
from action import Action, MediaControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


class App:
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


def load_all_apps(dir) -> list[App]:
    apps: list[App] = []

    try:
        files = os.listdir(dir)
    except OSError as err:
        print(err)
        return apps

    for filename in files:
        if filename.endswith('.py'):
            try:
                module = __import__(dir + '/' + filename[:-3])
                apps.append(App(module.app))
            except (SyntaxError, ImportError, AttributeError, KeyError, NameError, IndexError, TypeError) as err:
                print(err)
                pass

    apps.sort(key=lambda m: m.order)
    return apps
