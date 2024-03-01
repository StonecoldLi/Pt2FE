import open3d as o3d
import numpy as np

def project_points(points, direction):
    """计算点在指定方向上的投影长度"""
    direction_normalized = direction / np.linalg.norm(direction)
    projection_lengths = np.dot(points, direction_normalized)
    return projection_lengths

def remove_gaps_from_pcd_custom_direction(pcd, gap_distance, direction):
    # 将点云转换为NumPy数组
    points = np.asarray(pcd.points)
    
    # 计算点在自定义方向上的投影
    projection_lengths = project_points(points, direction)
    
    # 按投影长度进行排序
    sorted_indices = np.argsort(projection_lengths)
    sorted_points = points[sorted_indices]
    sorted_projection_lengths = projection_lengths[sorted_indices]
    
    # 初始化调整后的点集
    adjusted_points = sorted_points.copy()
    last_projection_length = sorted_projection_lengths[0]
    accumulated_gap = 0
    
    # 遍历所有点，根据投影长度差距移除间隔
    for i in range(1, len(sorted_points)):
        current_projection_length = sorted_projection_lengths[i]
        if current_projection_length - last_projection_length > gap_distance:
            accumulated_gap += gap_distance
        adjustment = accumulated_gap * direction / np.linalg.norm(direction)
        adjusted_points[i] -= adjustment
        last_projection_length = current_projection_length
    
    # 创建新的点云对象
    adjusted_pcd = o3d.geometry.PointCloud()
    adjusted_pcd.points = o3d.utility.Vector3dVector(adjusted_points)
    
    return adjusted_pcd

# 示例：自定义方向向量
direction = np.array([1, 0, 0])  # 自定义方向，例如(1, 0, 0)

# 读取包含间隔的点云文件
#pcd = o3d.io.read_point_cloud("./data_slicing/plane1_centroids.pcd")  # 调整文件名以匹配实际情况
pcd = o3d.io.read_point_cloud("plane1_test.pcd")

# 移除间隔
adjusted_pcd = remove_gaps_from_pcd_custom_direction(pcd, gap_distance=1, direction=direction)

# 保存调整后的点云为新的PCD文件
o3d.io.write_point_cloud("plane1_test2.pcd", adjusted_pcd)
