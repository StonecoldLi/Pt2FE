import open3d as o3d
import numpy as np

def slice_and_merge_point_cloud(pcd, direction, slice_distance, gap_distance):
    # 将点云转换为NumPy数组
    points = np.asarray(pcd.points)
    
    # 计算每个点在指定方向上的投影长度
    projections = np.dot(points, direction)
    
    # 计算切片的开始和结束位置
    min_projection = np.min(projections)
    max_projection = np.max(projections)
    
    # 初始化当前切片的开始位置
    current_slice_start = min_projection
    
    # 存储合并后的所有切片点
    merged_points = []
    
    # 分组切片操作
    while current_slice_start < max_projection:
        # 定位当前切片内的点
        in_slice = np.logical_and(projections >= current_slice_start, projections < current_slice_start + slice_distance)
        slice_points = points[in_slice]
        
        # 调整切片位置以添加间距
        slice_offset = (current_slice_start - min_projection) / slice_distance * gap_distance
        adjusted_slice_points = slice_points + np.array([slice_offset, 0, 0])
        
        # 将调整后的切片点添加到合并列表中
        merged_points.append(adjusted_slice_points)
        
        # 更新切片的开始位置
        current_slice_start += slice_distance
    
    # 合并所有切片为一个点云
    merged_points = np.vstack(merged_points)
    merged_pcd = o3d.geometry.PointCloud()
    merged_pcd.points = o3d.utility.Vector3dVector(merged_points)
    
    return merged_pcd

# 读取点云
pcd = o3d.io.read_point_cloud("plane3_data_b.pcd")

# 设置方向向量，切片距离和间距
direction = np.array([1, 0, 0])
slice_distance = 0.05
gap_distance = 0.1

# 进行切片合并操作
merged_pcd = slice_and_merge_point_cloud(pcd, direction, slice_distance, gap_distance)

# 保存合并后的点云为一个PCD文件
o3d.io.write_point_cloud("merged_slices.pcd", merged_pcd)

