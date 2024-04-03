import pandas as pd

def pcd_to_txt(pcd_file, txt_file):
    # 读取PCD文件
    pcd_data = pd.read_csv(pcd_file, sep=' ', skiprows=11, header=None, names=['x', 'y', 'z'])
    
    # 保存为TXT文件
    pcd_data.to_csv(txt_file, sep=' ', index=False)

def pcd_to_txt_without_xyz(pcd_file, txt_file):
    # 读取PCD文件
    pcd_data = pd.read_csv(pcd_file, sep=' ', skiprows=11, header=None)
    
    # 保存为TXT文件
    pcd_data.to_csv(txt_file, sep=' ', index=False)

