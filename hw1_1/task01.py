from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

sq = square()
tr1 = apply(sq, rotate(30))
print_points('Поворот на 30', tr1)
tr2 = apply(tr1, translate(2, 3))
print_points('Переміщення на вектор (2, 3)', tr2)

run_task([
    RotationAnimation(end=30, frames=20, channel=FIGURE_KEY),
    TranslationAnimation(end=vertex(2, 3), frames=20, channel=FIGURE_KEY)
], "Task 1")
