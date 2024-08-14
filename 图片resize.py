import os
from PIL import Image
import numpy as np
size_h,size_w=512,512 # 统一大小的宽高

#提取目录下所有图片,更改尺寸后保存到另一目录
infer_path = r'F:\All_DataSet\NHM\clear' # 参考图像的大小
old_path = r'F:\DownLoad_Storage\DADRNet\NHM' # 待修改图片地址
new_path = r'F:\DownLoad_Storage\DADRNet\NHMRe'  # 修改后图片地址

# 参考infer_path动态修改不同图像为不同尺寸
size_w = []
size_h = []

for i in os.listdir(infer_path):
    print(i)
    infer = os.path.join(infer_path,i)
    w,h = Image.open(infer).size
    size_w.append(w)
    size_h.append(h)

count = 0
file_list = os.listdir(old_path)
# file_list.sort(key=lambda x: int(x.split(".")[0].split("_")[1])) #不同图像分类参考标准
# file_list.sort(key=lambda x: int(x.split(".")[0])) #不同图像分类参考标准
for i in file_list:
    try:
        # 打开图像并将其调整为size_w x size_h大小
        old = os.path.join(old_path,i)
        new = os.path.join(new_path,i)
        w, h = size_w[count], size_h[count]
        # w, h = size_w, size_h
        img = Image.open(old).resize((w,h))
        # 将灰度图像转换为数组，并调整形状为(size_w, size_h,3)
        # img_array  = np.array(img).reshape((w, h,3))
        # 保存形状为(size_w, size_h,3)的数组为图像
        # img_new  = Image.fromarray(img_array, mode='RGB')
        print(f'{count+1}/{len(os.listdir(old_path))}')
        img.save(new)

    except Exception as e:
        print(old, e) 
        continue
    count += 1
