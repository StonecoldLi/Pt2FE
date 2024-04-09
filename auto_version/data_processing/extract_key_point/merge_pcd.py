import open3d as o3d
import os

def merge_pcd_files(pcd_files_directory, output_pcd_file):
    # 初始化一个空的点云对象，用于累加合并
    merged_pcd = o3d.geometry.PointCloud()
    
    # 遍历指定目录下的所有.pcd文件
    for filename in os.listdir(pcd_files_directory):
        if filename.endswith(".pcd"):
            # 读取每个.pcd文件
            pcd_path = os.path.join(pcd_files_directory, filename)
            pcd = o3d.io.read_point_cloud(pcd_path)
            
            # 将当前点云合并到累加器中
            merged_pcd += pcd
    
    # 保存合并后的点云到一个新的.pcd文件
    o3d.io.write_point_cloud(output_pcd_file, merged_pcd)
    print(f"Saved merged point cloud to {output_pcd_file}")

# 示例用法
#pcd_files_directory = './centroid_5'  # 替换为你的.pcd文件所在的文件夹路径
#output_pcd_file = 'merged_centroid.pcd'  # 合并后的点云文件名及路径
#merge_pcd_files(pcd_files_directory, output_pcd_file)
