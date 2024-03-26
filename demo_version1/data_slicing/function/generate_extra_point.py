import numpy as np
import open3d as o3d
# 起始点
start_point = np.array([0,3.40900642,0.01966359])
# 方向向量
direction = np.array([1, 0, 0])
# 归一化方向向量
direction_normalized = direction / np.linalg.norm(direction)
# 设定p_max的值
p_max = 17  # 假设值，根据需要调整
# 每隔0.5的距离
distance = 0.5

# 计算点的序列
points = []
current_point = start_point
while current_point[0] <= p_max:
    points.append(current_point)
    current_point = current_point + direction_normalized * distance

points_array = np.array(points)
#print(points)

# 创建点云对象
point_cloud = o3d.geometry.PointCloud()

# 将NumPy数组中的点添加到点云中
point_cloud.points = o3d.utility.Vector3dVector(points_array)

# 保存点云到PCD文件
o3d.io.write_point_cloud("extra_plane1.pcd", point_cloud, write_ascii=False)
