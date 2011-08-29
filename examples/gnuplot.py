#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "build","lib"))

from subprocess import call
from wde1 import WDE1
import time

def sensor_listener(src, event):
  if event.event_type == WDE1.SENSOR_UPDATE or event.event_type == WDE1.SENSOR_AVAILABLE:
    f = open("{0}.dat".format(str(event.adr)), "at")
    f.write("{0};{1}\n".format(str(event.timestamp), str(event.temperature)))
    f.close()
  if event.event_type == WDE1.SENSOR_UNREACHABLE:
    f = open("{0}.dat".format(str(event.adr)), "at")
    f.write("{0};NaN\n".format(str(event.timestamp)))
    f.close()

w = WDE1("/dev/ttyUSB0")
w.add_observer(sensor_listener,notify=WDE1.NOTIFY_ALL)
w.start_reading(blocking=False)

while True:
  time.sleep(20)
  call(["gnuplot", "plot.p"])
