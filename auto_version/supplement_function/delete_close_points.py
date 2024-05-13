import numpy as np
import open3d as o3d
import random

def remove_close_points(pcd_file_path, limit, output_file_path):
    """
    Remove randomly one of two points in a point cloud if their Euclidean distance is less than 'limit'.

    Args:
    pcd_file_path (str): Path to the input .pcd file.
    limit (float): Distance threshold to consider points as close.
    output_file_path (str): Path to save the modified .pcd file.
    """
    # Load the point cloud
    pcd = o3d.io.read_point_cloud(pcd_file_path)
    points = np.asarray(pcd.points)
    
    # Calculate the distance matrix
    dist_matrix = np.sqrt(((points[:, np.newaxis, :] - points[np.newaxis, :, :]) ** 2).sum(axis=2))

    # Find pairs of points where the distance is less than the limit
    close_pairs = np.argwhere((dist_matrix < limit) & (dist_matrix > 0))

    # To avoid handling a point pair more than once
    handled_indices = set()
    for i, j in close_pairs:
        if i in handled_indices or j in handled_indices:
            continue
        # Randomly choose one of the two points to remove
        to_remove = random.choice([i, j])
        handled_indices.add(to_remove)
    
    # Create a mask to keep points that are not removed
    keep_mask = np.ones(len(points), dtype=bool)
    keep_mask[list(handled_indices)] = False

    # Update points
    filtered_points = points[keep_mask]

    # Save the modified point cloud
    modified_pcd = o3d.geometry.PointCloud()
    modified_pcd.points = o3d.utility.Vector3dVector(filtered_points)
    o3d.io.write_point_cloud(output_file_path, modified_pcd, write_ascii=False)
    print(f"Modified point cloud saved to {output_file_path}")

# Example usage
pcd_file_path = '../data/centroid_data/jie1/jie1_plane2_centroids_modified_4.pcd'
limit = 0.15  # Example limit
output_file_path = '../data/centroid_data/jie1/jie1_plane2_centroids_modified_4_2.pcd'
remove_close_points(pcd_file_path, limit, output_file_path)
