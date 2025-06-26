#importing the module
#module is a file containing code in python

#method 1 of importing
# import maths

# print(maths.addition(12, 12))

#method 2 for importing
from maths import addition #import particular function from module
print(addition(1, 14))

#package is a folder containing one or more modules

from models import basicMathsII

print(basicMathsII.power(9, 3))