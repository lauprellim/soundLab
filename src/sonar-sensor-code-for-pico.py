'''
sonar-sensor-code-for-pico.py

This program simply reads distance data from an HC-SR04 connected
to a Raspberry Pi Pico, and prints the data the the terminal.

You can download and install CircuitPython on the Pico:
  https://circuitpython.org/downloads

We also need the adafruit_hcsr04 library, which is available in
the bundle here. Be sure to pick the correct bundle version for
the version of CircuitPython you installed. As of spring 2026,
we are on version 10.
  https://circuitpython.org/libraries


'''


import time
import board
import adafruit_hcsr04   # this should go in lib/ on the pico itsel

# Initialize the sensor on the specified pins.
# Replace board.D5 and board.D6 with your actual pin names.
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP0, echo_pin=board.GP1)

while True:
    try:
        # Read the distance in centimeters
        print(sonar.distance)
    except RuntimeError:
        # The sensor can sometimes return an error if it can't get a reading
        print("Retrying!")
        pass
    # Sleep for a short duration to prevent constant polling
    time.sleep(0.5)
