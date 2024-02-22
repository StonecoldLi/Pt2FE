import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cross_product(v1, v2):
    return np.cross(v1, v2)

def find_intersection_point(plane1, plane2, direction):
    # 为了找到交线上的一个点，我们需要解决一个由两个平面方程和一个额外条件构成的系统
    # 该额外条件可以是沿着交线方向的一个点，我们可以设置x=0（如果方向向量的x分量不为0）
    # 或者设置y=0或z=0，取决于方向向量的非零分量
    n1 = np.array(plane1[:3])
    n2 = np.array(plane2[:3])
    
    # 选择一个额外的方程以保证系统有唯一解
    if direction[0] != 0:
        A = np.array([n1, n2, [1, 0, 0]])
    elif direction[1] != 0:
        A = np.array([n1, n2, [0, 1, 0]])
    else:
        A = np.array([n1, n2, [0, 0, 1]])
    
    b = np.array([-plane1[3], -plane2[3], 0])
    
    point = np.linalg.solve(A, b)
    return point

def plot_planes_and_line(plane1, plane2, line_direction, point_on_line):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Generate meshgrid for the plane drawing
    xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
    zz1 = (-plane1[3] - plane1[0] * xx - plane1[1] * yy) / plane1[2]
    zz2 = (-plane2[3] - plane2[0] * xx - plane2[1] * yy) / plane2[2]

    # Draw the planes
    ax.plot_surface(xx, yy, zz1, alpha=0.5, rstride=100, cstride=100, color='y', edgecolor='none')
    ax.plot_surface(xx, yy, zz2, alpha=0.5, rstride=100, cstride=100, color='c', edgecolor='none')

    # Calculate and draw the line of intersection
    line_points = np.array([point_on_line + t * line_direction for t in np.linspace(-10, 10, 2)])
    ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], color='red', linewidth=2)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Example plane coefficients
plane1 = [1.53677273e-04, -9.50453435e-01,  3.10866924e-01,  3.23398910e+00]
plane2 = [-3.49946945e-12, -2.20672290e-12,  1.00000000e+00, -1.96635929e-02]
plane3 = [1.13386453e-06, -9.47393334e-01, -3.20071664e-01, -2.87827417e+00]

# direction = cross_product(np.array(plane3[:3]), np.array(plane2[:3]))
# point_on_line = find_intersection_point(plane3, plane2, direction)

# plot_planes_and_line(plane3, plane2, direction, point_on_line)

#surface1 & surface2
direction1 = cross_product(np.array(plane1[:3]), np.array(plane2[:3]))
point_on_line1 = find_intersection_point(plane1, plane2, direction1)
print("平面1和平面2的交线方向向量：",direction1)
print("平面1和平面2的交线上的一点：",point_on_line1)
plot_planes_and_line(plane1, plane2, direction1, point_on_line1)

#surface2 & surface3
direction3 = cross_product(np.array(plane3[:3]), np.array(plane2[:3]))
point_on_line3 = find_intersection_point(plane3, plane2, direction3)
print("平面3和平面2的交线方向向量：",direction3)
print("平面3和平面2的交线上的一点：",point_on_line3)
plot_planes_and_line(plane3, plane2, direction3, point_on_line3)
