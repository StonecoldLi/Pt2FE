import open3d as o3d

def visualize_pcds(file_paths):
    """
    Visualize multiple PCD files in a single window using the Open3D library.

    Parameters:
    - file_paths: list of str, the paths to the ASCII-encoded .pcd files.
    """
    # Initialize an empty list to hold the point cloud objects
    pcds = []
    
    # Load each point cloud and add it to the list
    for file_path in file_paths:
        pcd = o3d.io.read_point_cloud(file_path)
        pcds.append(pcd)
    
    # Visualize all the point clouds together
    o3d.visualization.draw_geometries(pcds)

