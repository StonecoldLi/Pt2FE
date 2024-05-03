import pandas as pd
import os

def save_clusters_to_csv(file_path,o_path,file_name):
    """
    Reads a CSV file with columns x, y, z, cluster, groups the data by the cluster
    value, and saves each group to a separate CSV file named plane_n.csv where
    n is the cluster value.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Group the data by the 'cluster' column
    grouped = df.groupby('cluster')
    
    # Iterate over each group
    for name, group in grouped:
        # Select only the x, y, z columns
        xyz_data = group[['x', 'y', 'z']]
        
        # Construct the output file name
        output_file_name = f'plane_{name}.csv'
        output_path = f"./data/rotated_data/" + o_path + f"{file_name}_plane_{name}" #家目录所在位置为起点（）
        full_path = os.path.join(output_path, output_file_name) #创建相应文件夹和.txt文件

        # 确保目标路径存在
        os.makedirs(output_path, exist_ok=True)
        # Save the xyz data to the output file
        xyz_data.to_csv(full_path, index=False) 
        print(f'Saved to: {output_file_name}')

