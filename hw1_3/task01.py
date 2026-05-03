from hw1_3.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4

obj = Cube(alpha=0.2)

cube = cube_points()

S = scale(2, 0.5, 1)
tr1 = apply(cube, S)
print_points("Scale", tr1)

R = compose(rot_x(30), rot_y(45), rot_z(60))
tr2 = apply(cube, compose(S, R))
print_points("Scale + Rotate", tr2)

T = translate(-3, 2, 5)
tr3 = apply(cube, compose(S, R, T))
print_points("Final", tr3)

animations = [
    ScaleAnimation(end=Vec4(2,0.5,1), channel="object"),
    RotationAnimation(end=np.radians(30), axis=Vec4(1,0,0), channel="object"),
    RotationAnimation(end=np.radians(45), axis=Vec4(0,1,0), channel="object"),
    RotationAnimation(end=np.radians(60), axis=Vec4(0,0,1), channel="object"),
    TranslationAnimation(end=Vec4(-3,2,5), channel="object")
]

run_animations(animations, "Task 1", obj)