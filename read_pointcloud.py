'''
import open3d as o3d
import numpy as np
pcd = o3d.io.read_point_cloud("plane_data_e6.txt", format='xyz')
print(pcd)#输出点云点的个数
print(np.asarray(pcd.points))#输出点的三维坐标
print('给所有的点上一个统一的颜色，颜色是在RGB空间得[0，1]范围内得值')
pcd.paint_uniform_color([0, 0, 1])
o3d.io.write_point_cloud("test.pcd", pcd)
o3d.visualization.draw_geometries([pcd])
'''

import open3d as o3d
import numpy as np

# 读取点云数据
pcd = o3d.io.read_point_cloud("plane_data_e6.txt", format='xyz')

# 创建平面几何体
plane = o3d.geometry.TriangleMesh.create_coordinate_frame(size=40.0)

# 平面方程系数
a, b, c, d = -0.13145762,  0.01110872,  0.99125955, -1.38707248

# 平面点云数据
num_points = 1000
x = np.linspace(50, 50, num_points)
y = np.linspace(50, 50, num_points)
X, Y = np.meshgrid(x, y)
Z = -(a*X + b*Y + d) / c
points = np.column_stack([X.flatten(), Y.flatten(), Z.flatten()])
plane_pcd = o3d.geometry.PointCloud()
plane_pcd.points = o3d.utility.Vector3dVector(points)

# 合并点云数据和平面
merged_pcd = pcd + plane_pcd

# 设置点云数据的统一颜色
merged_pcd.paint_uniform_color([0, 0, 1])

# 保存合并后的点云数据
#o3d.io.write_point_cloud("test.pcd", merged_pcd)

# 可视化合并后的结果
o3d.visualization.draw_geometries([merged_pcd])
