from hw1_2.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4


obj = Cube(alpha=0.2)

cube = cube_points()

angle_x, angle_y, angle_z = 30, 45, 60

OX = Vec4(1, 0, 0)
OY = Vec4(0, 1, 0)
OZ = Vec4(0, 0, 1)

S = scale(2, 0.5, 1)
R = euler_xyz(angle_x, angle_y, angle_y)
T = translate(-3, 2, 5)

tr1 = apply(cube, S)
print_points("Scale", tr1)

tr2 = apply(cube, compose(S, R))
print_points("Scale + Rotate", tr2)

tr3 = apply(cube, compose(S, R, T))
print_points("Final", tr3)

scaling = ScaleAnimation(
    end=Vec4(2, 0.5, 1),
    channel="object",
)

rotation_x = RotationAnimation(
    end=np.radians(angle_x),
    axis=OX,
    channel="object",
)

rotation_y = RotationAnimation(
    end=np.radians(angle_y),
    axis=OY,
    channel="object",
)

rotation_z = RotationAnimation(
    end=np.radians(angle_z),
    axis=OZ,
    channel="object",
)

translation = TranslationAnimation(
    end=Vec4(2, -1, 3),
    channel="object",
)

animations = [
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
    translation
]

run_animations(animations, "Task 2", obj)