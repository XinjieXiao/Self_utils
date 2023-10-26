from tqdm import tqdm
import os
hazy_file_road = r"F:\All_DataSet\UNREAL_NH_size_480_480\train\deep" # 被改名的文件夹
gt_road = r"F:\All_DataSet\UNREAL_NH_size_480_480\train\gt" # 参照名字的文件夹
hazy_files = os.listdir(hazy_file_road)
gt_files = os.listdir(gt_road)
os.chdir(hazy_file_road)
for i in tqdm(range(len(hazy_files))):
    old = hazy_files[i]
    new = gt_files[i]
    os.rename(old,new)
print('Finish files rename!!')
