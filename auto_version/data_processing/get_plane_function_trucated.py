import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD

def fit_plane_to_points(points):
    """
    Fits a plane to a set of points in 3D space and returns the plane's coefficients using truncated SVD.
    
    Parameters:
    - points: A 2D numpy array of shape (N, 3) where each row represents [x, y, z].
    
    Returns:
    - A list [A, B, C, D] representing the plane's equation coefficients in the form AX + BY + CZ + D = 0.
    """
    # Ensure points are in a proper numeric format
    points = np.asarray(points, dtype=np.float64)
    
    # Subtract the mean to find the principal components
    points_mean = points.mean(axis=0)
    points_centered = points - points_mean
    
    # Use Truncated SVD to find the direction vector of the smallest principal component
    svd = TruncatedSVD(n_components=1, n_iter=7, random_state=42)
    svd.fit(points_centered)
    normal_vector = svd.components_[0]
    
    # The plane passes through the mean point, so we can find D
    D = -np.dot(normal_vector, points_mean)
    
    # The plane's equation coefficients
    A, B, C = normal_vector
    return [A, B, C, D]

def fit_planes_from_csv_truc(csv_file_path):
    """
    Reads a CSV file with columns x, y, z, cluster, fits planes for each cluster using truncated SVD,
    and returns a dictionary of plane equations.
    
    Parameters:
    - csv_file_path: str, the path to the CSV file.
    
    Returns:
    - A dictionary where keys are cluster values and values are lists of plane coefficients [A, B, C, D].
    """
    # Read the CSV file ensuring data types
    df = pd.read_csv(csv_file_path, dtype={'x': 'float64', 'y': 'float64', 'z': 'float64', 'cluster': 'category'})
    
    # Fit a plane for each cluster
    planes = {}
    for cluster, group in df.groupby('cluster'):
        points = group[['x', 'y', 'z']].values
        if not points.size == 0:
            plane_coeffs = fit_plane_to_points(points)
            planes[cluster] = plane_coeffs
    #print(points)
    
    print(planes)

fit_planes_from_csv_truc("../data/org_data/jie5_clu.csv")