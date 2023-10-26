import os
import shutil
file_road = r"F:\All_DataSet\NHM\middlebury_datasets\total"
save_road = r"F:\All_DataSet\NHM\middlebury_datasets"
files = os.listdir(file_road)
count = 0
for i in files:
    print(i)
    if(i.endswith('lowLight.jpg')):
        shutil.copyfile(os.path.join(file_road,i),os.path.join(r"F:\All_DataSet\NHM\middlebury_datasets\lowLight",i))
    elif(i.endswith('NighttimeHazy.jpg')):
        shutil.copyfile(os.path.join(file_road,i),os.path.join(r"F:\All_DataSet\NHM\middlebury_datasets\NighttimeHazy",i))
print("Done!")
