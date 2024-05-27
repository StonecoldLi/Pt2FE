def move_point_along_vector(point, vector, distance):
    """
    Moves a point along the negative direction of a given vector by a specified distance.

    Args:
    point (np.array): The starting point (x, y, z).
    vector (np.array): The direction vector (t, p, q).
    distance (float): The distance to move along the vector's negative direction.

    Returns:
    np.array: The new point after moving.
    """
    # Normalize the direction vector
    normalized_vector = vector / np.linalg.norm(vector)
    
    # Calculate the new point by moving in the negative direction of the vector
    new_point = point - distance * normalized_vector
    
    return new_point

#对于底面，需要将点云两条连接线沿各自direction负方向移动
def move_pcd_points(pcd_file_path, direction, distance, output_file_path):
    """
    Moves all points in a .pcd file along the negative direction of the given vector by a specified distance.

    Args:
    pcd_file_path (str): Path to the input .pcd file.
    direction (list or np.array): Direction vector to move points along its negative direction.
    distance (float): Distance to move points.
    output_file_path (str): Path to save the modified .pcd file.
    """
    # Load the point cloud
    pcd = o3d.io.read_point_cloud(pcd_file_path)
    
    # Normalize the direction vector and multiply by the negative distance
    direction = np.array(direction)
    move_vector = -distance * direction / np.linalg.norm(direction)
    
    # Update each point in the point cloud
    points = np.asarray(pcd.points) + move_vector
    pcd.points = o3d.utility.Vector3dVector(points)
    
    # Save the modified point cloud
    o3d.io.write_point_cloud(output_file_path, pcd, write_ascii=False)
    print(f"Modified point cloud saved to {output_file_path}")