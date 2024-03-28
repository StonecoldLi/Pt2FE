import pandas as pd

def csv_to_txt(input_csv_path, output_txt_path):
    """
    Converts a CSV file to a TXT file, preserving the original numeric precision
    and excluding the column names.

    Parameters:
    - input_csv_path: str, the file path of the source CSV file.
    - output_txt_path: str, the file path for the output TXT file.
    """
    # 使用pandas读取CSV文件，但不处理数值格式化
    data = pd.read_csv(input_csv_path)
    
    # 将数据写入TXT文件，不包括列名称
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        for index, row in data.iterrows():
            # 将每一行的数据转换为字符串列表，保持原有精度
            row_str = row.astype(str).values
            # 用空格连接每个值，并写入文件
            txt_file.write(' '.join(row_str) + '\n')