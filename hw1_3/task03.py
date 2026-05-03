from hw1_3.utils import *

cube = cube_points()

R_xyz = compose(rot_x(45), rot_y(30), rot_z(60))
R_zyx = compose(rot_z(60), rot_y(30), rot_x(45))

print("XYZ:\n", R_xyz)
print("ZYX:\n", R_zyx)

tr_xyz = apply(cube, R_xyz)
tr_zyx = apply(cube, R_zyx)

print_points("XYZ result", tr_xyz)
print_points("ZYX result", tr_zyx)