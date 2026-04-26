from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

sq = square()
pivot = [0.5, 0.5]
tr1 = apply(sq, rotate_around(60, pivot=pivot))
print_points("Поворот на 60 навколо (0.5, 0.5)", tr1)

run_task([
    RotationAnimation(end=(60), frames=20, channel=FIGURE_KEY)
], "Task 7", pivot=pivot)
