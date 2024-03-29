import open3d as o3d
import numpy as np
import pandas as pd

def slice_and_save_point_clouds(pcd, direction, slice_distance, gap_distance, output_path_pcd, output_path_csv, flag):
    # 将点云转换为NumPy数组
    points = np.asarray(pcd.points)
    
    # 计算每个点在指定方向上的投影长度
    projections = np.dot(points, direction)
    
    # 初始化记录点所属切片和移动后位置的DataFrame
    points_info = pd.DataFrame(columns=['X', 'Y', 'Z', 'Slice_Index', 'Adjusted_X', 'Adjusted_Y', 'Adjusted_Z'])
    
    # 计算切片的开始和结束位置
    min_projection = np.min(projections)
    max_projection = np.max(projections)
    
    # 初始化当前切片的开始位置
    current_slice_start = min_projection
    
    # 切片索引，用于命名文件和记录点所属切片
    slice_index = 0
    
    # 分组切片操作
    while current_slice_start < max_projection:
        # 定位当前切片内的点
        in_slice = np.logical_and(projections >= current_slice_start, projections < current_slice_start + slice_distance)
        slice_points = points[in_slice]
        
        # 调整切片位置以添加间距
        slice_offset = (current_slice_start - min_projection) / slice_distance * gap_distance
        adjusted_slice_points = slice_points + np.array([slice_offset, 0, 0])
        
        if len(adjusted_slice_points) > 0:
            # 更新点信息到DataFrame
            for point, adjusted_point in zip(slice_points, adjusted_slice_points):
                new_row = {
                    'X': point[0], 'Y': point[1], 'Z': point[2], 
                    'Slice_Index': slice_index, 
                    'Adjusted_X': adjusted_point[0], 'Adjusted_Y': adjusted_point[1], 'Adjusted_Z': adjusted_point[2]
                }
                points_info = points_info.append(new_row, ignore_index=True)
            
            # 创建新的点云对象并保存当前切片
            slice_pcd = o3d.geometry.PointCloud()
            slice_pcd.points = o3d.utility.Vector3dVector(adjusted_slice_points)
            file_name = output_path_pcd + f"/slice_{slice_index}.pcd"
            o3d.io.write_point_cloud(file_name, slice_pcd)
            print(f"Saved slice to {file_name}")
        
            # 更新切片索引
            slice_index += 1
        
        # 更新切片的开始位置
        current_slice_start += slice_distance
    
    # 保存记录点所属切片和移动后位置的DataFrame到CSV
    points_info.to_csv(output_path_csv + f"/points_slice_info_plane{flag}.csv", index=False)
    points_info[['Adjusted_X', 'Adjusted_Y', 'Adjusted_Z']].to_csv(output_path_csv + f"/points_adjusted_positions_plane{flag}.csv", index=False)

# 读取点云
#pcd = o3d.io.read_point_cloud("plane3_data_b.pcd")

# 设置方向向量，切片距离和间距
#direction = np.array([1, 0, 0])
#slice_distance = 0.5
#gap_distance = 1

# 进行切片并保存操作
#slice_and_save_point_clouds(pcd, direction, slice_distance, gap_distance)


#还得存入新坐标
