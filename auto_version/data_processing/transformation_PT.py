#变换矩阵
'''
希望以底边为基础，以底边上的一点为（0，0，0），进行坐标变换 （1为底边）
'''

import numpy as np

def normalize(v):
    """Normalize a vector."""
    return v / np.linalg.norm(v)

def rotation_matrix_from_vectors(vec1, vec2):
    """Find the rotation matrix that aligns vec1 to vec2"""
    a, b = normalize(vec1), normalize(vec2)
    v = np.cross(a, b)
    c = np.dot(a, b)
    s = np.linalg.norm(v)
    kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    rotation_matrix = np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2))
    return rotation_matrix

def transform_points(points, plane_normal, point_to_origin):
    # Step 1: Translate points so that point_to_origin moves to (0,0,0)
    #translated_points = points - point_to_origin
    
    # Step 2: Rotate points so that plane_normal aligns with the z-axis
    #target_normal = np.array([0, 0, 1])  # Target normal vector (z-axis)
    #R = rotation_matrix_from_vectors(plane_normal, target_normal)
    #rotated_points = np.dot(translated_points, R.T)  # Apply rotation

    rotated_points = points - point_to_origin
    
    return rotated_points


#points = np.loadtxt('./plane_data_e6.txt')
#point_to_origin = [-0.129960,0.448177,1.787794]
#plane_normal = [-3.22005644e-03, -1.11233907e-03,  9.99994197e-01]

#rotated_points = transform_points(points, plane_normal, point_to_origin)
#np.savetxt("rotated_e6.txt", rotated_points)
#import pandas as pd
#pd.DataFrame(rotated_points,columns=["x","y","z"]).to_csv("rotated_e6.csv",index=False)