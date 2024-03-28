import numpy as np
import pandas as pd
from scipy.linalg import svd

def fit_plane_to_points(points):
    """
    Fits a plane to a set of points in 3D space and returns the plane's coefficients.
    
    Parameters:
    - points: A 2D numpy array of shape (N, 3) where each row represents [x, y, z].
    
    Returns:
    - A list [A, B, C, D] representing the plane's equation coefficients in the form AX + BY + CZ + D = 0.
    """
    # Subtract the mean to find the principal components
    points_mean = points.mean(axis=0)
    points_centered = points - points_mean
    
    # Use SVD to find the direction vector of the smallest principal component
    _, _, vh = svd(points_centered, full_matrices=True)
    normal_vector = vh[-1, :]
    
    # The plane passes through the mean point, so we can find D
    D = -np.dot(normal_vector, points_mean)
    
    # The plane's equation coefficients
    A, B, C = normal_vector
    return [A, B, C, D]

def fit_planes_from_csv(csv_file_path):
    """
    Reads a CSV file with columns x, y, z, cluster, fits planes for each cluster,
    and returns a dictionary of plane equations.
    
    Parameters:
    - csv_file_path: str, the path to the CSV file.
    
    Returns:
    - A dictionary where keys are cluster values and values are lists of plane coefficients [A, B, C, D].
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Fit a plane for each cluster
    planes = {}
    for cluster, group in df.groupby('cluster'):
        points = group[['x', 'y', 'z']].values
        plane_coeffs = fit_plane_to_points(points)
        planes[cluster] = plane_coeffs
    
    return planes

# Example usage
#csv_file_path = 'your_data.csv'  # Replace this with the path to your CSV file
#plane_coefficients = fit_planes_from_csv(csv_file_path)
#print(plane_coefficients)
