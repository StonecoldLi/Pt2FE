import numpy as np
import open3d as o3d

def interpolate_and_save_points(pcd_file_path, points_pairs, output_file_path):
    """
    Interpolates points between given pairs of points and merges them with the original point cloud.

    Args:
    pcd_file_path (str): Path to the input .pcd file.
    points_pairs (list of list): Each sublist contains two points between which interpolation is performed.
    output_file_path (str): Path where the merged point cloud will be saved.
    """
    # Load the original point cloud
    pcd = o3d.io.read_point_cloud(pcd_file_path)
    
    # Get existing points from the point cloud
    existing_points = np.asarray(pcd.points)
    
    # List to store new interpolated points
    new_points = []

    # Calculate midpoints for each pair of points
    for pair in points_pairs:
        point1 = np.array(pair[0])
        point2 = np.array(pair[1])
        midpoint = (point1 + point2) / 2
        new_points.append(midpoint)
    
    # Combine original points with new interpolated points
    all_points = np.vstack((existing_points, new_points))
    
    # Update the point cloud
    pcd.points = o3d.utility.Vector3dVector(all_points)
    
    # Save the updated point cloud to a new .pcd file
    o3d.io.write_point_cloud(output_file_path, pcd, write_ascii=False)
    print(f"Updated point cloud saved to {output_file_path}")

# Example usage:
pcd_file_path = '../data/final_data/jie5/jie5_final_point_cloud_p0.pcd'
points_pairs = [
     [[-54.078979,2.021523,0.119142], [-54.070621,2.977706,0.108866]],
     [[-54.263771,1.998322,0.115826], [-54.270622,2.977787,0.108342]],
     [[-54.469215,1.971401,0.113338], [-54.470619,2.977867,0.107819]]
 ]
output_file_path = '../data/final_data/jie5/jie5_final_point_cloud_p0_modified.pcd'
interpolate_and_save_points(pcd_file_path, points_pairs, output_file_path)
