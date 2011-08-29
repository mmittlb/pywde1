#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 by Researchstudio iSpace
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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
