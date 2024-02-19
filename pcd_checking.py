import open3d as o3d

def load_pcd(filename):
    cloud = o3d.io.read_point_cloud(filename)
    if cloud.is_empty():
        print(f"Can't read file {filename}")
        return None
    return cloud

def main():
    print("Hello, world!")
    filename = "./1kua.pcd"
    cloud_source = load_pcd(filename)
    if cloud_source:
        print(f"PointCloud_source has: {len(cloud_source.points)} data points.")

        output_filename = "./ascii_change.pcd"
        o3d.io.write_point_cloud(output_filename, cloud_source, write_ascii=True)

if __name__ == "__main__":
    main()
