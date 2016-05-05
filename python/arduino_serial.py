#
# arduino_serial.py
#
# 2016 Developed by Keith Choison
#

import serial
from firebase import firebase

firebaseURL = 'https://ece158b-swe-mt.firebaseio.com/'

db = firebase.FirebaseApplication (firebaseURL, None)
arduino = serial.Serial ('/dev/ttyACM0', baudrate=9600, timeout=1)

print 'DYEL (Midterm) - Arduino Serial'

print '\nRunning...'

while 1:
  # clear serial buffer
  arduino.flushInput()
  
  temperature = float (arduino.readline().strip())
  db.put ('/main/', 'temp', temperature)
