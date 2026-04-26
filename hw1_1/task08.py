from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

sq = square()
pivot = [0.5, 0.5]
tr1 = apply(sq, scale_around(2, 3, pivot))
print_points('Розтяг по x x2 і по y x3 відносно (0.5, 0.5)', tr1)

run_task([
    ScaleAnimation(end=(2, 3), frames=20, channel=FIGURE_KEY),
], "Task 8", pivot=pivot)
