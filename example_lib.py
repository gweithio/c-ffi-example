# example_lib.py

from cffi import FFI
# Create our FFI Builder
ffibuilder = FFI()
# Add the C definition
ffibuilder.cdef("int sum_list(int arr[], unsigned int length);")
# Set our source and include
ffibuilder.set_source("example_lib",'#include "example.h"',sources=["example.c"])
# Compile it to an .so file
ffibuilder.compile()
