#!/bin/sh
# Pass the first argument as path to build directory in the arguments.
# Pass the second argument one of, --CI=ON or --CI=OFF.
./$1/bin/test_autodiff $2
./$1/bin/test_cuda_core
./$1/bin/test_operations $2
./$1/bin/test_core $2
./$1/bin/test_io $2
