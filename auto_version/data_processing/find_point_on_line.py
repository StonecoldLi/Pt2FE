import numpy as np

def find_point_on_line(direction_vector, point_on_line, X_value):
    """
    Find the point coordinates on a line at a specific X value.
    
    Parameters:
    - direction_vector: numpy array, the direction vector of the line (d_x, d_y, d_z).
    - point_on_line: numpy array, a point on the line (p_x, p_y, p_z).
    - X_value: float, the specific X value at which to find the point on the line.
    
    Returns:
    - numpy array: the coordinates of the point on the line at the specified X value.
    """
    d_x, d_y, d_z = direction_vector
    p_x, p_y, p_z = point_on_line
    
    # Calculate the parameter t
    t = (X_value - p_x) / d_x if d_x != 0 else 0
    
    # Calculate the point coordinates at the specific X value
    point_at_X = point_on_line + t * direction_vector
    
    return point_at_X

# # Example usage
# direction_vector = np.array([2, 3, 4])  # Direction vector of the line
# point_on_line = np.array([1, 2, 3])     # A point on the line
# X_value = 5                             # Specific X value

# point_at_X = find_point_on_line(direction_vector, point_on_line, X_value)
# print(f"The point on the line at X = {X_value} is: {point_at_X}")
