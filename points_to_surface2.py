import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def assign_points_to_planes(points, plane_models):
    num_planes = len(plane_models)
    num_points = points.shape[0]
    distances = np.zeros((num_points, num_planes))
    
    for i, plane in enumerate(plane_models):
        # Here we calculate the distance of each point to each plane
        distances[:, i] = np.abs(np.dot(points, plane[:3]) + plane[3]) / np.linalg.norm(plane[:3])
    
    # Assign each point to the closest plane
    assignments = np.argmin(distances, axis=1)
    return assignments

def fit_plane_PCA(points):
    pca = PCA(n_components=3)
    pca.fit(points)
    
    normal = pca.components_[-1]  # The last component is the one with the smallest variance
    point_on_plane = pca.mean_
    
    # The equation of the plane is ax + by + cz + d = 0, where [a,b,c] is the normal vector and d can be calculated
    d = -np.dot(normal, point_on_plane)
    return np.append(normal, d)

def find_planes_PCA(points, num_planes):
    # Initialize with random points (could be improved)
    plane_models = []
    
    for _ in range(num_planes):
        # Fit a plane using PCA
        plane = fit_plane_PCA(points)
        plane_models.append(plane)
    
    # Assign points to the nearest plane
    assignments = assign_points_to_planes(points, plane_models)
    
    # Recalculate planes based on assignments
    for i in range(num_planes):
        assigned_points = points[assignments == i, :]
        if assigned_points.shape[0] > 0:  # Check if there are any points assigned to this plane
            plane_models[i] = fit_plane_PCA(assigned_points)
    
    return plane_models, assignments

def initialize_planes_with_kmeans(points, num_planes):
    # 使用K-Means聚类来找到数据中的聚类中心
    kmeans = KMeans(n_clusters=num_planes, random_state=42).fit(points)
    labels = kmeans.labels_
    
    # 对每个聚类使用PCA进行平面拟合
    initial_planes = []
    for i in range(num_planes):
        cluster_points = points[labels == i]
        if len(cluster_points) > 0:
            plane = fit_plane_PCA(cluster_points)
            initial_planes.append(plane)
    return initial_planes



# Example usage
points = np.loadtxt('./plane_data_100.txt')  # Generate some random points
initial_planes = initialize_planes_with_kmeans(points, num_planes=3)
print(initial_planes)
#num_planes = 3  # Number of planes we want to fit
#plane_models, assignments = find_planes_PCA(points, num_planes)

#print("Plane parameters:", plane_models)
