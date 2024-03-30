#生成每部分的点云数据组
import pandas as pd
import numpy as np
import open3d as o3d

def save_groups_to_pcd(csv_file_path, output_path):
    # 读取CSV文件
    df = pd.read_csv(csv_file_path)
    
    # 按照a, b列的值进行分组
    grouped = df.groupby(['Slice_Index_1', 'Slice_Index_2'])
    
    for (a, b), group in grouped:
        # 提取每组的x, y, z列作为点云数据
        points = group[['X', 'Y', 'Z']].values
        # 创建一个Point Cloud对象
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)
        
        # 保存点云到PCD文件
        pcd_file_name = output_path + f"/points_group_{a}_{b}.pcd"
        o3d.io.write_point_cloud(pcd_file_name, pcd)
        print(f"Saved {pcd_file_name} with {len(points)} points.")

# 示例用法
#csv_file_path = 'file_fin_plane3.csv'  # 替换为实际的文件路径
#save_groups_to_pcd(csv_file_path)
