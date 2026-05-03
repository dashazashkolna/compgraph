from hw1_3.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4

obj = Cube(alpha=0.2)

cube = cube_points()

R = compose(rot_z(50), rot_y(35), rot_x(20))
tr1 = apply(cube, R)
print_points("Rotate", tr1)

T = translate(1, 3, -2)
tr2 = apply(cube, compose(R, T))
print_points("Final", tr2)

animations = [
    RotationAnimation(end=np.radians(50), axis=Vec4(0,0,1), channel="object"),
    RotationAnimation(end=np.radians(35), axis=Vec4(0,1,0), channel="object"),
    RotationAnimation(end=np.radians(20), axis=Vec4(1,0,0), channel="object"),
    TranslationAnimation(end=Vec4(1,3,-2), channel="object")
]

run_animations(animations, "Task 2", obj)