from hw1_2.utils import *
import numpy as np
from src.math.utils_matrix import decompose_affine_2
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Tetrahedron import Tetrahedron
from src.math.Vec4 import Vec4


obj = Tetrahedron(alpha=0.2)

tetra = tetra_points()

M = np.eye(4)

M = M @ rot_x(45)
tr1 = apply(tetra, M)
print_points("Step 1 (rotate X local)", tr1)

rot1 = RotationAnimation(
    end=np.radians(45),
    axis=Vec4(1, 0, 0),
    channel="object",
)

local_y = M[:3, 1]

T_local = translate(local_y[0]*2, local_y[1]*2, local_y[2]*2)

M = M @ T_local
tr2 = apply(tetra, M)
print_points("Step 2 (move along local Y)", tr2)

translation_vector = M[:3, 3]

translation = TranslationAnimation(
    end=Vec4(translation_vector[0], translation_vector[1], translation_vector[2], 0),
    channel="object",

)

local_z = M[:3, 2]

R_local_z = rot_axis(30, local_z)

M = M @ R_local_z
tr3 = apply(tetra, M)
print_points("Step 3 (rotate around local Z)", tr3)

_, R_final, _, rot_axis_final, rot_angle = decompose_affine_2(R_local_z)


rot2 = RotationAnimation(
    end=np.radians(30),
    axis=Vec4(local_z[0], local_z[1], local_z[2], 0),
    channel="object",
)

animations = [
    rot1,
    translation,
    rot2
]

run_animations(animations, "Task 13", obj)