import pandas as pd

#ADD K (keypoint)
'''
df = pd.read_csv("../data_merged/plane1_mcp_id.csv")
#df = pd.DataFrame(data)

# 指定保存的文件名
file_name = '../ball_pivoting/bpa_data/plane1_cp.txt'

# 将DataFrame的每行转换为指定格式的字符串并保存到txt文件
with open(file_name, 'w') as file:
    for index, row in df.iterrows():
        line = f"k,{row['id']},{row['x']},{row['y']},{row['z']}\n"
        file.write(line)
'''

#ADD A (area)
df = pd.read_csv("../ball_pivoting/bpa_data/triangle_point_ids.csv")
#df = pd.DataFrame(data)

# 指定保存的文件名
file_name = '../ball_pivoting/bpa_data/area_gene.txt'

# 将DataFrame的每行转换为指定格式的字符串并保存到txt文件
with open(file_name, 'w') as file:
    for index, row in df.iterrows():
        line = f"A,{row['PointID1']},{row['PointID2']},{row['PointID3']}\n"
        file.write(line)