import open3d as o3d

def load_pcd(filename):
    cloud = o3d.io.read_point_cloud(filename)
    if cloud.is_empty():
        print(f"Can't read file {filename}")
        return None
    return cloud

def binary_to_ascii(filename, output_filename):
    print("Hello, world!")
    cloud_source = load_pcd(filename)
    if cloud_source:
        print(f"PointCloud_source has: {len(cloud_source.points)} data points.")
        o3d.io.write_point_cloud(output_filename, cloud_source, write_ascii=True)

if __name__ == "__main__":
    #binary_to_ascii("C:/Users/ADMIN/Desktop/org_jd_data/binary/jie5.pcd","C:/Users/ADMIN/Desktop/org_jd_data/binary/jie5_asc.pcd")
    binary_to_ascii()