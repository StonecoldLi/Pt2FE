import open3d as o3d
import numpy as np
import os

def calculate_centroids_and_save(input_folder, output_file):
    # 列出文件夹下的所有.pcd文件
    pcd_files = [f for f in os.listdir(input_folder) if f.endswith('.pcd')]
    
    # 初始化一个空列表来存储所有质心
    centroids = []
    
    # 遍历文件夹中的每个.pcd文件
    for pcd_file in pcd_files:
        # 读取点云文件
        pcd_path = os.path.join(input_folder, pcd_file)
        pcd = o3d.io.read_point_cloud(pcd_path)
        
        # 计算当前点云的质心
        centroid = np.mean(np.asarray(pcd.points), axis=0)
        centroids.append(centroid)
    
    # 将质心列表转换为NumPy数组
    centroid_array = np.array(centroids)
    
    # 创建一个新的点云对象，包含所有质心
    centroid_pcd = o3d.geometry.PointCloud()
    centroid_pcd.points = o3d.utility.Vector3dVector(centroid_array)
    
    # 保存包含所有质心的新点云文件
    o3d.io.write_point_cloud(output_file, centroid_pcd)
    print(f"Saved centroid point cloud to {output_file}")


#input_folder = 'plane3_fin'  # 指向含有.pcd文件的文件夹
#output_file = 'plane3_centroids.pcd'  # 质心点云将被保存到这个文件

# 计算质心并保存
#calculate_centroids_and_save(input_folder, output_file)

