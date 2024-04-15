from machine import I2C, Pin
from time import sleep_ms
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

oled_width = 128
oled_height = 64

disp = SSD1306_I2C(oled_width, oled_height, i2c)

def animate_flying_object():
    object_width = 10  # Width of the flying object (adjust as needed)
    object_pos = -object_width  # Initial position of the flying object
    
    while True:
        disp.fill(0)  # Clear the display
        disp.fill_rect(object_pos, 10, object_width, 10, 1)  # Draw the flying object
        disp.show()  # Update the display
        
        object_pos += 1  # Move the object to the right
        if object_pos > oled_width:  # Reset position if object goes beyond display width
            object_pos = -object_width
        
        sleep_ms(50)  # Adjust the speed of animation by changing the delay

# Start the flying animation
animate_flying_object()
