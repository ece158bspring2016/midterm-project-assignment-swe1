import time
import json
from firebase import Firebase

# Raspberry Pi Python GPIO Library
# https://pypi.python.org/pypi/RPi.GPIO
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  "
          "This is probably because you need superuser privileges.  "
          "You can achieve this by using 'sudo' to run your script")


# Set RPi GPIO numbering system
GPIO.setmode(GPIO.BOARD)


PIR_enter                = 0            # Input Pin for ENTER PIR Sensor
PIR_exit                 = 0            # Input Pin for EXIT PIR Sensor
PIRStatus                = None         # PIR Sensor HIGH/LOW output
occupancy_enter          = 0            # Variable for amount of people entering
occupancy_exit           = 0            # Variable for amount of people exiting
firebase_update_interval = 10           # Push to Firebase every X occupants
firebase_URL = Firebase('https://flickering-inferno-7283.firebaseio.com/message_list/')
date = time.strftime('%m/%d/%Y')

while (1):
    # Reset occupancy every day
    if date is not time.strftime('%m/%d/%Y'):
        occupancy_enter = 0
        occupancy_exit = 0

    # Wait (blocking) on GPIO Rise (Low to High)
    GPIO.add_event_detect(PIR_enter, GPIO.RISING)  # add rising edge detection on a channel
    GPIO.add_event_detect(PIR_exit, GPIO.RISING)  # add rising edge detection on a channel

    if GPIO.event_detected(PIR_enter):
        occupancy_enter += 1
    if GPIO.event_detected(PIR_exit):
        occupancy_exit += 1


    # Setup JSON for time, date, and current occupants
    data = {'time': time.strftime('%H:%M:%S'),
            'date': time.strftime('%m/%d/%Y'),
            'occupancyEnter': occupancy_enter,
            'occupancyExit': occupancy_exit
           }

    # Push data to Firebase every X occupants
    if (occupancy_enter  % firebase_update_interval == 0) or (occupancy_exit % firebase_update_interval == 0):
        result = firebase_URL.push(data)
        print result


