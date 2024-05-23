# 此脚本使用时需要先试用一张图片测试exe文件读取和生成图像的名字形式再使用
# 手动使用exe代码文件：dehaze.exe test_pic.jpg，如果无法使用，尝试手动切换到exe文件所在目录再运行，不知道是什么奇怪的原理


#encoding=utf-8
import os
import shutil
# import pyiqa
import torch
exe_path = r'F:\Code\Experience_Results\NDIMorLCD_2014ICIP\NighttimeDehaze-master\NighttimeDehaze\NighttimeDehaze.exe' # 你要运行的exe文件\

# dir_path = r'F:\DownLoad_Storage\NHC\NHC-M\hazy' # 原图所在文件夹
# output_path = r'F:\DownLoad_Storage\NHC\NHC-M\hazy' # exe文件执行后产生图像所在的文件夹
# result_path = r'F:\Code\Experience_Results\OSFD_pred_psnr_20.703965111704957\NHCM' # 处理后图片存储文件夹

dir_path = r'F:\DownLoad_Storage\Unreal_NH' # 原图所在文件夹
output_path = r'F:\DownLoad_Storage\Unreal_NH' # exe文件执行后产生图像所在的文件夹
result_path = r'F:\Code\Experience_Results\NDIMorLCD_2014ICIP\NighttimeDehaze-master\Unreal_NH' # 处理后图片存储文件夹

count = 0
# psnr_score = pyiqa.create_metric('psnr').cuda()
# ssim_score = pyiqa.create_metric('ssim').cuda()
psnr = 0
ssim = 0
for i in os.listdir(dir_path):
    print(f'------------{count+1}/{len(os.listdir(dir_path))}-----------')
    # output_Pic_name = ''
    # output_Pic = ''
    # result_Pic = ''

    # 获取原图像名字和格式
    Pic_name,Pic_format = i.split('.')

    # 获取原图
    current_Pic = os.path.join(dir_path,i)

    # 开始处理当前图像
    r_v = os.system(exe_path + ' ' + current_Pic)
    # r_v = os.system(exe_path + ' ' + current_Pic + ' ' + '1')

    # 将文件移动到结果存储文件夹中
    # output_Pic_name = Pic_name + '_J_OSFD.bmp'
    # output_Pic_name = Pic_name + '_J_Fast.bmp'
    output_Pic_name = Pic_name + '_J.bmp'
    output_Pic = os.path.join(output_path, output_Pic_name)
    # output_Pic = os.path.join(dir_path,output_Pic_name)

    target_Pic_name = str(i)
    result_Pic = os.path.join(result_path,target_Pic_name)

    # psnr_t = psnr_score(output_Pic,current_Pic)
    # ssim_t = ssim_score(output_Pic,current_Pic)
    # psnr += psnr_t
    # ssim += ssim_t

    # 将输出图像移动至指定文件夹并更换回原名
    shutil.move(output_Pic,result_Pic)

    count += 1

    # print(f'--------PSNR：{psnr_t}----SSIM：{ssim_t}----------{count}/{len(os.listdir(dir_path))}-')


count += 1
# avg_psnr = psnr/count
# avg_ssim = ssim/count

print(f'%%%%%%%%%%%%%%%%% All Images Are Finished %%%%%%%%%%%%%%%%%')
# print(f'avg_psnr：{avg_psnr}')
# print(f'avg_ssim：{avg_ssim}')

