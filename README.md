pywde1
======

`pywde1` is a simple wrapper library used to retrieve data from ELV USB-WDE1
wheather data receiver.

The library is designed around the [WDE1 Spec][1].


Requirements
------------

### Linux 

It is important to have a kernel with the following modules loaded:

- usbserial
- cp210x


Install
-------

Under any Posix compliant environment the install is just as easy as typing

```bash
python setup.py build
sudo python setup.py install
```

### Library dependencies
- pyserial


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


Links
-----

[1]: http://www.elv-downloads.de/Assets/Produkte/9/920/92030/Downloads/92030_USB_WDE1_V1.0_UM.pdf "WDE1 Spec"
