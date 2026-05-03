from hw1_2.utils import *
from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.engine.model.Cube import Cube
from src.engine.model.SimplePolygon import SimplePolygon
from src.math.Vec4 import Vec4


obj = SimplePolygon(1, 2, 3,
                    4, 5, 6,
                    7, 8, 9,)

triangle_points = np.array([
        [1, 2, 3, 1],
        [4, 5, 6, 1],
        [7, 8, 9, 1],
    ])

obj.pivot(2, 3, 4)
obj.show_pivot()

pivot = (2, 3, 4)

R = around_point(rot_axis(90, (1, 1, 1)), pivot)
T = translate(0, -1, 2)

tr1 = apply(triangle_points, R)
print_points("Rotation", tr1)

tr2 = apply(triangle_points, compose(R, T))
print_points("Final", tr2)


rotation = RotationAnimation(
    end=np.radians(90),
    axis=Vec4(1, 1, 1),
    channel='object',
)

translation = TranslationAnimation(
    end=Vec4(0, -1, 2),
    channel='object'
)

animations = [
    rotation,
    translation
]

run_animations(animations, "Task 8", obj)