from hw1_2.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4

obj = Cube(alpha=0.2)
obj.pivot(1, 1, 1)
obj.show_pivot()

cube = cube_points()
pivot = (1, 1, 1)

S = around_point(scale(2, 1, 1), pivot)
tr1 = apply(cube, S)
print_points("Scale", tr1)

R = around_point(rot_axis(45, (0,1,0)), pivot)
tr2 = apply(cube, compose(S, R))
print_points("Scale + Rotate", tr2)

T = translate(-3, 4, 2)
tr3 = apply(cube, compose(S, R, T))
print_points("Final", tr3)

scale_anim = ScaleAnimation(
    end=Vec4(2, 1, 1),
    channel="object",
)

rotation = RotationAnimation(
    end=np.radians(45),
    axis=Vec4(0, 1, 0),
    channel="object",
)

translation = TranslationAnimation(
    end=Vec4(-3, 4, 2),
    channel="object",
)

animations = [
    scale_anim,
    rotation,
    translation
]

run_animations(animations, "Task 10", obj)