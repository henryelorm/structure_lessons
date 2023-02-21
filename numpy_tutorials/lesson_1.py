import numpy as np

a1 = np.array([[1, 2, 3], [4, 5, 6]], ndmin=2)
a1.shape = (3, 2)

a1 = np.array([1, 2, 3], dtype=complex)

# Data Types
dt = np.dtype([('age', np.int8)])
a2 = np.array([(10,), (20,), (30,)], dtype=dt)
a2.shape = (3, 2)

print(a2)

# an array of evenly spaced numbers
# this is one dimensional array
a3 = np.arange(24)
print(a3.ndim)

# now reshape it
b = a3.reshape(2, 4)
print(b)
# b is having three dimensions


# Array Creation Routines
x1 = np.empty([3, 2], dtype=int)

# array of five zeros. Default dtype is float
x2 = np.zeros(5)
print(x2)

# custom type
x3 = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(x3)

# array of five ones. Default dtype is float
x4 = np.ones(5)
print(x4)
