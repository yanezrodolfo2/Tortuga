"""
right.py - Tortuga self-righting routine

Purpose:
    The integrated self-righting program. Continuously reads the
    MPU-6050 Z axis; when the rover is detected inverted, it drives
    the righting arm from stowed to deployed, holds, then returns the
    arm to stowed and waits before re-arming.

Sequence:
    1. Arm driven to STOWED on startup, held 1 s to settle.
    2. Loop: read Z.
         z < -5 m/s^2  -> inverted. Deploy arm, hold 1.5 s so the
                          sweep carries the chassis over, return to
                          STOWED, then wait 3 s before testing again
                          (prevents immediate re-trigger while the
                          rover is still settling).
         otherwise     -> upright, print Z and keep watching.
    3. 0.3 s poll interval.

Servo positions:
    STOWED   = -0.4   arm lies along the deck
    DEPLOYED = +0.8   arm swept out past vertical

    DEPLOYED was raised from +0.4 to +0.8 during bench testing: at
    +0.4 the arm swept but did not carry enough angle to roll the
    assembled chassis over.

Wiring:
    MPU-6050: VCC -> pin 1, GND -> pin 6, SDA -> pin 3, SCL -> pin 5
    MG996R:   signal (orange) -> GPIO 12 (physical pin 32)
              power  (red)    -> 7.4V battery +
              ground (brown)  -> battery -, jumpered to Pi GND (pin 6)

Prerequisites:
    pip install mpu6050-raspberrypi --break-system-packages
    sudo apt install i2c-tools python3-smbus python3-lgpio
    I2C enabled via raspi-config; verify with: i2cdetect -y 1 -> 0x68

Run:
    python3 right.py
    Ctrl+C to exit.
"""

from gpiozero import Servo, Device
from gpiozero.pins.lgpio import LGPIOFactory
from mpu6050 import mpu6050
from time import sleep

Device.pin_factory = LGPIOFactory()

sensor = mpu6050(0x68)
s = Servo(12, min_pulse_width=0.0006, max_pulse_width=0.0024)

STOWED = -0.4
DEPLOYED = 0.8

s.value = STOWED
sleep(1)

print("watching for flip...")

while True:
    z = sensor.get_accel_data()['z']

    if z < -5:
        print("FLIPPED - deploying arm")
        s.value = DEPLOYED
        sleep(1.5)
        s.value = STOWED
        sleep(3)
    else:
        print(f"upright  z={z:.1f}")

    sleep(0.3)
