import numpy as np
from hw1_4.utils import *


def quat_conj(q):
    w, x, y, z = q
    return np.array([w, -x, -y, -z])


theta = np.radians(90)

q = np.array([
    np.cos(theta/2),
    0,
    0,
    np.sin(theta/2)
])

v = np.array([0,1,0,0])

# v' = q v q^-1
q_inv = quat_conj(q)

v1 = quat_mult(q, v)
v2 = quat_mult(v1, q_inv)

print("Rotated vector:", v2[1:])