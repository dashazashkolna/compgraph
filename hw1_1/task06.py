from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

sq = square()
tr1 = apply(sq, scale(1, 3))
tr2 = apply(tr1, rotate(60))
tr3 = apply(tr2, translate(2, 3))
print_points('Розтяг + поворот + перенесення', tr3)
tr4 = apply(sq, translate(2, 3))
tr5 = apply(tr4, scale(1, 3))
tr6 = apply(tr5, rotate(60))
print_points('Перенесення + розтяг + поворот', tr6)

run_task([
    ScaleAnimation(end=(1, 3), frames=20, channel=FIGURE_KEY),
    RotationAnimation(end=(60), frames=20, channel=FIGURE_KEY),
    TranslationAnimation(vertex(2, 3), frames=20, channel=FIGURE_KEY),
], "Task 6")
