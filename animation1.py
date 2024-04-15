from machine import I2C, Pin
from time import sleep_ms
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

oled_width = 128
oled_height = 64

disp = SSD1306_I2C(oled_width, oled_height, i2c)

def animate_fast_word(word):
    word_width = len(word) * 8  # Assuming each character is 8 pixels wide
    word_pos = oled_width  # Initial position of the word (right edge of the display)
    speed = 2  # Adjust speed by changing the value (higher values mean faster animation)
    
    while word_pos > -word_width:
        disp.fill(0)  # Clear the display
        disp.text(word, word_pos, 20)  # Display the word at its current position
        disp.show()  # Update the display
        
        word_pos -= speed  # Move the word to the left
        sleep_ms(50)  # Adjust animation speed by changing the delay

# Start the fast animation with a custom word
animate_fast_word("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
