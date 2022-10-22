# Adafruit Macropad Libraries

The libraries required by this version of Macropad Hotkeys includes:

- adafruit_debouncer.mpy
- adafruit_display_shapes
- adafruit_display_text
- adafruit_displayio_layout
- adafruit_hid
- adafruit_macropad.mpy
- adafruit_midi
- adafruit_pixelbuf.mpy
- adafruit_simple_text_display.mpy
- neopixel.mpy

## Installation via circup (recommended)

```shell
pip3 install circup

circup install adafruit_debouncer.mpy
circup install adafruit_display_shapes
circup install adafruit_display_text
circup install adafruit_displayio_layout
circup install adafruit_hid
circup install adafruit_macropad.mpy
circup install adafruit_midi
circup install adafruit_pixelbuf.mpy
circup install adafruit_simple_text_display.mpy
circup install neopixel.mpy
```

You can also use `circup update --all` for convenience.

## Installation with VS Code

- Install the [CircuitPython Extension](https://marketplace.visualstudio.com/items?itemName=joedevivo.vscode-circuitpython)
- Open the CIRCUITPYTHON drive (`code /Volumes/CIRCUITPYTHON`)
- `⌘ + ⇧ + P` to pull up the command palette and use the `CircuitPython: Show Available Libraries` command to install the required libraries one by one

## License

These libraries are individually licensed in each of their GitHub repositories
and are provided by Adafruit under the [MIT License](LICENSE.md).
