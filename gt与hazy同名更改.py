from tqdm import tqdm
import os

# 注意lsitdir出来后的文件排序问题，改名前手动检查listdir的排序规则是否正确

hazy_file_road = r"F:\DownLoad_Storage\test\hazy" # 被改名的文件夹
gt_road = r"F:\DownLoad_Storage\test\gt" # 参照名字的文件夹

hazy_files = os.listdir(hazy_file_road)
# hazy_files.sort(key=lambda x: int(x.split(".")[0].split("_")[0])) # 检查排名规则
hazy_files.sort(key=lambda x: int(x.split("_")[0])) # 检查排名规则

gt_files = os.listdir(gt_road)
# gt_files.sort(key=lambda x: int(x.split(".")[0])) # 检查排名规则
gt_files.sort(key=lambda x: int(x.split("_")[0])) # 检查排名规则

os.chdir(hazy_file_road)
for i in tqdm(range(len(hazy_files))):
    old = hazy_files[i]
    new = gt_files[i]
    os.rename(old,new)
print('Finish files rename!!')
