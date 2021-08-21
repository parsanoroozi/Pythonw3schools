# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

# To create a module just save the code you want in a file with the file extension .py:
# actually it doesnt need the exort keyword like other languages
# and you can reach it using import keyword:

import util as utilFunc
utilFunc.theFunc()
# or
from  util import  theFunc
theFunc()

#if you want to import the file from outter directories...
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from number import Number

Number.calculateRand()
# Number.calculateRand()

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
x = dir(utilFunc)
print(x)



