import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"F:\All_DataSet\NHR\test\hazy\0920_lowLight_1.jpg")


# n_bins = 256
# hist_range = [0, 256]
# hists = []
# channels = {0: "blue", 1: "green", 2: "red"}
# for ch in channels:
#     hist = cv2.calcHist(
#         [img], channels=[ch], mask=None, histSize=[n_bins], ranges=hist_range
#     )
#     hist = hist.squeeze(axis=-1)
#     hists.append(hist)
#
#
# def plot_hist(bins, hist, color):
#     centers = (bins[:-1] + bins[1:]) / 2
#     widths = np.diff(bins)
#     ax.bar(centers, hist, width=widths, color=color)
#
#
# bins = np.linspace(*hist_range, n_bins + 1)
# fig, ax = plt.subplots()
# ax.set_xticks([0, 256])
# ax.set_xlim([0, 256])
# ax.set_ylim([0, 8000])
# ax.set_xlabel("Pixel Value")
#
# for hist, color in zip(hists, channels.values()):
#     plot_hist(bins, hist, color=color)
# plt.show()



# 按R、G、B三个通道分别计算颜色直方图
b_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
g_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
r_hist = cv2.calcHist([img], [2], None, [256], [0, 256])

# 显示3个通道的颜色直方图

plt.plot(r_hist, label='R', color='red')
plt.plot(g_hist, label='G', color='green')
plt.plot(b_hist, label='B', color='blue')
plt.legend(loc='best')
plt.xlim([0, 180])
plt.ylim([0, 8000])
plt.show()

