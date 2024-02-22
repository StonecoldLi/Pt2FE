import open3d as o3d
import numpy as np

def reverse_transform_centroids(input_file, output_file, first_direction, first_slice_distance, first_gap_distance, second_direction, second_slice_distance, second_gap_distance):
    # 读取包含变换后质心的.pcd文件
    pcd = o3d.io.read_point_cloud(input_file)
    centroids_transformed = np.asarray(pcd.points)

    # 逆向操作: 需要先计算每个质心在逆向操作中的偏移量
    # 由于是两次变换，我们先逆向第二次变换，然后再逆向第一次变换

    # 对每个方向进行规范化
    first_direction_normalized = np.array(first_direction) / np.linalg.norm(first_direction)
    second_direction_normalized = np.array(second_direction) / np.linalg.norm(second_direction)

    # 逆向第二次变换
    centroids_step1 = []
    for point in centroids_transformed:
        offset = (np.dot(point, second_direction_normalized) // (second_slice_distance + second_gap_distance)) * second_gap_distance
        point_reverted = point - offset * second_direction_normalized
        centroids_step1.append(point_reverted)

    # 逆向第一次变换
    centroids_reverted = []
    for point in centroids_step1:
        offset = (np.dot(point, first_direction_normalized) // (first_slice_distance + first_gap_distance)) * first_gap_distance
        point_reverted = point - offset * first_direction_normalized
        centroids_reverted.append(point_reverted)

    # 创建新的点云对象并保存
    reverted_pcd = o3d.geometry.PointCloud()
    reverted_pcd.points = o3d.utility.Vector3dVector(np.array(centroids_reverted))
    o3d.io.write_point_cloud(output_file, reverted_pcd)
    print(f"Reverted centroid point cloud saved to {output_file}")

# 示例用法
input_file = './data_slicing/plane2_centroids.pcd'  # 变换后的质心.pcd文件
output_file = 'plane2_reverted_centroids.pcd'    # 还原后的质心.pcd文件

# 指定切片距离、间隔和方向
first_direction = [1, 0, 0]  # 第一次切片方向
first_slice_distance = 0.05
first_gap_distance = 1.0

second_direction = [0, 1, 0]  # 第二次切片方向
second_slice_distance = 0.4
second_gap_distance = 1.0

# 还原质心坐标并保存
reverse_transform_centroids(input_file, output_file, first_direction, first_slice_distance, first_gap_distance, second_direction, second_slice_distance, second_gap_distance)


'''
# 示例用法
input_file = './data_slicing/plane2_centroids.pcd'  # 变换后的质心.pcd文件
output_file = 'plane2_reverted_centroids.pcd'    # 还原后的质心.pcd文件
'''