from hw1_2.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4

obj = Cube(alpha=0.2)

cube = cube_points()

R1 = rot_axis(60, (0, 0, 1))
R2 = rot_axis(45, (1, 1, 1))
T = translate(4, -2, 1)

tr1 = apply(cube, R1)
print_points("Rotation Z", tr1)

tr2 = apply(cube, compose(R1, R2))
print_points("Rotation (1, 1, 1)", tr2)

tr3 = apply(cube, compose(R1, R2, T))
print_points("Final", tr3)

rotation_1 = RotationAnimation(
    end=np.radians(60),
    axis=Vec4(0, 0, 1),
    channel="object",
)

rotation_2 = RotationAnimation(
    end=np.radians(45),
    axis=Vec4(1, 1, 1),
    channel="object",
)

translation = TranslationAnimation(
    end=Vec4(4, -2, 1),
    channel="object",
)

animations = [
    rotation_1,
    rotation_2,
    translation
]

run_animations(animations, "Task 3", obj)