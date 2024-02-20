import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def assign_points_to_planes(points, plane_models):
    num_planes = len(plane_models)
    num_points = points.shape[0]
    distances = np.zeros((num_points, num_planes))
    
    for i, plane in enumerate(plane_models):
        distances[:, i] = np.abs(np.dot(points, plane[:3]) + plane[3]) / np.linalg.norm(plane[:3])
    
    assignments = np.argmin(distances, axis=1)
    return assignments

def fit_plane_PCA(points):
    pca = PCA(n_components=3)
    pca.fit(points)
    normal = pca.components_[-1]
    point_on_plane = pca.mean_
    d = -np.dot(normal, point_on_plane)
    return np.append(normal, d)

def initialize_planes_with_kmeans(points, num_planes):
    kmeans = KMeans(n_clusters=num_planes, random_state=42).fit(points)
    labels = kmeans.labels_
    initial_planes = []
    for i in range(num_planes):
        cluster_points = points[labels == i]
        plane = fit_plane_PCA(cluster_points)
        initial_planes.append(plane)
    return initial_planes

def refine_planes(points, initial_planes, max_iterations=100, tolerance=1e-4):
    plane_models = initial_planes
    assignments = np.zeros(points.shape[0], dtype=int)
    previous_error = np.inf
    
    for iteration in range(max_iterations):
        assignments = assign_points_to_planes(points, plane_models)
        total_error = 0
        new_plane_models = []
        for i in range(len(plane_models)):
            assigned_points = points[assignments == i, :]
            if assigned_points.shape[0] > 0:
                plane = fit_plane_PCA(assigned_points)
                new_plane_models.append(plane)
                distances = np.abs(np.dot(assigned_points, plane[:3]) + plane[3]) / np.linalg.norm(plane[:3])
                total_error += np.sum(distances)
            else:
                new_plane_models.append(plane_models[i])
        if np.abs(previous_error - total_error) < tolerance:
            break
        previous_error = total_error
        plane_models = new_plane_models
    
    return plane_models, assignments

def plot_points_by_group(points, assignments):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = ['r', 'g', 'b']
    for i in range(3):
        ax.scatter(points[assignments == i, 0], points[assignments == i, 1], points[assignments == i, 2], color=colors[i])
    plt.show()

# Example usage (Assuming `points_sample` is your points data)
#points_sample = np.loadtxt('./plane_data_e6.txt') # Replace this with your actual data
points_sample = np.loadtxt('./rotated_e6.txt')
initial_planes = initialize_planes_with_kmeans(points_sample, 3)
refined_planes, refined_assignments = refine_planes(points_sample, initial_planes)
print(refined_planes)
#print(refined_assignments)

#将assignment结果存入.csv文件中
'''
import pandas as pd
ass_series = pd.Series(refined_assignments)
csv_file = 'data_e6.csv'
df = pd.read_csv(csv_file)
df['cluster'] = ass_series
df.to_csv("data_e6_clu.csv", index=False)
'''
#ass_series.to_csv(csv_file, index=False)

plot_points_by_group(points_sample, refined_assignments)

