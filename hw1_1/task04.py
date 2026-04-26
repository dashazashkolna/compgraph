from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

sq = square()
tr1 = apply(sq, scale(3, 3))
print_points('Розтяг х3', tr1)
tr2 = apply(tr1, rotate(60))
print_points('Поворот на 60', tr2)

run_task([
    ScaleAnimation(end=(3, 3), frames=20, channel=FIGURE_KEY),
    RotationAnimation(end=60, frames=20, channel=FIGURE_KEY)
], "Task 4")
