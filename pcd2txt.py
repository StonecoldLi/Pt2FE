import pandas as pd

# 读取PCD文件
pcd_data = pd.read_csv('ascii_change.pcd', sep=' ', skiprows=11, header=None, names=['x', 'y', 'z'])

# 保存为TXT文件
pcd_data.to_csv('plane_data_org.txt', sep=' ', index=False)
