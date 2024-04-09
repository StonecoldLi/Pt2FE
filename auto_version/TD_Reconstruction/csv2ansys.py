import pandas as pd

#ADD K (keypoint)
def Generate_KP(csv_file,output_txt):
    df = pd.read_csv(csv_file)

    # 指定保存的文件名
    #file_name = '../ball_pivoting/bpa_data/plane3_cp.txt'


    with open(output_txt, 'w') as file:
        for index, row in df.iterrows():
            line = f"k,{row['id']},{row['x']},{row['y']},{row['z']}\n"
            file.write(line)


#ADD A (area)
def Generate_AREA(csv_file, output_txt):
    df = pd.read_csv(csv_file)
#df = pd.DataFrame(data)

# 指定保存的文件名
    #file_name = '../ball_pivoting/bpa_data/plane3_area_gene.txt'

# 将DataFrame的每行转换为指定格式的字符串并保存到txt文件
    with open(output_txt, 'w') as file:
        for index, row in df.iterrows():
            line = f"A,{row['PointID1']},{row['PointID2']},{row['PointID3']}\n"
            file.write(line)
