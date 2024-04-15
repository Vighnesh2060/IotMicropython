from machine import I2C, Pin
from time import sleep_ms
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

oled_width = 128
oled_height = 64

disp = SSD1306_I2C(oled_width, oled_height, i2c)

def animate_text(text, start_pos, end_pos, delay_ms):
    for pos in range(start_pos, end_pos + 1):
        disp.fill(0)  # Clear the display
        disp.text(text, pos, 10)  # Display text at current position
        disp.show()  # Update the display
        sleep_ms(delay_ms)  # Pause for a short duration

while True:
    animate_text("", 0, oled_width - 32, 50)  # Animate text from left to right
    sleep_ms(1000)  # Pause for a second before restarting the animation
