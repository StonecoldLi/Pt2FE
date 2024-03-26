import open3d as o3d
import numpy as np


def dist(point, a, b, c, d):
    """
    计算点到平面的距离
    :param point: 平面外一点
    :param a: 平面方程系数a
    :param b: 平面方程系数b
    :param c: 平面方程系数c
    :param d: 平面方程系数d
    :return:  点到平面的距离
    """
    dis = abs(a * point[0] + b * point[1] + c *
              point[2] - d) / np.sqrt(a ** 2 + b ** 2 + c ** 2)
    return dis


# -------------------------------加载点云---------------------------------
pcd = o3d.io.read_point_cloud("data_e6_b.pcd")

# -----------------------------获取平面参数-------------------------------
a,b,c,d = -0.02236471, -0.73981471,  0.67243886,  0.63011034

print(f"Plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = 0")
pt = np.asarray([14.5999802,5.314893315,6.3106190280000005])  # 平面外一点
# ---------------------------计算点到平面的距离----------------------------
p2p_dis = dist(pt, a, b, c, d)
print("点到平面的距离为:", p2p_dis)

