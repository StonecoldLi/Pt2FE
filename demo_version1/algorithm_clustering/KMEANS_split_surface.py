import numpy as np
import open3d as o3d
import copy
from matplotlib import pyplot as plt


# 在点云上添加分类标签
def draw_labels_on_model(pcl, labels):
    cmap = plt.get_cmap("tab20")
    pcl_temp = copy.deepcopy(pcl)
    max_label = labels.max()
    colors = cmap(labels / (max_label if max_label > 0 else 1))
    pcl_temp.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([pcl_temp], window_name="可视化分类结果",
                                      width=800, height=800, left=50, top=50,
                                      mesh_show_back_face=False)


# 计算欧氏距离
def euclidean_distance(one_sample, X):
    # 将one_sample转换为一纬向量
    one_sample = one_sample.reshape(1, -1)
    # 把X转换成一维向量
    X = X.reshape(X.shape[0], -1)
    # 这是用来确保one_sample的尺寸与X相同
    distances = np.power(np.tile(one_sample, (X.shape[0], 1)) - X, 2).sum(axis=1)
    return distances


class Kmeans(object):
    # 构造函数
    def __init__(self, k=2, max_iterations=1500, tolerance=0.00001):
        self.k = k
        self.max_iterations = max_iterations
        self.tolerance = tolerance

    # 随机选取k个聚类中心点
    def init_random_centroids(self, X):
        # save the shape of X
        n_samples, n_features = np.shape(X)
        # make a zero matrix to store values
        centroids = np.zeros((self.k, n_features))
        # 因为有k个中心点，所以执行k次循环
        for i in range(self.k):
            # 随机选取范围内的值
            centroid = X[np.random.choice(range(n_samples))]
            centroids[i] = centroid
        return centroids

    # 查找距离样本点最近的中心

    def closest_centroid(self, sample, centroids):
        distances = euclidean_distance(sample, centroids)
        # np.argmin 返回距离最小值的下标
        closest_i = np.argmin(distances)
        return closest_i

    # 确定聚类
    def create_clusters(self, centroids, X):
        # 这是为了构造用于存储集群的嵌套列表
        clusters = [[] for _ in range(self.k)]
        for sample_i, sample in enumerate(X):
            centroid_i = self.closest_centroid(sample, centroids)
            clusters[centroid_i].append(sample_i)
        return clusters

    # 基于均值算法更新质心
    def update_centroids(self, clusters, X):
        n_features = np.shape(X)[1]
        centroids = np.zeros((self.k, n_features))
        for i, cluster in enumerate(clusters):
            centroid = np.mean(X[cluster], axis=0)
            centroids[i] = centroid
        return centroids

    # 获取标签

    def get_cluster_labels(self, clusters, X):
        y_pred = np.zeros(np.shape(X)[0])
        for cluster_i, cluster in enumerate(clusters):
            for sample_i in cluster:
                y_pred[sample_i] = cluster_i
        return y_pred

    # 预测标签
    def predict(self, X):
        # 随机选取中心点
        centroids = self.init_random_centroids(X)

        for _ in range(self.max_iterations):
            # 对所有点进行聚类
            clusters = self.create_clusters(centroids, X)
            former_centroids = centroids
            # 计算新的聚类中心
            centroids = self.update_centroids(clusters, X)
            # 判断是否满足收敛
            diff = centroids - former_centroids
            if diff.any() < self.tolerance:
                break

        return self.get_cluster_labels(clusters, X)


if __name__ == "__main__":
    #  加载点云
    pcd = o3d.io.read_point_cloud('../kua1_data/data_e6_b.pcd')
    points = np.asarray(pcd.points)
    o3d.visualization.draw_geometries([pcd], window_name="可视化原始点云",
                                      width=800, height=800, left=50, top=50,
                                      mesh_show_back_face=False)
    # 执行K-means聚类
    clf = Kmeans(k=3)
    labels = clf.predict(points)
    # 可视化聚类结果
    draw_labels_on_model(pcd, labels)

