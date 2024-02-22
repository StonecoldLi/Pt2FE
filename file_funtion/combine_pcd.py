import open3d as o3d
import numpy as np

# 读取两个PCD文件
pcd1 = o3d.io.read_point_cloud("../data_slicing/centroid_5/plane2_centroids.pcd")
pcd2 = o3d.io.read_point_cloud("..\data_slicing\extra_data\extra_plane3.pcd")
pcd3 = o3d.io.read_point_cloud("..\data_slicing\extra_data\extra_plane1.pcd")

# 合并点云
# 这里我们直接将两个点云的点合并到一个新的点云对象中
merged_points = np.concatenate((np.asarray(pcd1.points), np.asarray(pcd2.points), np.asarray(pcd3.points)),axis=0)
merged_pcd = o3d.geometry.PointCloud()
merged_pcd.points = o3d.utility.Vector3dVector(merged_points)

# 可选：如果PCD文件包含颜色信息，也可以合并颜色
if pcd1.colors and pcd2.colors:
    merged_colors = np.concatenate((np.asarray(pcd1.colors), np.asarray(pcd2.colors), np.asarray(pcd3.colors)), axis=0)
    merged_pcd.colors = o3d.utility.Vector3dVector(merged_colors)

# 保存合并后的点云到新的PCD文件
o3d.io.write_point_cloud("../data_slicing/merge_data_cp_plane2.pcd", merged_pcd, write_ascii=False)
