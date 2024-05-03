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


def compute_and_save_centroids(input_folder, output_folder):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.pcd'):
            file_path = os.path.join(input_folder, filename)
            # 读取点云文件
            pcd = o3d.io.read_point_cloud(file_path)
            # 计算质心
            points = np.asarray(pcd.points)
            centroid = np.mean(points, axis=0)
            # 创建新的点云对象并设置质心为唯一的点
            centroid_pcd = o3d.geometry.PointCloud()
            centroid_pcd.points = o3d.utility.Vector3dVector([centroid])
            # 构造输出文件名并保存
            centroid_filename = filename.replace('.pcd', '_centroid.pcd')
            output_path = os.path.join(output_folder, centroid_filename)
            o3d.io.write_point_cloud(output_path, centroid_pcd)
            print(f"Saved centroid to {output_path}")

# 使用示例
# compute_and_save_centroids('path_to_input_folder', 'path_to_output_folder')

