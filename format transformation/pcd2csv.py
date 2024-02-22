import open3d as o3d
import pandas as pd
import numpy as np

def pcd_to_csv(pcd_file_path, csv_file_path):
    # 读取.pcd文件
    pcd = o3d.io.read_point_cloud(pcd_file_path)
    
    # 将点云数据转换为numpy数组
    points = np.asarray(pcd.points)
    
    # 创建一个DataFrame
    df = pd.DataFrame(points, columns=['x', 'y', 'z'])
    
    # 保存DataFrame到.csv文件
    df.to_csv(csv_file_path, index=False)
    print(f"Saved point cloud data to {csv_file_path}")
# 示例用法
pcd_file_path = '../data_slicing/centroid_5/plane1_centroids.pcd'  # .pcd文件的路径
csv_file_path = '../data_slicing/plane1.csv'  # 输出的.csv文件路径
pcd_to_csv(pcd_file_path, csv_file_path)
