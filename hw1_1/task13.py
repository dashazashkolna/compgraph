from hw1_1.utils import *

from src.engine.animation.RotationAnimation import RotationAnimation
from src.engine.animation.TranslationAnimation import TranslationAnimation
from src.engine.animation.ScaleAnimation import ScaleAnimation
from src.math.Vec3 import vertex

FIGURE_KEY = "rect"

TRS = np.array([
        [1.414, -2.121, 1.000],
        [1.414, 2.121, 1.000],
        [0.0, 0.0, 1.0]
    ])

res = decompose_trs(TRS)

run_task([
    TranslationAnimation(end=res[0], frames=20, channel=FIGURE_KEY),
    RotationAnimation(end=res[1], frames=20, channel=FIGURE_KEY),
    ScaleAnimation(end=res[2], frames=20, channel=FIGURE_KEY),
], "Task 13")