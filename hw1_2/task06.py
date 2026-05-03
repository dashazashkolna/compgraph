from hw1_2.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.model.Cube import Cube
from src.math.Vec4 import Vec4

obj = Cube(alpha=0.2)
obj.pivot(2, 0, 3)
obj.show_pivot()

cube = cube_points()

pivot = (2, 0, 3)

R = around_point(rot_axis(45, (0,1,0)), pivot)
T = translate(-1, 2, 4)

tr1 = apply(cube, R)
print_points("Rotate around pivot", tr1)

tr2 = apply(cube, compose(R, T))
print_points("Final", tr2)

rotation = RotationAnimation(
    end=np.radians(45),
    axis=Vec4(0, 1, 0),
    channel='object',
)

translation = TranslationAnimation(
    end=Vec4(-1, 2, 4),
    channel="object",
)

animations = [
    rotation,
    translation
]

run_animations(animations, "Task 6", obj)