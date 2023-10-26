import os
from PIL import Image
import numpy as np
size_h,size_w=256,256 # 统一大小的宽高

#提取目录下所有图片,更改尺寸后保存到另一目录
old_path=r'F:\All_DataSet\NHR\ChallengeData-II-RESIDE\gt\train' # 原图片地址
new_path=r'F:\All_DataSet\NHR\Resize256\gt\train'  # 统一图片大小地址

for i in os.listdir(old_path):
    try:
        # 打开图像并将其调整为size_w x size_h大小
        old=os.path.join(old_path,i)
        new=os.path.join(new_path,i)
        img = Image.open(old).resize((size_w, size_h))
        # 将灰度图像转换为数组，并调整形状为(size_w, size_h,3)
        img_array  = np.array(img).reshape((size_w, size_h,3))
        # 保存形状为(size_w, size_h,3)的数组为图像
        img_new  = Image.fromarray(img_array, mode='RGB')
        print(old,new)
        img_new.save(new)

    except Exception as e:
        print(old, e) 
        continue
