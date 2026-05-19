import numpy as np
from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.math.Quaternion import Quaternion
from hw1_4.utils import *

obj = Cube(alpha=0.2)

alpha, beta, gamma = 20, 90, 50

qz = quat_from_axis(np.array([0,0,1]), alpha)
qy = quat_from_axis(np.array([0,1,0]), beta)
qx = quat_from_axis(np.array([1,0,0]), gamma)

q = quat_mult(qz, quat_mult(qy, qx))

print("Final quaternion:", q)
print("Norm:", np.linalg.norm(q))

angle_x, angle_y, angle_z = np.radians(alpha), np.radians(beta), np.radians(gamma)

qx = Quaternion.rotation_x(angle_x)
qy = Quaternion.rotation_y(angle_y)
qz = Quaternion.rotation_z(angle_z)
q_final = qz * qy * qx

animation_x = QuaternionAnimation(
    qx,
    channel="object",
)
animation_y = QuaternionAnimation(
    qy,
    channel="object",
)

animation_z = QuaternionAnimation(
    qz,
    channel="object",
)

run_animations([animation_x, animation_y, animation_z], "Task 3", obj)
