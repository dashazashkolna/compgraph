from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

TRS = np.array([
        [1.732, -1, 5],
        [1, 1.732, -3],
        [0, 0, 1]
    ])

pivot = [1, 1]

res = decompose_trs_with_pivot(TRS, pivot)

run_task([
    TranslationAnimation(end=res[0], frames=20, channel=FIGURE_KEY),
    RotationAnimation(end=res[1], frames=20, channel=FIGURE_KEY),
    ScaleAnimation(end=res[2], frames=20, channel=FIGURE_KEY),
], "Task 14", pivot=pivot)