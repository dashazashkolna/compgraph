from hw1_2.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4

obj = Cube(alpha=0.2)

cube = cube_points()

angle_z, angle_y, angle_x = 20, 35, 50

OX = Vec4(1, 0, 0)
OY = Vec4(0, 1, 0)
OZ = Vec4(0, 0, 1)

R = euler_zyx(angle_z, angle_y, angle_x)
T = translate(1, 3, -2)

tr1 = apply(cube, R)
print_points("Rotate", tr1)

tr2 = apply(cube, compose(R, T))
print_points("Final", tr2)

rotation_z = RotationAnimation(
    end=np.radians(50),
    axis=Vec4(0, 0, 1),
    channel="object",
)

rotation_y = RotationAnimation(
    end=np.radians(35),
    axis=Vec4(0, 1, 0),
    channel="object",
)

rotation_x = RotationAnimation(
    end=np.radians(20),
    axis=Vec4(1, 0, 0),
    channel="object",
)

translation = TranslationAnimation(
    end=Vec4(1, 3, -2),
    channel="object",
)

animations = [
    rotation_z,
    rotation_y,
    rotation_x,
    translation
]

run_animations(animations, "Task 4", obj)