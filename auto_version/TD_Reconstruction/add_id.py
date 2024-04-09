import pandas as pd
# 以前面创建的CSV文件为例，添加'id'列
#df = pd.read_csv('../data_merged/plane3merge_cp.csv')

def add_id(csv_file,flag,updated_csv_file_path):
    df = pd.read_csv(csv_file)
# 添加'id'列，从1开始
    df['id'] = [str(flag+1) + str(i+1) for i in range(len(df))] #命名规则！

# 由于原始CSV文件没有'id'列，这里将'id'列移动到最前面
    df = df[['id'] + [col for col in df.columns if col != 'id']]

# 保存修改后的CSV文件
    df.to_csv(updated_csv_file_path, index=False)
