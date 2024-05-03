import os
import re
import numpy as np
import open3d as o3d

def translate_and_save_centroids(input_folder, output_folder, vector1, vector2):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 正则表达式匹配文件名中的数字
    pattern = re.compile(r'slice_(\d+)_slice_with_gap_(\d+)_centroid.pcd')
    
    # 遍历输入文件夹中的所有.pcd文件
    for filename in os.listdir(input_folder):
        match = pattern.match(filename)
        if match:
            N = int(match.group(1))
            NNN = int(match.group(2))
            
            # 读取点云文件
            file_path = os.path.join(input_folder, filename)
            pcd = o3d.io.read_point_cloud(file_path)
            
            # 计算移动距离
            move_distance1 = np.array(vector1) * NNN
            move_distance2 = np.array(vector2) * N
            
            # 应用平移
            pcd.translate(move_distance1)
            pcd.translate(move_distance2)
            
            # 保存处理后的文件
            new_filename = filename.replace('.pcd', '_adjust.pcd')
            output_path = os.path.join(output_folder, new_filename)
            o3d.io.write_point_cloud(output_path, pcd)
            print(f"Processed and saved {output_path}")