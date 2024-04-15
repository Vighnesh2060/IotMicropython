from machine import ADC, Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C

# Initialize the ADC for LDR
ldr = ADC(2)

# Conversion factor from ADC value to voltage
conv = 3.3 / 65535

# Initialize LED pin
led = Pin('LED', Pin.OUT)

# Initialize I2C for OLED display
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled_width = 128
oled_height = 64
disp = SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    intensity = ldr.read_u16()
    voltage = intensity * conv
    
    # Clear the OLED display
    disp.fill(0)
    
    # Display LDR intensity and voltage on the OLED
    disp.text(f"LDR Intensity: {intensity}", 0, 10)
    disp.text(f"LDR Voltage: {voltage:.2f} V", 0, 30)
    
    # Control LED based on LDR reading
    if voltage >= 1.0:
        led.off()  # Turn off LED
        disp.text("LED Status: OFF", 0, 50)
    else:
        led.on()  # Turn on LED
        disp.text("LED Status: ON", 0, 50)
    
    # Update and show OLED display
    disp.show()
    
    sleep(1)
