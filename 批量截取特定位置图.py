# 代码来源:https://zhuanlan.zhihu.com/p/685833237

import cv2
import os

def draw_local_zoom_callback(value):
    global zoom_fac
    zoom_fac = value
    print("Zoom fac: {}".format(zoom_fac))

def mouse_callback(event, x1, y1, flags, userdata):
    global pt_l
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Rec left top: {} {}".format(x1, y1))
        pt_l.append([x1, y1])

def draw_zoom_rec(output_path,img):
    global zoom_fac
    h, w = img.shape[0], img.shape[1]
    x1, y1, x2, y2 = pt_l[0][0], pt_l[0][1], pt_l[1][0], pt_l[1][1]
    zoom_w = x2 - x1
    zoom_h = y2 - y1
    # 放大系数弹窗自定义
    if zoom_w * zoom_fac > w or zoom_h * zoom_fac > h:
        print("Local zoom size > image size, Please set smaller zoom size")
        return
    zoom_w = zoom_w * zoom_fac
    zoom_h = zoom_h * zoom_fac
    zoom_in_img = img[y1:y2, x1:x2]
    zoom_in_img = cv2.resize(zoom_in_img, (zoom_w, zoom_h))
    cv2.rectangle(img, pt_l[0], pt_l[1], (0, 0, 255), 3, -1)
    cv2.imwrite(os.path.join(output_path, image_file.split('.')[0] + "label.png"), img)
    # 局部在图像左上部分，放大框在右下
    if (x1 + (x2 - x1) / 2 < w / 2 and y1 + (y2-y1)/2 < h/2):
        img[h-zoom_h:h, w-zoom_w:w] = zoom_in_img[:, :]
        cv2.rectangle(img, (w-zoom_w, h - zoom_h), (w, h), (0, 0, 255), 3, -1)
    # 局部在图像右上部分，放大框在左下
    elif (x1 + (x2 - x1) / 2 > w / 2 and y1 + (y2-y1)/2 < h/2):
        img[h-zoom_h:h, 0:zoom_w] = zoom_in_img[:, :]
        cv2.rectangle(img, (0, h), (0 + zoom_w, h-zoom_h), (0, 0, 255), 3, -1)

    # 局部在图像左下部分，放大框在右上
    elif (x1 + (x2 - x1) / 2 < w / 2 and y1 + (y2-y1)/2 > h/2):
        img[0:zoom_h, w-zoom_w: w] = zoom_in_img[:, :]
        cv2.rectangle(img, (w, 0), (w-zoom_w, zoom_h), (0, 0, 255), 3, -1)
    # 局部在图像右下，放大在左上
    elif (x1 + (x2 - x1) / 2 > w / 2 and y1 + (y2-y1)/2 > h/2):
        img[0:zoom_h, 0:zoom_w] = zoom_in_img[:, :]
        cv2.rectangle(img, (0, 0), (0 + zoom_w, 0+zoom_h), (0, 0, 255), 3, -1)




if __name__ == '__main__':
    ws_path = os.path.abspath(".")
    data_path = os.path.join(ws_path, "data")
    if not os.path.exists(data_path):
        Exception("Data path not exist!")
    img_file_list = os.listdir(data_path)
    if not img_file_list:
        Exception("Data folder has not image files.")
    cv2.namedWindow("DrawRec", flags=0)
    cv2.setMouseCallback("DrawRec", mouse_callback)
    cv2.createTrackbar("ZoomSize", "DrawRec", 3, 5, draw_local_zoom_callback)
    pt_l = []
    zoom_fac = 3
    output_path = os.path.join(ws_path, "output")
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    while True:
        vis_img = cv2.imread(os.path.join(data_path, img_file_list[0]))
        pic_hei, pic_wid, _ =  vis_img.shape
        cv2.imshow("DrawRec", vis_img)
        k = cv2.waitKey(1)
        if k == 27:
            break

    for image_file in img_file_list:
        img = cv2.imread(os.path.join(data_path, image_file))
        img = cv2.resize(img,(pic_wid,pic_hei))
        if len(pt_l) == 2:
            draw_zoom_rec(output_path,img)
            cv2.imwrite(os.path.join(output_path, image_file.split('.')[0] + "rec.png"), img)
    pt_l.clear()
    cv2.destroyAllWindows()