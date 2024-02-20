#"求两面的交线"

def intersection_line(plane1_coeffs, plane2_coeffs):
    A1, B1, C1, D1 = plane1_coeffs
    A2, B2, C2, D2 = plane2_coeffs

    # 计算交线的方向向量
    direction_vector = [B1*C2 - B2*C1, A2*C1 - A1*C2, A1*B2 - A2*B1]

    # 计算交点
    if direction_vector != [0, 0, 0]:
        # 求解交点的参数
        t = -(D1 * direction_vector[0] + D2 * direction_vector[1]) / \
            (A1 * direction_vector[0] + B1 * direction_vector[1] + C1 * direction_vector[2])
        
        # 计算交点坐标
        intersection_point = [A1 * t + D1, B1 * t + D1, C1 * t + D1]
        return intersection_point
    else:
        return None

# 示例平面方程系数
plane1_coeffs = [1.53677273e-04, -9.50453435e-01,  3.10866924e-01,  3.23398910e+00]
plane2_coeffs = [-3.49946945e-12, -2.20672290e-12,  1.00000000e+00, -1.96635929e-02]
plane3_coeffs = [1.13386453e-06, -9.47393334e-01, -3.20071664e-01, -2.87827417e+00]

# 计算交线
intersection_line1 = intersection_line(plane1_coeffs, plane2_coeffs)
intersection_line2 = intersection_line(plane3_coeffs, plane2_coeffs)

if (intersection_line1 and intersection_line2):
    print("平面1&底面的交线为:", intersection_line1)
    print("平面3&底面的交线为:", intersection_line2)

