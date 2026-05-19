import numpy as np
from hw1_4.utils import *

M = np.array([
    [0, -2, 0, 10],
    [1,  0, 0, -5],
    [0,  0, 1.5, 3],
    [0,  0, 0, 1]
])

T = M[:3, 3]
print("Translation:", T)

A = M[:3, :3]

sx = np.linalg.norm(A[:,0])
sy = np.linalg.norm(A[:,1])
sz = np.linalg.norm(A[:,2])

S = np.array([sx, sy, sz])
print("Scale:", S)

R = np.zeros((3,3))
R[:,0] = A[:,0] / sx
R[:,1] = A[:,1] / sy
R[:,2] = A[:,2] / sz

print("\nRotation matrix:\n", R)

q = matrix_to_quaternion(R)
print("\nQuaternion:", q)