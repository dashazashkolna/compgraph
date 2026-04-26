from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

sq = square()
pivot = [0.5, 0.5]
tr11 = apply(sq, scale_around(2, 2, pivot))
tr12 = apply(tr11, rotate_around(30, pivot=pivot))
tr13 = apply(tr12, translate(1, -1))
print_points('Розтяг + поворот + переміщення', tr13)

tr21 = apply(sq, translate(1, -1))
tr22 = apply(tr21, scale_around(2, 2, pivot))
tr23 = apply(tr22, rotate_around(30, pivot=pivot))
print_points('Переміщення + розтяг + поворот', tr23)

tr31 = apply(sq, scale_around(2, 2, pivot))
tr32 = apply(tr31, translate(1, -1))
tr33 = apply(tr32, rotate_around(30, pivot=pivot))
print_points('Розтяг + переміщення + поворот', tr33)

run_task([
    ScaleAnimation(end=(2, 2), frames=20, channel=FIGURE_KEY),
    RotationAnimation(30, frames=20, channel=FIGURE_KEY),
    TranslationAnimation(vertex(1, -1), frames=20, channel=FIGURE_KEY),
], "Task 10", pivot=pivot)
