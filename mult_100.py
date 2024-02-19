# 打开原始txt文件和目标txt文件
with open('plane_data100.txt', 'r') as f_in, open('plane_data_100.txt', 'w') as f_out:
    # 逐行读取原始文件
    for line in f_in:
        # 将每行数据按空格分割
        data = line.split()
        # 将每个值乘以100并转换为字符串，然后用空格连接并写入目标文件
        multiplied_data = [str(float(val) * 100) for val in data]
        f_out.write(' '.join(multiplied_data) + '\n')
