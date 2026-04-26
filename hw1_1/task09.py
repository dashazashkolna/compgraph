from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

sq = square()
pivot = [1, 1]
tr1 = apply(sq, scale_around(2, 1, pivot))
tr2 = apply(tr1, translate(3, -2))
print_points('Розтяг + переміщення', tr2)
tr3 = apply(sq, translate(3, -2))
tr4 = apply(tr3, scale_around(2, 1, pivot))
print_points('Переміщення + розтяг', tr4)

run_task([
    ScaleAnimation(end=(2, 1), frames=20, channel=FIGURE_KEY),
    TranslationAnimation(vertex(3, -2), frames=20, channel=FIGURE_KEY),
], "Task 9", pivot=pivot)