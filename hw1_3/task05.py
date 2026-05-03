from hw1_3.utils import *
from src.engine.model.Cube import Cube
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.scene.AnimatedScene import AnimatedScene
from src.math.Vec4 import Vec4
import numpy as np

cube = cube_points()

R_int_1 = rot_x(30) @ rot_y(90) @ rot_z(45)
tr_int_1 = apply(cube, R_int_1)
print_points("Internal original (30,90,45)", tr_int_1)

R_int_2 = rot_x(40) @ rot_y(90) @ rot_z(35)
tr_int_2 = apply(cube, R_int_2)
print_points("Internal modified (40,90,35)", tr_int_2)

print("Same result:", np.allclose(tr_int_1, tr_int_2))

obj = Cube(alpha=0.5, color=(1, 0, 0))
obj.show_local_frame()
obj_ref = Cube(alpha=0.3, color=(0, 0, 1))
obj_ref.transformation = R_int_2

angle_x = 40
angle_y = 90
angle_z = 35

OX = Vec4(1, 0, 0)
OY = Vec4(0, 1, 0)
OZ = Vec4(0, 0, 1)

Rx = rot_x(angle_x)

animation_x = RotationAnimation(
    end=np.radians(angle_x),
    axis=OX,
    channel="cube",
)

OY1 = apply(np.array([[OY.x, OY.y, OY.z, 0]]), Rx)[0][:3]
OY1 = Vec4(OY1[0], OY1[1], OY1[2])

animation_y = RotationAnimation(
    end=np.radians(angle_y),
    axis=OY1,
    channel="cube",
)

rot_y = rot_axis(angle_y, (OY1.x, OY1.y, OY1.z))
OZ1 = apply(np.array([[OZ.x, OZ.y, OZ.z, 0]]), rot_x(angle_x))[0][:3]
OZ2 = apply(np.array([[OZ1[0], OZ1[1], OZ1[2], 0]]), rot_y)[0][:3]
OZ2 = Vec4(OZ2[0], OZ2[1], OZ2[2])

animation_z = RotationAnimation(
    end=np.radians(angle_z),
    axis=OZ2,
    channel="cube",
)

scene = AnimatedScene(
    title="Task 5",
    image_size=(10, 10),
    coordinate_rect=(-2, -2, -2, 3, 3, 3),
)

scene["cube"] = obj
scene["ref_cube"] = obj_ref

scene.add_animations(animation_x, animation_y, animation_z)
scene.show()