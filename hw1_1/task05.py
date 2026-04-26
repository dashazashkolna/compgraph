from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

sq = square()
tr1 = apply(sq, translate(1, -1))
print_points('Переміщення на (1, -1)', tr1)
tr2 = apply(tr1, scale(2, 2))
print_points('Розтяг х2', tr2)

run_task([
    TranslationAnimation(vertex(1, -1), frames=20, channel=FIGURE_KEY),
    ScaleAnimation(end=(2, 2), frames=20, channel=FIGURE_KEY,),
], "Task 5")
