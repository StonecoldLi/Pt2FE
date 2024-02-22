import open3d as o3d
import numpy as np
import os

def slice_save_and_add_gap_to_point_cloud(pcd, direction, slice_distance, gap_distance, output_folder, file_prefix):
    # 将点云转换为NumPy数组
    points = np.asarray(pcd.points)
    
    # 计算每个点在指定方向上的投影长度
    projections = np.dot(points, direction)
    
    # 计算切片的开始和结束位置
    min_projection = np.min(projections)
    max_projection = np.max(projections)
    
    # 初始化当前切片的开始位置
    current_slice_start = min_projection
    slice_index = 0  # 用于命名每个切片文件
    total_gap = 0  # 累计间隔，用于偏移
    
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 分组切片操作
    while current_slice_start < max_projection:
        # 定位当前切片内的点
        in_slice = np.logical_and(projections >= current_slice_start, projections < current_slice_start + slice_distance)
        slice_points = points[in_slice]
        
        if len(slice_points) > 0:  # 确保切片中有点
            # 根据累计间隔对切片点进行偏移
            adjusted_slice_points = slice_points + total_gap * direction
            
            # 创建调整后切片的点云对象
            slice_pcd = o3d.geometry.PointCloud()
            slice_pcd.points = o3d.utility.Vector3dVector(adjusted_slice_points)
            
            # 保存调整后的切片为PCD文件
            slice_filename = os.path.join(output_folder, f"{file_prefix}_slice_with_gap_{slice_index:03d}.pcd")
            o3d.io.write_point_cloud(slice_filename, slice_pcd)
            print(f"Saved {slice_filename}")
            
            # 更新总间隔
            total_gap += gap_distance
        
        # 更新切片的开始位置和索引
        current_slice_start += slice_distance
        slice_index += 1

def process_folder(input_folder, direction, slice_distance, gap_distance, output_folder):
    # 列出文件夹下的所有.pcd文件
    pcd_files = [f for f in os.listdir(input_folder) if f.endswith('.pcd')]
    
    # 遍历并处理每个.pcd文件
    for pcd_file in pcd_files:
        file_path = os.path.join(input_folder, pcd_file)
        pcd = o3d.io.read_point_cloud(file_path)
        
        # 文件前缀使用原始文件名
        file_prefix = os.path.splitext(pcd_file)[0]
        
        # 进行切片，添加间隔，并保存为独立的PCD文件
        slice_save_and_add_gap_to_point_cloud(pcd, direction, slice_distance, gap_distance, output_folder, file_prefix)

# 示例用法
input_folder = './data_slicing/plane1_org'  # 指向含有.pcd文件的文件夹
output_folder = './data_slicing/plane1_split'  # 所有处理后的文件将保存在这个文件夹下
direction = np.array([0, 0, 1])  
slice_distance = 1  # 切片间的距离
gap_distance = 1.0  # 每个切片之间的间隔距离

# 对文件夹内的每个.pcd文件进行操作，并将结果保存到一个总文件夹下
process_folder(input_folder, direction, slice_distance, gap_distance, output_folder)
