import numpy as np
from matplotlib import pyplot as plt

# indexing and slicing
a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
# b = np.array([1.0, 2.0, 3.0])

x = np.arange(1, 11)

y = 2 * x + 10


plt.plot(x, y)
plt.title('Normal title')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()