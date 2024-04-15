from machine import Pin, I2C
import network
from time import sleep
from ssd1306 import SSD1306_I2C
import urequests  # Import the urequests module for HTTP requests

# Initialize the OLED display
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled_width = 128
oled_height = 64
disp = SSD1306_I2C(oled_width, oled_height, i2c)

# Initialize Wi-Fi interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Define your Wi-Fi credentials
SSID = "cheak"
PASSWORD = "12345678"

# Connect to Wi-Fi network
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    disp.fill(0)  # Clear display
    disp.text("Connecting to", 0, 10)
    disp.text("Wi-Fi...", 0, 20)
    disp.show()
    sleep(1)

disp.fill(0)  # Clear display
disp.text("Wi-Fi Connected", 0, 10)
disp.show()

# Function to get internet speed
def get_internet_speed():
    try:
        response = urequests.get("http://speedtest.net/speedtest")
        speed = response.headers.get("Content-Length")
        response.close()
        return int(speed)  # Convert speed to integer (bytes per second)
    except Exception as e:
        print("Error fetching internet speed:", e)
        return None

# Main loop
while True:
    # Get internet speed
    speed = get_internet_speed()
    
    # Update OLED display
    disp.fill(0)  # Clear display
    disp.text("Wi-Fi Connected", 0, 10)
    if speed is not None:
        disp.text("Speed: {} B/s".format(speed), 0, 30)
    else:
        disp.text("Speed: Error", 0, 30)
    disp.show()
    
    sleep(5)  # Wait for 5 seconds before updating speed again
