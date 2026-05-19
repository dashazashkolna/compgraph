import numpy as np

from src.engine.scene.AnimatedScene import AnimatedScene
from src.engine.model.Cube import Cube


def create_scene(title, model, key="object",
                 image_size=(8, 8),
                 coordinate_rect=(-2, -2, -2, 3, 3, 3)):

    scene = AnimatedScene(
        title=title,
        image_size=image_size,
        coordinate_rect=coordinate_rect,
    )

    scene[key] = model
    return scene


def run_animations(animations, title, model, key="object"):
    scene = create_scene(title, model, key)
    scene.add_animations(*animations)
    scene.show()


def quat_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2

    return np.array([
        w1*w2 - x1*x2 - y1*y2 - z1*z2,
        w1*x2 + x1*w2 + y1*z2 - z1*y2,
        w1*y2 - x1*z2 + y1*w2 + z1*x2,
        w1*z2 + x1*y2 - y1*x2 + z1*w2
    ])


def quat_from_axis(axis, deg):
    theta = np.radians(deg)
    axis = axis / np.linalg.norm(axis)

    w = np.cos(theta/2)
    x,y,z = axis*np.sin(theta/2)

    return np.array([w,x,y,z])


def matrix_to_quaternion(R):
    tr = np.trace(R)

    if tr > 0:
        S = np.sqrt(tr + 1.0) * 2
        w = 0.25 * S
        x = (R[2,1] - R[1,2]) / S
        y = (R[0,2] - R[2,0]) / S
        z = (R[1,0] - R[0,1]) / S
    else:
        w = 1
        x = y = z = 0

    return np.array([w,x,y,z])
