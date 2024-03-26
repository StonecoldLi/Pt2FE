import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Utilize PCA to fit a plane to the given points
def fit_plane_PCA(points):
    pca = PCA(n_components=3)
    pca.fit(points)
    normal = pca.components_[-1]  # The last component is the smallest variance
    point_on_plane = pca.mean_
    d = -np.dot(normal, point_on_plane)
    return np.append(normal, d)

# Assign points to the closest plane
def assign_points_to_planes(points, plane_models):
    num_planes = len(plane_models)
    num_points = points.shape[0]
    distances = np.zeros((num_points, num_planes))
    for i, plane in enumerate(plane_models):
        distances[:, i] = np.abs(np.dot(points, plane[:3]) + plane[3]) / np.linalg.norm(plane[:3])
    assignments = np.argmin(distances, axis=1)
    return assignments

# Improved version to find planes using PCA with K-Means initialization
def find_planes_PCA_with_kmeans(points, num_planes):
    initial_planes = initialize_planes_with_kmeans(points, num_planes)
    plane_models = initial_planes
    
    # Assign points to the nearest plane
    assignments = assign_points_to_planes(points, plane_models)
    
    # Recalculate planes based on assignments to refine the fit
    for i in range(num_planes):
        assigned_points = points[assignments == i, :]
        if assigned_points.shape[0] > 0:  # Check if there are points assigned to this plane
            plane_models[i] = fit_plane_PCA(assigned_points)
    
    return plane_models, assignments

# Initialize planes with K-Means for better starting points
def initialize_planes_with_kmeans(points, num_planes):
    kmeans = KMeans(n_clusters=num_planes, random_state=42).fit(points)
    labels = kmeans.labels_
    initial_planes = []
    for i in range(num_planes):
        cluster_points = points[labels == i]
        if len(cluster_points) > 0:
            plane = fit_plane_PCA(cluster_points)
            initial_planes.append(plane)
    return initial_planes

# Plot points by group with different colors
def plot_points_by_group(points, assignments):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    colors = ['r', 'g', 'b']
    for i in range(np.max(assignments) + 1):
        ax.scatter(points[assignments == i, 0], points[assignments == i, 1], points[assignments == i, 2], color=colors[i], label=f'Group {i+1}')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.legend()
    plt.show()

# Generating a sample set of points for demonstration
np.random.seed(42)
points_sample = np.random.rand(300, 3) * 100

# Find planes and assignments
plane_models, assignments = find_planes_PCA_with_kmeans(points_sample, num_planes=3)

# Plotting the points by group
plot_points_by_group(points_sample, assignments)
