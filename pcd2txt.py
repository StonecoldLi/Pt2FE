import pandas as pd

# 读取PCD文件
pcd_data = pd.read_csv('points_1kua.pcd', sep=' ', skiprows=0, header=None, names=['x', 'y', 'z'])

# 保存为TXT文件
pcd_data.to_csv('plane_data.txt', sep=' ', index=False)
