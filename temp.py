from machine import I2C, Pin
from time import sleep
from ssd1306 import SSD1306_I2C
from picozero import pico_temp_sensor


i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq=400000)

oled_width = 128
oled_height = 64

disp = SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    temp =pico_temp_sensor.temp
    sleep(1)
    disp.fill(0)
    disp.text(f"Temperature:{temp}",0,10)
    
    disp.show()
