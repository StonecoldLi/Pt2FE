import open3d as o3d
import numpy as np

def load_point_cloud(points):
    """
    根据numpy array加载点云数据
    """
    cloud = o3d.geometry.PointCloud() #创建一个Open3d点云对象
    cloud.points = o3d.utility.Vector3dVector(points) #将传入的点赋值给点云对象
    return cloud #返回点云对象

def segment_planes(points, distance_threshold=0.1,ransac_n=3, num_iterations=1000):
    """
    分割平面（RanSAC）并且可视化
    """
    cloud = load_point_cloud(points)
    plane_models = [] #目标平面参数

    #loop,直到点云中没有足够的点进行平面分割
    while cloud.has_points():
        # 如果剩余的点少于ransac_n，说明不足以进行RANSAC平面拟合，结束循环
        if len(cloud.points) < ransac_n:
            print("Not enough points to proceed with RANSAC.")
            break

        colors = np.asarray(cloud.colors)
        #print(colors)
        #break

        #使用RanSAC算法尝试从点云中分割出一个平面
        plane_model, inliers = cloud.segment_plane(distance_threshold=distance_threshold, ransac_n=ransac_n, num_iterations=num_iterations)

        # 如果找到的内点数量不足或者低于某个阈值，认为没有找到显著的平面，结束循环
        if len(inliers) < cloud.points.__len__() * 0.01:
            print("No significant plane found or not enough inliers.")
            break

        inlier_cloud = cloud.select_by_index(inliers) # 从点云中选出属于当前平面的点（内点）
        outlier_cloud = cloud.select_by_index(inliers, invert=True) # 从点云中选出不属于当前平面的点（外点）

        #Assign a random color to inlier points for vis.
        if len(colors) == 0:  # Check if the colors array is empty and initialize if necessary
            colors = np.zeros((np.asarray(cloud.points).shape[0], 3))
        color = np.random.uniform(0, 1, 3)
        colors[inliers] = color
        #print(colors)
        cloud.colors = o3d.utility.Vector3dVector(colors)

        plane_models.append(plane_model)
        cloud = outlier_cloud #更新点云数据，进行下一轮平面分割

    #o3d.visualization.draw_geometries([cloud])
    
    return plane_models
    

#points = np.random.rand(1000,3)
#print(points[0:10])
points = np.loadtxt('./plane_data_100.txt')
#print(type(a))
print(segment_planes(points))