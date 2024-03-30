import pandas as pd
import os
from tqdm import tqdm

def process_csv_files(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            
            # 读取CSV文件
            df = pd.read_csv(file_path)
            
            # 去除Adjusted_X和Adjusted_Y列均为0的行
            df_filtered = df[(df['Adjusted_X'] != 0) | (df['Adjusted_Y'] != 0)]
            
            # 删除Original_X, Original_Y列
            df_filtered.drop(['Original_X', 'Original_Y', 'Original_Z'], axis=1, inplace=True)
            
            # 保存修改后的CSV文件
            df_filtered.to_csv(file_path, index=False)
            print(f"Processed and saved {file_path}")

# 示例用法
#input_folder = 'plane3_split/info/'  # 指定需要处理的文件夹路径
#process_csv_files(input_folder)


def format_value(value):
    # 格式化值，取前5位，忽略小数点
    value_str = str(value)
    formatted = value_str.replace('.', '')[:5]
    return formatted

def update_target_with_p_XZ(folder_path, target_csv_path, flag=0):
    '''
    适用于先沿X轴进行切分，再沿Z轴进行切分的情况 （侧面，立面等）
    '''
    # 确保目标CSV存在
    target_df = pd.read_csv(target_csv_path)

    # 如果目标文件中还没有P列，就添加这一列
    if 'Slice_Index' not in target_df.columns:
        target_df['Slice_Index'] = None

    # 遍历文件夹中的所有.csv文件
    for filename in tqdm(os.listdir(folder_path), desc="Processing files"):
        #if flag==3:
            #break
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            current_df = pd.read_csv(file_path)

            # 遍历当前文件的每一行
            for _, row in tqdm(current_df.iterrows(), total=current_df.shape[0], leave=False, desc=f"Rows in {filename}"):
                # 格式化Ad和Cd列的值
                row_ad = format_value(row['Adjusted_X'])
                row_cd = format_value(row['Adjusted_Y'])

                # 查找目标文件中相匹配的行
                matches = target_df.apply(lambda x: format_value(x['Adjusted_X']) == row_ad and format_value(x['Adjusted_Y']) == row_cd, axis=1)
                
                if matches.any():
                    # 更新P列的值
                    target_df.loc[matches, 'Slice_Index'] = row['Slice_Index']
        #flag=flag+1

    # 保存更新后的目标CSV文件
    target_df.to_csv(target_csv_path, index=False)
    print(f"Updated target CSV at {target_csv_path}")


def update_target_with_p_XY(folder_path, target_csv_path, flag=0):
    '''
    适用于先沿X轴进行切分，再沿Y轴进行切分的情况 （底面等）
    '''
    # 确保目标CSV存在
    target_df = pd.read_csv(target_csv_path)

    # 如果目标文件中还没有P列，就添加这一列
    if 'Slice_Index' not in target_df.columns:
        target_df['Slice_Index'] = None

    # 遍历文件夹中的所有.csv文件
    for filename in tqdm(os.listdir(folder_path), desc="Processing files"):
        #if flag==3:
            #break
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            current_df = pd.read_csv(file_path)

            # 遍历当前文件的每一行
            for _, row in tqdm(current_df.iterrows(), total=current_df.shape[0], leave=False, desc=f"Rows in {filename}"):
                # 格式化Ad和Cd列的值
                row_ad = format_value(row['Adjusted_X'])
                row_cd = format_value(row['Adjusted_Z'])

                # 查找目标文件中相匹配的行
                matches = target_df.apply(lambda x: format_value(x['Adjusted_X']) == row_ad and format_value(x['Adjusted_Z']) == row_cd, axis=1)
                
                if matches.any():
                    # 更新P列的值
                    target_df.loc[matches, 'Slice_Index'] = row['Slice_Index']
        #flag=flag+1

    # 保存更新后的目标CSV文件
    target_df.to_csv(target_csv_path, index=False)
    print(f"Updated target CSV at {target_csv_path}")
# 文件夹路径和目标CSV文件路径
#folder_path = './plane3_split/info'  # 替换为实际的文件夹路径
#target_csv_path = 'plane3_adjust1.csv'  # 替换为实际的目标CSV文件路径

#update_target_with_p(folder_path, target_csv_path)

'''
plane2 应比较 Adjust_X & Adjust_Z
'''