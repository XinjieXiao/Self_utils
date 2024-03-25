import os
from PIL import Image
import numpy as np
size_h,size_w=256,256 # 统一大小的宽高

#提取目录下所有图片,更改尺寸后保存到另一目录
infer_path = r'F:\All_DataSet\NHR\ChallengeData-II-RESIDE\test\input' # 参考图像的大小
old_path = r'F:\BaiduSyncdisk\Code\Experience_Results\FCDM\NHR_results_colofix_infer' # 待修改图片地址
new_path = r'F:\BaiduSyncdisk\Code\Experience_Results\FCDM\t'  # 修改后图片地址
size_w = []
size_h = []

for i in os.listdir(infer_path):
    infer = os.path.join(infer_path,i)
    w,h = Image.open(infer).size
    size_w.append(w)
    size_h.append(h)

count = 0
file_list = os.listdir(old_path)
file_list.sort(key=lambda x: int(x.split(".")[0].split("_")[1]))
for i in file_list:
    try:
        # 打开图像并将其调整为size_w x size_h大小
        old = os.path.join(old_path,i)
        new = os.path.join(new_path,i)
        w, h = size_w[count], size_h[count]
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
