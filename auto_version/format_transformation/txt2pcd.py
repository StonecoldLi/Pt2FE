import numpy as np

def txt_to_pcd(txt_file_path, pcd_file_path):
    """
    Convert a .txt file with point cloud data (x, y, z) to a .pcd file.

    Parameters:
    - txt_file_path: str, the path to the source .txt file.
    - pcd_file_path: str, the path to the output .pcd file.
    """
    # Load the point cloud data from the .txt file
    points = np.loadtxt(txt_file_path)
    
    # Open the output .pcd file
    with open(pcd_file_path, 'w') as pcd_file:
        # Write the PCD header
        pcd_file.write(
            "VERSION .7\n"
            "FIELDS x y z\n"
            "SIZE 4 4 4\n"
            "TYPE F F F\n"
            "COUNT 1 1 1\n"
            "WIDTH {}\n"
            "HEIGHT 1\n"
            "VIEWPOINT 0 0 0 1 0 0 0\n"
            "POINTS {}\n"
            "DATA ascii\n".format(points.shape[0], points.shape[0])
        )
        
        # Write the point data
        for point in points:
            pcd_file.write("{} {} {}\n".format(float(point[0]), float(point[1]), float(point[2])))

# Example usage
#txt_file_path = 'your_file.txt'  # Replace with your .txt file path
#pcd_file_path = 'output.pcd'     # The path for the output .pcd file
#txt_to_pcd(txt_file_path, pcd_file_path)
