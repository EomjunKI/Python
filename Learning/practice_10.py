# 10.01 Module

import numpy as np  # use 'np' instead of 'numpy'

matrix_1 = np.array([1,2,3])
print(matrix_1)

from numpy import * # use all functions of numpy

matrix_2 = array([3,4,5])
print(matrix_2)

from numpy import array as arr  # use 'arr' instead of 'array'

matrix_3 = arr([4,5,6])
print(matrix_3)

# 10.02 Package

# 10.03 Run modules

if __name__ == "__main__":  # to check that it is top-level program
    print('Run internally')
else:
    print('Run externally')

# 10.04 Location of package or module

import inspect
import numpy
print(inspect.getfile(numpy))

# 10.05 Pip install

# 10.06 Builtin function

print(dir())    # display variables and functions