'''
read-serial-into-terminal.py

This code is for Windows machines with "COM" ports such as "COM5".

Run this code to read serial information into the terminal.
This can be used to connect to a Raspberry Pi Pico.
When this code is terminated, the pi pico will be available for other software,
such as PureData.

'''

import serial
import time

# Configure the serial port and baud rate
# Replace 'COM5' with your port name that you can find in the corner of Thonny
# The baudrate 115200 is specific to the Raspberry Pi Pico
ser = serial.Serial(port='COM5', baudrate=115200, timeout=1) 

# Wait a moment for the connection to establish
time.sleep(0.5)

print("Starting serial monitor...")

try:
    while True:
        # Read a line of data from the serial port
        # It returns bytes, so decode it to a string and strip whitespace
        line = ser.readline().decode('utf-8').strip() 

        if line:
            print(line)

except KeyboardInterrupt:
    # Exit the loop when Ctrl+C is pressed
    print("Serial monitor stopped.")

finally:
    # Close the serial connection
    ser.close()
