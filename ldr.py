from machine import ADC ,Pin
from time import sleep
from ssd1306 import SSD1306_I2C

ldr = ADC(2)

conv = 3.3/65535

led = Pin('LED',Pin.OUT)




while True:
    intensity =ldr.read_u16()
    inten =intensity*conv
    print(inten)
    sleep(1)
    
    if inten>=1.0:
       temp= led.value(0)
         disp.text(f"Temperature:{temp}",0,10)
    else:
        led.value(1)