#!/usr/bin/python3


# Imports from the same directory
from one import one_func
from two import two_func

# Imports from different directory
from three import four

# Import function from different directory
from three.four import four_func

one_func()
two_func()
four.four_func()
four_func()
