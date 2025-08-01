# Syenasweta Mechanical Keyboard
# Keymaps Layout Author by Nashrullah ALi Fauzi
# Hardware by Raspberry Pi Pico RP2040
# Software by CircuitPython 8.2.6
# Keyboard Firmware by KMK

import microcontroller
import board
import time
import supervisor
import storage
import usb_cdc
import usb_hid
import usb_midi

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP0,  # column
    source=board.GP12,  # row
    boot_device=0,
    cdc=True,
    consumer_control=True,
    keyboard=True,
    midi=True,
    mouse=True,
    nkro=True,
    pan=True,
    storage=True,
    usb_id=('Syenasweta', 'SyenaKeyboards: Syenasweta Mechanical Keyboard')
)

usb_cdc.enable(console=True, data=True)
storage.enable_usb_drive()
storage.remount("/", readonly=False, disable_concurrent_write_protection=True)
m = storage.getmount("/")
m.label = "SYENASWETA"
storage.remount("/", readonly=True, disable_concurrent_write_protection=False)
storage.enable_usb_drive()

# Uncomment bellow to reset CircuitPython
# import microcontroller
# microcontroller.on_next_reset(microcontroller.RunMode.UF2)
# microcontroller.reset()
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-resetting
