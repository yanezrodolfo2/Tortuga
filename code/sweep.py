"""
sweep.py - MG996R servo range test

Purpose:
    Sweeps the righting-arm servo between its stowed and deployed
    positions on a loop, with no sensor in the path. Used to verify
    travel, check for mechanical interference with the shell, and
    confirm the arm clears the chassis before the detection logic is
    connected.

Why LGPIOFactory:
    gpiozero's default pin factory generates PWM in software, which
    produced visible jitter and audible buzzing on the MG996R. Setting
    the pin factory to lgpio moves PWM generation to hardware timing
    and the jitter largely disappears. (pigpio would also work but has
    no installation candidate on the current Raspberry Pi OS release.)

Pulse widths:
    min_pulse_width=0.0006 (600 us), max_pulse_width=0.0024 (2400 us)
    These override gpiozero's 1000-2000 us default to match the
    MG996R's actual range, so s.value = -1..+1 maps to the full sweep.

Wiring (MG996R):
    Signal (orange) -> Pi GPIO 12 (physical pin 32)
    Power  (red)    -> battery + (7.4V pack, NOT the Pi's 5V rail -
                       the MG996R draws up to ~2.5A at stall)
    Ground (brown)  -> battery -, AND jumpered to Pi GND (pin 6)
                       Grounds must be tied common for the signal to
                       have a reference.

Prerequisites:
    sudo apt install python3-lgpio

Run:
    python3 sweep.py
    Ctrl+C to exit.
"""

from gpiozero import Servo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

Device.pin_factory = LGPIOFactory()

s = Servo(12, min_pulse_width=0.0006, max_pulse_width=0.0024)

while True:
    s.value = -0.4
    sleep(1)
    s.value = 0.4
    sleep(1)
