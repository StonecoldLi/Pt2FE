import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def kmeans_clustering(points, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(points)
    return kmeans.labels_, kmeans.cluster_centers_

def plot_points_by_cluster(points, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=labels, cmap='viridis')
    #plt.colorbar(scatter)
    plt.show()

#points = np.loadtxt('../../data/rotated_data/jie5/jie5_rot_txt.txt',skiprows=1)  # 请替换文件名为你的文件路径
#n_clusters = 3
#labels, centers = kmeans_clustering(points, n_clusters)
#plot_points_by_cluster(points, labels)
