from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)

while True:
    z = sensor.get_accel_data()['z']

    if z > 5:
        state = "UPRIGHT"
    elif z < -5:
        state = "FLIPPED"
    else:
        state = "ON ITS SIDE"

    print(f"z={z:6.2f}   {state}")
    sleep(0.3)
