# coding:utf-8
import numpy as np
import cv2
import os

# 导入图片
#img = cv2.imread('./files/0_20_sr.png', cv2.IMREAD_COLOR)

# 显示原图
#cv2.imshow('GrayWorld_before', img)


data_base_dir = r'F:\BaiduSyncdisk\Code\Experience_Results\FCDM\NHR_results_by_ddpm_fcb_230221_121802_gen.pth'  # 输入文件夹的路径
outfile_dir = r'F:\BaiduSyncdisk\Code\Experience_Results\FCDM\NHR_results_by_ddpm_fcb_230221_121802_gen.pth+Gray_World'  # 输出文件夹的路径

list = os.listdir(data_base_dir)
list.sort(key=lambda x: int(x.split(".")[0].split("_")[1]))
list2 = os.listdir(outfile_dir)
list2.sort()


for file in list:
    read_img_name = data_base_dir + '/' + file.strip()
    img = cv2.imread(read_img_name)
    # 定义BGR通道
    r = img[:, :, 2]
    b = img[:, :, 0]
    g = img[:, :, 1]

    # 计算BGR均值
    averB = np.mean(b)
    averG = np.mean(g)
    averR = np.mean(r)

    # 计算灰度均值
    grayValue = (averR + averB + averG) / 3

    # 计算增益
    kb = grayValue / averB
    kg = grayValue / averG
    kr = grayValue / averR

    r[:] = (r[:] * kr).clip(0, 255)
    g[:] = (g[:] * kg).clip(0, 255)
    b[:] = (b[:] * kb).clip(0, 255)

    # 显示图像
    # cv2.imshow('GrayWorld_after', img)
    out_img_name = outfile_dir + '/' + file.strip()

    cv2.imwrite(out_img_name, img)
    print("The photo which is processed is {}".format(file))





    # # 响应键盘事件
    # while True:
    #     k = cv2.waitKey(1) & 0xFF
    #     # 如果输入ESC，就结束显示。
    #     if k == 27:
    #         break
    #
    # # 清理窗口
    # cv2.destroyAllWindows()
