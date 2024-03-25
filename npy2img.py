import PIL
import numpy as np
from PIL import Image
path = r'F:\DownLoad_Storage\NHR_train_C2PNet_3_19_default_clcr_1500000_losses.npy' # 要转换为图片的.npy文件
data = np.load(path)
image = Image.fromarray(data)
image.show()