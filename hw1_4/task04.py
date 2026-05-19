import numpy as np
from hw1_4.utils import *

R = np.array([
    [0, -1, 0],
    [1,  0, 0],
    [0,  0, 1]
])

q = matrix_to_quaternion(R)
print("Quaternion:", q)