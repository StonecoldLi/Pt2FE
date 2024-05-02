import open3d as o3d

def ascii_to_binary(ascii_file, binary_file):
    # 读取ASCII格式的点云数据
    pcd = o3d.io.read_point_cloud(ascii_file)
    
    # 将点云数据保存为二进制格式
    o3d.io.write_point_cloud(binary_file, pcd)

# 使用示例
#ascii_file = 'C:/Users/ADMIN/Desktop/points_kua_Cloud_2.pcd'
#binary_file = 'C:/Users/ADMIN/Desktop/points_kua_Cloud_2_bin.pcd'
#ascii_to_binary(ascii_file, binary_file)
