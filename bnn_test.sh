#!/bin/sh
# Pass the path to build directory in the arguments.
./$1/bin/test_autodiff
./$1/bin/test_core
./$1/bin/test_operations
./$1/bin/test_cuda_core

