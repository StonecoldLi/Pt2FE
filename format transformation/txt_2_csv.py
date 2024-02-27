import csv

# 定义输入和输出文件名
txt_file = '../generate_FE_model/data_merged/plane1merge_cp.txt'
csv_file = '../generate_FE_model/data_merged/plane1merge_cp.csv'

# 用于生成列名的字母列表
column_names = [chr(ord('x') + i) for i in range(3)]

# 打开txt文件进行读取，以及打开csv文件进行写入
with open(txt_file, 'r') as file_in, open(csv_file, 'w', newline='') as file_out:
    # 设置csv写入器，使用逗号作为分隔符
    writer = csv.writer(file_out, delimiter=',')
    
    # 写入列名
    writer.writerow(column_names[:len(next(file_in).split())])
    
    # 重新打开txt文件进行读取
    file_in.seek(0)
    # 逐行读取txt文件，并将其写入csv文件
    for line in file_in:
        # 使用空格分割行数据
        data = line.strip().split(' ')
        # 将分割后的数据写入csv文件
        writer.writerow(data)