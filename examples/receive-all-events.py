#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "build","lib"))


from wde1 import WDE1

def sensor_listener(src, event):
    print("=== listener: adr=2, notify every time ===")
    print("Sensor Address: " + str(event.adr))
    print("Changed since last receive:" + str(event.changed))
    print("Event type: " + event.event_type)
    print("Timestamp: " + str(event.timestamp))
    print("Temperature: " + str(event.temperature))
    print("Humidity: " + str(event.humidity))
    print("")

w = WDE1("/dev/ttyUSB0")
w.add_observer(sensor_listener, adr=2, notify=WDE1.NOTIFY_ALL)
w.start_reading(blocking=True)
