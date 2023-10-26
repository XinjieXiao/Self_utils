import pandas as pd

data_1 = pd.read_csv(r'F:\BaiduSyncdisk\Graduate_Student\课程\自然语言处理\大实验作业\Task1\output_1000steps.csv')
data_2 = pd.read_csv(r'F:\BaiduSyncdisk\Graduate_Student\课程\自然语言处理\大实验作业\Task1\output_2000steps.csv')
count = 0

for i in range(len(data_1)):
    if(data_1['Category'][i] != data_2['Category'][i]):
        print(data_1['Category'][i] + ':' + data_2['Category'][i])
        count += 1

print(count)