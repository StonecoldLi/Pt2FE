import numpy as np
import open3d as o3d

def transform_point_cloud(pcd_file_path, vector, specific_point,output_file_path):
    """
    Transform a point cloud by rotating it so that the projection of a given vector
    onto the Z=0 plane aligns with the positive y-axis, and translating so that a
    specific point after rotation aligns to the origin.

    Args:
    pcd_file_path (str): Path to the binary encoded .pcd file.
    vector (np.array): The vector to align with the y-axis.
    specific_point (np.array): The specific point to move to the origin after rotation.

    Returns:
    np.array: The transformation matrix used.
    """
    # Load the point cloud from a file
    pcd = o3d.io.read_point_cloud(pcd_file_path)
    
    # Projection of the vector onto the Z=0 plane (ignore z component)
    projected_vector = np.array([vector[0], vector[1], 0])
    
    # Target vector on the Z=0 plane (y-axis)
    target_vector = np.array([1, 0, 0])
    
    # Angle between projected_vector and target_vector
    angle = np.arctan2(projected_vector[1], projected_vector[0]) - np.arctan2(target_vector[1], target_vector[0])
    
    # Rotation matrix around Z-axis
    R = np.array([
        [np.cos(-angle), -np.sin(-angle), 0],
        [np.sin(-angle), np.cos(-angle), 0],
        [0, 0, 1]
    ])
    
    # Applying rotation
    rotated_points = np.dot(R, np.asarray(pcd.points).T).T
    
    # Update point cloud with rotated points
    pcd.points = o3d.utility.Vector3dVector(rotated_points)
    
    # Translate the specific point to the origin
    specific_point_rotated = np.dot(R, specific_point)
    translation = -specific_point_rotated
    
    # Translation matrix
    T = np.eye(4)
    T[:3, 3] = translation
    
    # Apply translation
    pcd.translate(translation)
    
    # Create the full transformation matrix
    transform_matrix = np.eye(4)
    transform_matrix[:3, :3] = R
    transform_matrix[:3, 3] = translation
    
    o3d.io.write_point_cloud(output_file_path, pcd, write_ascii=False)
    
    return transform_matrix

# Example usage (commented out):
# transform_matrix = transform_point_cloud("../../data/org_data/jie5_b.pcd"
#                                          , np.array([0.38257343, 0.92391709, 0.00384504])
#                                          , np.array([-2.107190,-6.126470,0.653520]))
#print("Transformation Matrix:\n", transform_matrix)
