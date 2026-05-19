import numpy as np
from hw1_4.utils import *

def quaternion_norm(q):
    return np.linalg.norm(q)


def quaternion_to_matrix(q):
    w, x, y, z = q

    return np.array([
        [1 - 2*(y*y + z*z), 2*(x*y - z*w), 2*(x*z + y*w)],
        [2*(x*y + z*w), 1 - 2*(x*x + z*z), 2*(y*z - x*w)],
        [2*(x*z - y*w), 2*(y*z + x*w), 1 - 2*(x*x + y*y)]
    ])



u = np.array([1,1,1]) / np.sqrt(3)
theta = 60

q = quat_from_axis(u, theta)
print("Quaternion:", q)

print("Norm:", quaternion_norm(q))

R = quaternion_to_matrix(q)
print("\nRotation matrix:\n", R)