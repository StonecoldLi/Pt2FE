import open3d as o3d
import numpy as np

# 加载PCD文件
pcd = o3d.io.read_point_cloud("./data_slicing/centroid_5/plane3_centroids.pcd")

# 获取点云中所有点的坐标
points = np.asarray(pcd.points)

# 计算x, y, z坐标的最大值
max_x = np.max(points[:, 0])
max_y = np.max(points[:, 1])
max_z = np.max(points[:, 2])

print(f"Max X: {max_x}")
print(f"Max Y: {max_y}")
print(f"Max Z: {max_z}")
