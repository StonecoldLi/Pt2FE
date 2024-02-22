import open3d as o3d
import numpy as np

def reverse_transform_centroids(input_file, output_file, directions, gap_distances):
    # 读取包含变换后质心的.pcd文件
    pcd = o3d.io.read_point_cloud(input_file)
    centroids_transformed = np.asarray(pcd.points)

    # 逆向操作: 对每个方向进行逆向间隔填充
    directions_normalized = [np.array(dir) / np.linalg.norm(dir) for dir in directions]

    # 逆向应用间隔
    for direction_normalized, gap_distance in zip(directions_normalized, gap_distances):
        # 计算在当前方向上的投影，并基于投影计算应该移除的间隔
        projections = np.dot(centroids_transformed, direction_normalized)
        offsets = np.floor(projections / gap_distance) * gap_distance
        centroids_transformed -= np.outer(offsets, direction_normalized)

    # 创建新的点云对象并保存
    reverted_pcd = o3d.geometry.PointCloud()
    reverted_pcd.points = o3d.utility.Vector3dVector(centroids_transformed)
    o3d.io.write_point_cloud(output_file, reverted_pcd)
    print(f"Reverted centroid point cloud saved to {output_file}")

# 示例用法
input_file = './data_slicing/plane3_centroids.pcd'  # 变换后的质心.pcd文件
output_file = 'plane3_reverted_centroids.pcd'    # 还原后的质心.pcd文件

# 指定方向向量和每个方向上的间隔距离
directions = [[1, 0, 0], [0, 0, 1]]  # 先沿x轴方向，再沿z轴方向
gap_distances = [1.0, 1.0]  # 每个方向上的间隔距离

# 还原质心坐标并保存
reverse_transform_centroids(input_file, output_file, directions, gap_distances)


'''
# 示例用法
input_file = './data_slicing/plane3_centroids.pcd'  # 变换后的质心.pcd文件
output_file = 'plane3_reverted_centroids.pcd'    # 还原后的质心.pcd文件
'''