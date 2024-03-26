import open3d as o3d

def visualize_pcd(file_path):
    """
    Visualize a PCD file using the Open3D library.

    Parameters:
    - file_path: str, the path to the ASCII-encoded .pcd file.
    """
    # Load the point cloud
    pcd = o3d.io.read_point_cloud(file_path)

    # Visualize the point cloud
    o3d.visualization.draw_geometries([pcd])
