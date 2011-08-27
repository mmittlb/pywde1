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

import re
import serial

class FormatError(BaseException):

    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return ("FormatError: {0}".format(self._msg))

class WDE1(object):

    ADR_KOMBI = 8

    SENSOR_AVAILABLE = "SENSOR_AVAILABLE"
    SENSOR_UPDATE = "SENSOR_UPDATE"
    SENSOR_UNREACHABLE = "SENSOR_UNREACHABLE"

    def __init__(self, port):
        self._observers = []
        self._sensors = [ 
          {"adr": i, 
           "temperature": None, 
           "humidity": None} for i in range(8)] + [{ 
           "adr": WDE1.ADR_KOMBI, 
           "temperature": None, 
           "humidity":None,
           "windspeed":None, 
           "raincycles":None, 
           "rain": None}
        ]
        self.ser = serial.Serial(port)

    def add_observer(self, fn, adr=None):
        if not (fn,adr) in self._observers:
            self._observers.append((fn,adr))

    def remove_observer(self, fn, adr=None):
        if (fn,adr) in self._observers:
            self._observers.remove((fn,adr))

    @property
    def observers(self):
        return self._observers

    def _parse_line(self, raw):
        matches = re.search(
            "^\$1;1;;" +
            8 * "([-0-9,]*);" +
            8 * "([0-9]{0,2});" +
            "([-0-9,]*);([0-9]{0,2});([0-9]{0,3},?[0-9]?);([0-9]{0,4});([01]);0\r\n$", raw
        )
        if not matches:
            # currently only OpenLog format is supported
            # TODO: should switch format here
            raise FormatError("currently only OpenLog format is supported")

        # substitute "" by None 
        values = [x if x != "" else None for x in matches.groups()]
        # first 8 values are floats per spec (temperature)
        values[0:8] = [float(x.replace(",", ".")) if x else None for x in
                values[0:8]]
        # second 8 values are ints per spec (humidity)
        values[8:16] = [int(x) if x else None for x in values[8:16]]
        # rest is float,int,float,int,bool per spec (kombi sensor)
        values[16] = float(values[16].replace(",", ".")) if values[16] else None
        values[17] = int(values[17]) if values[17] else None
        values[18] = float(values[18].replace(",",".")) if values[18] else None
        values[19] = int(values[19]) if values[19] else None
        values[20] = True if values[20] == "1" else False
        return values

    def _update_sensor(self, value, check_index, check_phen):
        if self._sensors[check_index][check_phen] != value:
            if self._sensors[check_index][check_phen] == None and value != None:
                typ =  WDE1.SENSOR_AVAILABLE
            if self._sensors[check_index][check_phen] != None and value != None:
                typ =  WDE1.SENSOR_UPDATE
            if self._sensors[check_index][check_phen] != None and value == None:
                typ = WDE1.SENSOR_UNREACHABLE
            self._sensors[check_index][check_phen] = value
            return typ
        return None


    def _update_state(self, values):
        notify_ids = {}
        for i in range(0, 7):
            typ = self._update_sensor(values[i], i, "temperature")
            if typ:
                notify_ids[str(i)] = typ
            typ = self._update_sensor(values[i+8], i, "humidity")
            if typ:
                notify_ids[str(i)] = typ
        typ = self._update_sensor(values[16], WDE1.ADR_KOMBI, "temperature")
        if typ:
            notify_ids[str(i)] = typ
        typ = self._update_sensor(values[17], WDE1.ADR_KOMBI, "humidity")
        if typ:
            notify_ids[str(WDE1.ADR_KOMBI)] = typ
        typ = self._update_sensor(values[18], WDE1.ADR_KOMBI, "windspeed")
        if typ:
            notify_ids[str(WDE1.ADR_KOMBI)] = typ
        typ = self._update_sensor(values[19], WDE1.ADR_KOMBI, "raincycles")
        if typ:
            notify_ids[str(WDE1.ADR_KOMBI)] = typ
        typ = self._update_sensor(values[20], WDE1.ADR_KOMBI, "rain")
        if typ:
            notify_ids[str(WDE1.ADR_KOMBI)] = typ

        return notify_ids

    def _notify(self, id_map):
        for key in id_map:
            int_key = int(key)
            for (obs,adr) in self._observers:
                if adr == None or adr == int_key:
                    obs(id_map[key], self._sensors[int_key])

    def start_reading(self):
        self.ser.open()
        line = self.ser.readline()
        while True:
            values = self._parse_line(line)
            ids = self._update_state(values)
            self._notify(ids)
            line = self.ser.readline()

    def close(self):
        self.ser.close()
