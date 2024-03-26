import open3d as o3d
import numpy as np

'''
gt_mesh = o3dtut.get_bunny_mesh()
gt_mesh.compute_vertex_normals()
pcd = gt_mesh.sample_points_poisson_disk(3000)
o3d.visualization.draw_geometries([pcd])
'''
# 创建一个示例点云，这里使用Open3D内置的兔子模型
gt_mesh = o3d.data.BunnyMesh()
gt_mesh = o3d.io.read_triangle_mesh(gt_mesh.path) #代替o3dtut.get_bunny_mesh()
gt_mesh.compute_vertex_normals()

# 采样点云
pcd = gt_mesh.sample_points_poisson_disk(3000)
o3d.visualization.draw_geometries([pcd])

'''
# 设置Ball Pivoting算法的球半径参数
radii = [0.005, 0.01, 0.02, 0.04]

# 使用Ball Pivoting算法重建三角形网格
rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
    pcd, o3d.utility.DoubleVector(radii))

# 获取重建后的三角形网格的顶点
vertices = np.asarray(rec_mesh.vertices)

# 获取重建后的三角形网格的面片，即每个面片由哪些顶点组成
triangles = np.asarray(rec_mesh.triangles)

# 由于点云是从采样得到的，它们没有直接的编号信息
# 因此，我们可以通过查找点云中最接近每个顶点的点来间接获取这些点的编号

# 转换点云为numpy数组
pcd_points = np.asarray(pcd.points)

# 初始化一个列表来存储每个顶点最接近的点云点的索引（编号）
vertex_to_pcd_index = []

# 对于每个顶点，找到最接近的点云点的索引
for vertex in vertices:
    distances = np.linalg.norm(pcd_points - vertex, axis=1)
    nearest_pcd_index = np.argmin(distances)
    vertex_to_pcd_index.append(nearest_pcd_index)

# 现在，我们可以使用vertex_to_pcd_index来找到构成每个三角形的点云点的索引
triangle_indices = []
for triangle in triangles:
    triangle_indices.append([vertex_to_pcd_index[v] for v in triangle])

# 打印前几个三角形的点云点索引
print(triangle_indices[:10])
'''

