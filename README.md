pywde1
======

`pywde1` is a simple wrapper library used to retrieve data from ELV USB-WDE1
wheather data receiver.

The library is designed around the [WDE1 specification][1].


Notes for the USB WDE1 data receiver
------------------------------------

The receiver itself does not provide any information on which sensor state 
changed, but instead sends the complete dataframe containing all sensors. This
is far from ideal.

As a consequence, the library provides mechanisms that one is only notified on
actual changes, i.e. phenomenon values changing. But since other use-cases may
need it, there also exists a mechanism to get a sensors state on the general 
update, i.e. at any time any sensor updates the receiver.

- Timeout for a sensor to be recognized as unreachable: 10 minutes
- Sensor updating frequency: 2.5-3 minutes (5-6 mHz)


Requirements
------------

### Linux 

It is important to have a kernel with the following modules loaded:

- [usbserial][2]
- cp210x


Install
-------

Under any sudo enabled Linux environment the install is just as easy as typing

```bash
python setup.py build
sudo python setup.py install
```

### Library dependencies
- pyserial
- python-setuptools


Examples
--------

Look at the example files that can be found in the `examples/` subdirectory.


License
-------

Copyright (C) 2011 by Researchstudio iSpace

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


[1]: http://www.elv-downloads.de/Assets/Produkte/9/920/92030/Downloads/92030_USB_WDE1_V1.0_UM.pdf "WDE1 specification"
[2]: http://www.kernel.org/doc/Documentation/usb/usb-serial.txt "usbserial"
