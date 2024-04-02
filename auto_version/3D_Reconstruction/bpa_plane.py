import open3d as o3d
import numpy as np
import pandas as pd

# 步骤1: 从CSV文件读取点云数据
csv_file = '../data_merged/plane2_mcp_id.csv' 
df = pd.read_csv(csv_file)
# 假设CSV文件中列名分别为'id', 'x', 'y', 'z'
points = df[['x', 'y', 'z']].values  # 获取空间坐标
point_ids = df['id'].values  # 获取点云编号

# 创建Open3D点云对象
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# 步骤2: 应用Ball Pivoting算法进行曲面重建
#radii = [0.05, 0.2, 0.5, 0.9]  # 根据数据集调整球半径参数
radii = [0.05, 0.2, 0.5, 2] #plane2
rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
    pcd, o3d.utility.DoubleVector(radii))

# 步骤3: 找出构成每个三角形的点云编号
# 获取重建后的三角形网格的顶点
vertices = np.asarray(rec_mesh.vertices)

# 获取重建后的三角形网格的面片
triangles = np.asarray(rec_mesh.triangles)

# 初始化一个列表来存储每个三角形的点云编号
triangle_point_ids = []

# 对于重建网格中的每个顶点，找到原始点云中最接近的点的编号
for triangle in triangles:
    ids = [point_ids[np.argmin(np.linalg.norm(points - vertices[v], axis=1))] for v in triangle]
    triangle_point_ids.append(ids)

# 打印或保存每个三角形的点云编号
print(len(triangle_point_ids))  # 打印前10个三角形的点云编号

# 将结果保存为CSV文件
triangle_ids_df = pd.DataFrame(triangle_point_ids, columns=['PointID1', 'PointID2', 'PointID3'])
output_csv = './bpa_data/plane2_triangle_point_ids.csv'  # 输出CSV文件的路径
triangle_ids_df.to_csv(output_csv, index=False)