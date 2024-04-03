import open3d as o3d
import numpy as np

def align_and_translate_point_cloud(pcd_path, save_path, specific_point):
    # 读取点云数据
    pcd = o3d.io.read_point_cloud(pcd_path)

    # 转换为numpy数组
    points = np.asarray(pcd.points)

    # 计算质心
    centroid = np.mean(points, axis=0)

    # 平移到质心在原点
    points_centered = points - centroid

    # 计算PCA
    pca = np.linalg.svd(points_centered.T, full_matrices=False)
    principal_axes = pca[0]

    # 构造旋转矩阵，使第一个主成分与x轴对齐
    rotation_matrix = np.identity(3)
    rotation_matrix[:, 0] = principal_axes[:, 0]
    if np.linalg.det(rotation_matrix) < 0:  # 保证右手定则
        rotation_matrix[:, 0] *= -1

    # 应用旋转
    rotated_points = np.dot(points_centered, rotation_matrix)

    # 找到指定点在旋转后的新位置
    specific_point_transformed = (np.dot(specific_point - centroid, rotation_matrix))

    # 计算将旋转后的特定点移至原点所需的平移向量
    translate_vector = -specific_point_transformed

    # 应用平移
    translated_points = rotated_points + translate_vector

    # 更新点云对象
    pcd.points = o3d.utility.Vector3dVector(translated_points)

    # 保存对齐和平移后的点云为PCD文件
    o3d.io.write_point_cloud(save_path, pcd)

    return pcd

# 调用函数
#pcd_path = 'path_to_your_pcd_file.pcd'  # 源PCD文件路径
#save_path = 'path_to_your_transformed_pcd_file.pcd'  # 变换后的PCD文件保存路径
#specific_point = np.array([x, y, z])  # 将x, y, z替换为你想移动到原点的点的坐标

#align_and_translate_point_cloud(pcd_path, save_path, specific_point)

# 如果你想查看保存的点云，可以重新加载并可视化它
#transformed_pcd = o3d.io.read_point_cloud(save_path)
#o3d.visualization.draw_geometries([transformed_pcd])
