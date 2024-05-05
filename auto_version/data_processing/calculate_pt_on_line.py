def calculate_point_on_line(x, point_on_line, direction_vector):
    x0, y0, z0 = point_on_line
    a, b, c = direction_vector

    # 确保方向向量的X分量不为0，以避免除以0的错误
    if a == 0:
        raise ValueError("方向向量的X分量不能为0，因为无法使用X坐标解出其他坐标。")

    # 计算参数t
    t = (x - x0) / a

    # 使用t计算Y和Z坐标
    y = y0 + b * t
    z = z0 + c * t

    return (x, y, z)

import numpy as np
import open3d as o3d

def generate_points_and_save_as_pcd(start_point, direction_vector, interval, max_distance, output_file):
    direction_vector = np.array(direction_vector)
    unit_vector = direction_vector / np.linalg.norm(direction_vector)
    num_points = int(max_distance / interval) + 1

    # Generating points
    points = [start_point + i * interval * unit_vector for i in range(num_points)]

    # Create a point cloud object
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    # Save the point cloud to a file
    o3d.io.write_point_cloud(output_file, pcd)
    #print(f"Saved {num_points} points to {output_file}")

    return points[-1]

def generate_points_along_vector(P, Q, t, output_file):
    # Convert P and Q to numpy arrays
    #P = np.array(P)
    #Q = np.array(Q)
    
    # Calculate direction vector and normalize it
    direction_vector = Q - P
    unit_vector = direction_vector / np.linalg.norm(direction_vector)
    
    # Calculate the number of points to generate
    total_distance = np.linalg.norm(Q - P)
    num_points = int(total_distance / t)
    
    # List to store generated points
    points = [P + i * t * unit_vector for i in range(1, num_points) if np.linalg.norm(Q - (P + i * t * unit_vector)) >= t]

    if points:
        # Create a point cloud object
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)
        
        # Save the point cloud to a binary .pcd file
        o3d.io.write_point_cloud(output_file, pcd, write_ascii=False)
        print(f"Generated points saved to {output_file}")
        print(f"Generated points saved to {output_file}")

        return points
    else:
        print("No points generated.")

# Example usage
# start_point = [0, 0, 0]  # Starting point X
# direction_vector = [1, 2, 3]  # Direction vector [p, q, m]
# interval = 5  # Distance t between points
# max_distance = 50  # Maximum distance to generate points

# generate_points_and_save_as_pcd(start_point, direction_vector, interval, max_distance, 'output.pcd')


