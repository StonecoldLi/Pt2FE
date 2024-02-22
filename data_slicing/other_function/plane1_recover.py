import open3d as o3d
import numpy as np

def reverse_transform_centroids(input_file, output_file, first_direction_slice_distance, first_gap_distance, second_direction_slice_distance, second_gap_distance):
    # 读取包含变换后质心的.pcd文件
    pcd = o3d.io.read_point_cloud(input_file)
    centroids_transformed = np.asarray(pcd.points)

    # 计算每个质心原始的Z坐标
    centroids_reversed_second_step = centroids_transformed.copy()
    for i, point in enumerate(centroids_transformed):
        z_gap_count = int(point[2] / (second_direction_slice_distance + second_gap_distance))
        z_gap_total = z_gap_count * second_gap_distance
        centroids_reversed_second_step[i, 2] = point[2] - z_gap_total

    # 计算每个质心原始的X坐标
    centroids_reversed_first_step = centroids_reversed_second_step.copy()
    for i, point in enumerate(centroids_reversed_second_step):
        x_gap_count = int(point[0] / (first_direction_slice_distance + first_gap_distance))
        x_gap_total = x_gap_count * first_gap_distance
        centroids_reversed_first_step[i, 0] = point[0] - x_gap_total

    # 创建新的点云对象并保存
    reverted_pcd = o3d.geometry.PointCloud()
    reverted_pcd.points = o3d.utility.Vector3dVector(centroids_reversed_first_step)
    o3d.io.write_point_cloud(output_file, reverted_pcd)
    #print(f"Reverted centroid point cloud saved to {output_file}")

# 示例用法
input_file = './data_slicing/plane1_centroids.pcd'  # 变换后的质心.pcd文件
output_file = 'reverted_centroids_plane1.pcd'    # 还原后的质心.pcd文件

# 指定切片距离和间隔
first_direction_slice_distance = 0.05
first_gap_distance = 1.0
second_direction_slice_distance = 0.4
second_gap_distance = 1.0

# 还原质心坐标并保存
reverse_transform_centroids(input_file, output_file, first_direction_slice_distance, first_gap_distance, second_direction_slice_distance, second_gap_distance)
