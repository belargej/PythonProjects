#!/usr/bin/python3

from distutils.core import setup
from distutils.extension import Extension
import sys

boostlib = "boost_python"
if sys.version_info >= (3,0):
   boostlib = "boost_python-py32"

setup(name="Cangmom",
      ext_modules=[
        Extension("Cangmom",["Cangmom.cpp"],libraries=[boostlib])
        ])
