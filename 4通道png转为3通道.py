from PIL import Image
import os
from tqdm import tqdm

path = r"G:\UIEB_result\gt"# 原始路径
save_path = r'G:\UIEB_result\gt_3channel'# 保存路径
all_images = os.listdir(path)

for image in tqdm(all_images):
    image_path = os.path.join(path, image)
    img = Image.open(image_path)  # 打开图片
    # print(img.format, img.size, img.mode)#打印出原图格式
    img = img.convert("RGB")  # 4通道转化为rgb三通道
    img.save(os.path.join(save_path,image))

print(f'Finish Processing!')