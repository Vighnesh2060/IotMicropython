from machine import Pin
from time import sleep

LED = Pin("LED",Pin.OUT)

while True:
    LED.toggle()
    sleep(1/10)
    