from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)

while True:
    a = sensor.get_accel_data()
    print(round(a['x'],2), round(a['y'],2), round(a['z'],2))
    sleep(0.5)
