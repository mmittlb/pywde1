#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os

from wde1 import __version__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pywde1",
    version = __version__,
    license = "MIT",
    url = "https://github.com/zoidrr/pywde1",
    packages = ["wde1"],
    description = "pywde1 is a simple wrapper library used to retrieve data "
                  "from ELV USB-WDE1 wheather data receiver.",
    long_description = read("README.md"),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
)
