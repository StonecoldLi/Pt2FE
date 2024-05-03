import numpy as np
import open3d as o3d

def visualize_point_cloud_with_pca_svd(pcd_file_path):
    """
    Load point cloud from a .pcd file, calculate the principal component direction using SVD,
    and visualize the original point cloud along with the principal direction vector.

    Args:
    pcd_file_path (str): Path to the binary encoded .pcd file.

    Returns:
    None, but visualizes the point cloud and principal direction vector.
    """
    # Load the point cloud from a file
    pcd = o3d.io.read_point_cloud(pcd_file_path)
    
    # Convert Open3D PointCloud to NumPy array
    points = np.asarray(pcd.points)
    
    # Centering the points (important for PCA)
    centroid = np.mean(points, axis=0)
    points_centered = points - centroid
    
    # Calculate PCA using SVD
    u, s, vh = np.linalg.svd(points_centered, full_matrices=False)
    principal_vector = vh[0]  # The first row of vh (principal component)

    
    # The principal vector is the first column of u (or the first row of vh transposed)
    #principal_vector = principal_axes[:, 0]
    
    # Visualizing the point cloud and the principal direction
    # Create a vector from the mean center pointing in the direction of the principal component
    vector_length = 2 * np.max(np.linalg.norm(points_centered, axis=1))  # Scale vector for better visualization
    vector = principal_vector * vector_length
    #print(principal_vector)
    vector_line = np.vstack([centroid, centroid + vector])  # Ensure array shapes are correct for stacking
    
    # Create a line set to visualize the principal direction
    line_set = o3d.geometry.LineSet(
        points=o3d.utility.Vector3dVector(vector_line),
        lines=o3d.utility.Vector2iVector([[0, 1]])
    )
    line_set.colors = o3d.utility.Vector3dVector([[1, 0, 0]])  # Red color for principal direction
    
    # Visualize point cloud and line
    o3d.visualization.draw_geometries([pcd, line_set])

    return principal_vector

# Example usage (commented out):
#visualize_point_cloud_with_pca_svd('../../data/org_data/jie5_dimian_pcd_b.pcd')
