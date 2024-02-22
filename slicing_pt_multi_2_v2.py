import open3d as o3d
import numpy as np
import os
import pandas as pd

def slice_save_and_add_gap_to_point_cloud(pcd, direction, slice_distance, gap_distance, output_folder, file_prefix):
    points = np.asarray(pcd.points)
    projections = np.dot(points, direction)
    min_projection = np.min(projections)
    max_projection = np.max(projections)
    current_slice_start = min_projection
    slice_index = 0
    total_gap = 0
    os.makedirs(output_folder, exist_ok=True)

    while current_slice_start < max_projection:
        in_slice = np.logical_and(projections >= current_slice_start, projections < current_slice_start + slice_distance)
        slice_points = points[in_slice]
        
        if len(slice_points) > 0:
            adjusted_slice_points = slice_points + total_gap * direction
            
            # 创建新的点云对象并保存
            slice_pcd = o3d.geometry.PointCloud()
            slice_pcd.points = o3d.utility.Vector3dVector(adjusted_slice_points)
            slice_filename = os.path.join(output_folder, f"{file_prefix}_slice_with_gap_{slice_index:03d}.pcd")
            o3d.io.write_point_cloud(slice_filename, slice_pcd)
            print(f"Saved {slice_filename}")
            
            # 创建DataFrame来保存点的信息
            slice_df = pd.DataFrame(slice_points, columns=['Original_X', 'Original_Y', 'Original_Z'])
            slice_df['Adjusted_X'] = adjusted_slice_points[:, 0]
            slice_df['Adjusted_Y'] = adjusted_slice_points[:, 1]
            slice_df['Adjusted_Z'] = adjusted_slice_points[:, 2]
            slice_df['Slice_Index'] = slice_index
            
            # 保存DataFrame为CSV文件
            slice_csv_filename = os.path.join(output_folder+'/info/', f"{file_prefix}_slice_with_gap_{slice_index:03d}.csv")
            slice_df.to_csv(slice_csv_filename, index=False)
            print(f"Saved slice data to {slice_csv_filename}")

            total_gap += gap_distance
        
        current_slice_start += slice_distance
        slice_index += 1

def process_folder(input_folder, direction, slice_distance, gap_distance, output_folder):
    pcd_files = [f for f in os.listdir(input_folder) if f.endswith('.pcd')]
    
    for pcd_file in pcd_files:
        file_path = os.path.join(input_folder, pcd_file)
        pcd = o3d.io.read_point_cloud(file_path)
        file_prefix = os.path.splitext(pcd_file)[0]
        slice_save_and_add_gap_to_point_cloud(pcd, direction, slice_distance, gap_distance, output_folder, file_prefix)

# 示例用法
input_folder = './data_slicing/plane3_org'  # 输入文件夹路径
output_folder = './data_slicing/plane3_split'  # 输出文件夹路径
direction = np.array([0, 0, 1])  # 切片方向
slice_distance = 0.5  # 切片间距
gap_distance = 1  # 切片间隙

process_folder(input_folder, direction, slice_distance, gap_distance, output_folder)
