import cv2
import skimage
import os
import time

if __name__ == "__main__":
    gt_road = r"F:\All_DataSet\Data\NHM\valid_NH\gt"
    hazy_road = r"F:\DownLoad_Storage\output\NHM\pred_FFA_ots"

    gt_imgs = os.listdir(gt_road)
    hazy_imgs = os.listdir(hazy_road)

    psnr = []
    ssim = []

    start_time = time.time()

    for i in range(len(gt_imgs)):
        img1 = cv2.imread(os.path.join(gt_road, gt_imgs[i]))
        img2 = cv2.imread(os.path.join(hazy_road,hazy_imgs[i]))
        psnr.append(skimage.measure.compare_psnr(img1, img2, data_range=255))
        ssim.append(skimage.measure.compare_ssim(img1, img2, data_range=255, multichannel=True))

    avr_psnr = sum(psnr) / len(psnr)
    avr_ssim = sum(ssim) / len(ssim)

    end_time = time.time() - start_time

    print('val_psnr: {0:.2f}, val_ssim: {1:.4f}'.format(avr_psnr, avr_ssim))

    print('validation time is {0:.4f}'.format(end_time))

    # print(skimage.measure.compare_psnr(img1, img2, data_range=255)) # 37.28288478569673
    # print(skimage.measure.compare_ssim(img1, img2, data_range=255, multichannel=True))