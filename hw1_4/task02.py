import numpy as np
from src.engine.animation.QuaternionAnimation import QuaternionAnimation
from src.math.Quaternion import Quaternion
from src.engine.model.Tetrahedron import Tetrahedron
from hw1_4.utils import *

def rotate_point(p, q):
    v = np.array([0, *p])
    q_inv = np.array([q[0], -q[1], -q[2], -q[3]])

    return quat_mult(quat_mult(q, v), q_inv)[1:]

obj = Tetrahedron(alpha=0.2)

points = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

q1 = quat_from_axis(np.array([1,0,0]), 45)
q2 = quat_from_axis(np.array([0,1,0]), 30)

q_total = quat_mult(q2, q1)

print("q_total:", q_total)

w, x, y, z = q_total
angle = 2 * np.arccos(w)
axis = np.array([x,y,z]) / np.sin(angle/2)

print("Axis:", axis)
print("Angle:", np.degrees(angle))

print("\nRotated points:")
for p in points:
    rp = rotate_point(p, q_total)
    print(rp)


angle_x, angle_y = np.radians(45), np.radians(30)

qx = Quaternion.rotation_x(angle_x)
qy = Quaternion.rotation_y(angle_y)
q_final = qy * qx

animation_x = QuaternionAnimation(
    qx,
    channel="object",
)
animation_y = QuaternionAnimation(
    qy,
    channel="object",
)

run_animations([animation_x, animation_y], "Task 2", obj)
