from hw1_2.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec4 import Vec4

obj = Cube(alpha=0.2)

cube = cube_points()

R = rot_axis(45, (1, 1, 0))
T = translate(2, -1, 3)

tr1 = apply(cube, R)
print_points("After rotation", tr1)

tr2 = apply(cube, compose(R, T))
print_points("Final", tr2)

animation_1 = RotationAnimation(
    end=np.radians(45),
    axis=Vec4(1,1,0),
    channel="object",
)

animation_2 = TranslationAnimation(
    end=Vec4(2,-1,3),
    channel="object",
)

run_animations([animation_1, animation_2], "Task 1", obj)