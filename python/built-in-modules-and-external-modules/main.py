# External-module

import pandas   # Importing the pandas library

print("Hello World!")

import pandas as pd
 
data = {
    "Name": ["Alice", "Bob", "Charlie"],   # I dont understand this code yet. Instructor said that will be taught later. so i copied the example for now.
    "Age": [24, 30, 28]
}
 
df = pd.DataFrame(data)
print(df)

"""
Examples if External-modules ==
Numpy
Pandas
Matplotlib
"""


# Built-in-module

import os   # Importing Python's built-in os module

print("Hello Python!")

print(os.listdir())   # It prints the content of a directory
print(os.getcwd())   # It will tell you the current directory you are in

"""
Examples if Built-in-modules ==
OS
Math
sys
"""

# You can use a module by importing it into your program.