from hw1_2.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4
from src.math.utils_matrix import decompose_affine_2


obj = Cube(alpha=0.2)

cube = cube_points()

R_ext = rot_z(60) @ rot_y(45) @ rot_x(30)

R_int = rot_x(60) @ rot_y(45) @ rot_z(30)

print("External matrix:\n", R_ext)
print("Internal matrix:\n", R_int)

tr_ext = apply(cube, R_ext)
tr_int = apply(cube, R_int)

print_points("External result (X30→Y45→Z60)", tr_ext)
print_points("Internal result (X60→Y45→Z30)", tr_int)

T1, R1, S1, u, theta = decompose_affine_2(R_int)

rotation = RotationAnimation(
    end=theta,
    axis=u,
    channel="object",
)

rotation_x = RotationAnimation(
    end=np.radians(30),
    axis=Vec4(1, 0, 0),
    channel="object",
)

rotation_y = RotationAnimation(
    end=np.radians(45),
    axis=Vec4(0, 1, 0),
    channel="object",
)

rotation_z = RotationAnimation(
    end=np.radians(60),
    axis=Vec4(0, 0, 1),
    channel="object",
)

animations = [
    rotation
    # rotation_x,
    # rotation_y,
    # rotation_z
]

run_animations(animations, "Task 11", obj)