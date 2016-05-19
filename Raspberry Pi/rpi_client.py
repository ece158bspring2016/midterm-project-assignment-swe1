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


PIRPin         = 0            # Input Pin for PIR Sensor
PIRStatus      = None         # PIR Sensor HIGH/LOW output
occupancy_count = 0            # Variable to hold weight room occupancy
firebase_update_interval = 10 # Push to Firebase every X occupants
firebase_URL = Firebase('https://flickering-inferno-7283.firebaseio.com/message_list/')
date = time.strftime('%m/%d/%Y')

while (1):
    # Reset occupancy every day
    if date is not time.strftime('%m/%d/%Y'):
        occupancy_count = 0

    # Wait (blocking) on GPIO Rise (Low to High)
    GPIO.wait_for_edge(PIRPin, GPIO.RISING)
    occupancy_count  += 1

    # Setup JSON for time, date, and current occupants
    data = {'time': time.strftime('%H:%M:%S'),
            'date': time.strftime('%m/%d/%Y'),
            'occupancy': occupancy_count
           }

    # Push data to Firebase every X occupants
    if occupancy_count  % firebase_update_interval == 0:
        result = firebase_URL.push(data)
        print result

    # data1 = {'name': 'erikx',
    #         'time': time.strftime('%H:%M:%S'),
    #         'date': time.strftime('%m/%d/%Y'),
    #         'occupancy': 0
    #        }

    #r = f.update(data1)
    #print r

    # r = firebase_URL.get()
    # print json.dumps(r, sort_keys=True, indent=4, separators=(',', ': '))
