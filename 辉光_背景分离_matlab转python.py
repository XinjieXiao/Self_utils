import numpy as np
from scipy import ndimage, fftpack
from PIL import Image
import matplotlib.pyplot as plt
import os
import datetime

start_time = datetime.datetime.now()

def zero_pad(image, shape, position='corner'):
    shape = np.asarray(shape, dtype=int)
    imshape = np.asarray(image.shape, dtype=int)

    if np.alltrue(imshape == shape):
        return image

    if np.any(shape <= 0):
        raise ValueError("ZERO_PAD: null or negative shape given")

    dshape = shape - imshape
    if np.any(dshape < 0):
        raise ValueError("ZERO_PAD: target size smaller than source one")

    pad_img = np.zeros(shape, dtype=image.dtype)

    idx, idy = np.indices(imshape)

    if position == 'center':
        if np.any(dshape % 2 != 0):
            raise ValueError("ZERO_PAD: source and target shapes "
                             "have different parity.")
        offx, offy = dshape // 2
    else:
        offx, offy = (0, 0)

    pad_img[idx + offx, idy + offy] = image

    return pad_img

# def psf2otf(psf, shape):
#
#     if np.all(psf == 0):
#         return np.zeros_like(psf)
#
#     inshape = psf.shape
#     # Pad the PSF to outsize
#     psf = zero_pad(psf, shape, position='corner')
#
#     # Circularly shift OTF so that the 'center' of the PSF is
#     # [0,0] element of the array
#     for axis, axis_size in enumerate(inshape):
#         psf = np.roll(psf, -int(axis_size / 2), axis=axis)
#
#     # Compute the OTF
#     otf = np.fft.fft2(psf)
#
#     # Estimate the rough number of operations involved in the FFT
#     # and discard the PSF imaginary part if within roundoff error
#     # roundoff error  = machine epsilon = sys.float_info.epsilon
#     # or np.finfo().eps
#     n_ops = np.sum(psf.size * np.log2(psf.shape))
#     otf = np.real_if_close(otf, tol=n_ops)
#
#     return otf

def psf2otf(psf,size):
	import numpy as np
	if not(0 in psf):
		#Pad the PSF to outsize
		psf=np.double(psf)
		psfsize=np.shape(psf)
		psfsize=np.array(psfsize)
		padsize=size-psfsize
		psf=np.lib.pad(psf,((0,padsize[0]),(0,padsize[1])),'constant')
		#Circularly shift otf so that the "center" of the PSF is at the (1,1) element of the array.
		psf=np.roll(psf,-np.array(np.floor(psfsize/2),'i'),axis=(0,1))
		#Compute the OTF
		otf=np.fft.fftn(psf,axes=(0,1))
		#Estimate the rough number of operations involved in the computation of the FFT.
		nElem=np.prod(psfsize,axis=0)
		nOps=0
		for k in range(0,np.ndim(psf)):
			nffts=nElem/psfsize[k]
			nOps=nOps+psfsize[k]*np.log2(psfsize[k])*nffts
		mx1=(abs(np.imag(otf[:])).max(0)).max(0)
		mx2=(abs(otf[:]).max(0)).max(0)
		eps= 2.2204e-16
		if mx1/mx2<=nOps*eps:
			otf=np.real(otf)
	else:
		otf=np.zeros(size)
	return otf

def septRelSmo(I, lambda_, lb, hb, L1_0):
    if L1_0 is None:
        L1_0 = I
    N, M, D = np.shape(I)

    # f1_2d = np.pad(f1.reshape(1, -1), ((0, 1), (0, 0)), mode='constant')
    # f2_2d = np.pad(f2.reshape(-1, 1), ((0, 0), (0, 1)), mode='constant', constant_values=0)

    f1 = np.array([[1, -1]])

    f2 = np.array([[1], [-1]])

    f3 = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])


    sizeI2D = np.array([N, M])
    otfFx = psf2otf(f1, sizeI2D)
    otfFy = psf2otf(f2, sizeI2D)
    otfL = psf2otf(f3, sizeI2D)

    # Normin1 = np.tile(np.abs(otfL), (D, 1, 1)).transpose(1,2,0)**2 * np.fft.fft2(I)
    # matlab代码：Normin1 = repmat(abs(otfL),[1,1,D]).^2.*fft2(I);
    otfL_abs = np.abs(otfL)
    N1 = np.zeros((N, M, D), dtype=np.double)
    for i in range(D):
        N1[:, :, i] = otfL_abs
    Normin1 = N1
    Normin1 = Normin1**2 * np.fft.fft2(I)

    Denormin1 = np.abs(otfL) ** 2
    Denormin2 = np.abs(otfFx) ** 2 + np.abs(otfFy) ** 2

    if D > 1:
        D1 = np.zeros((N, M, D), dtype=np.double)
        for i in range(D):
            D1[:, :, i] = Denormin1
        Denormin1 = D1

        D2 = np.zeros((N, M, D), dtype=np.double)
        for i in range(D):
            D2[:, :, i] = Denormin2
        Denormin2 = D2

    eps = 1e-16
    L1 = L1_0

    thr = 0.05

    for i in range(1,4):
        beta = 2 ** (i - 1) / thr
        Denormin = lambda_ * Denormin1 + beta * Denormin2
        # f1_3t = np.tile(f1, (2, 1, 1))
        # f1_3d = np.zeros_like(f1_3t)
        # f1_3d[0] = f1
        f1_3d = np.zeros((2, 2, 2), dtype=f1.dtype)
        f1_3d[0] = f1

        # matlab代码
        # gFx = -imfilter(L1, f1, 'circular');
        # gFy = -imfilter(L1, f2, 'circular');
        ouputs_x = []
        bv = L1.shape[2]
        for i in range(bv):
            filt = L1[...,i]
            out = ndimage.convolve(filt,f1)
            ouputs_x.append(out)
        ouputs_x = np.dstack(ouputs_x)
        gFx = ouputs_x

        ouputs_y = []
        bv = L1.shape[2]
        for i in range(bv):
            filt = L1[..., i]
            out = ndimage.convolve(filt, f2)
            ouputs_y.append(out)
        ouputs_y = np.dstack(ouputs_y)
        gFy = ouputs_y


        # matlab代码：t = repmat(sum(abs(gFx),3)<1/beta,[1 1 D]);
        t = (np.sum(np.abs(gFx), axis=2) < 1 / beta)
        t1 = np.zeros((N,M,D),dtype=np.int64)
        for i in range(D):
            t1[:,:,i] = t
        t = t1
        t = t.astype(bool)
        # t = t.astype(int)
        gFx[t] = 0

        # matlab代码：t = repmat(sum(abs(gFy),3)<1/beta,[1 1 D]);
        t = (np.sum(np.abs(gFy), axis=2) < 1 / beta)
        t1 = np.zeros((N, M, D), dtype=np.int64)
        for i in range(D):
            t1[:, :, i] = t
        t = t1
        t = t.astype(bool)
        gFy[t] = 0

        # matlab代码：Normin2 = [gFx(:, end,:) - gFx(:, 1,:), -diff(gFx, 1, 2)];
        h1 = np.reshape(gFx[:,-1],(N,1,3))-np.reshape(gFx[:,0],(N,1,3))
        h2 = np.diff(gFx,1,1)
        Normin2 = np.hstack((h1, -h2))

        # matlab代码：Normin2 = Normin2 + [gFy(end,:,:) - gFy(1,:,:); -diff(gFy, 1, 1)];
        v1 = np.reshape(gFy[-1,:],(1,M,3)) - np.reshape(gFy[0,:],(1,M,3))
        v2 = np.diff(gFy,1,0)
        Normin2 = Normin2 + np.vstack((v1, -v2))

        FL1 = (lambda_ * Normin1 + beta * np.fft.fft2(Normin2,axes=(0,1))) / (Denormin + eps)
        L1 = np.real(np.fft.ifft2(FL1,axes=(0,1)))

        for c in range(D):
            L1t = L1[:, :, c]
            for k in range(500):
                # matlab代码：dt = (sum(L1t(L1t<lb(:,:,c)) ) + sum(L1t(L1t>hb(:,:,c)) ))*2/numel(L1t);
                sum_lower = np.sum(L1t[L1t < lb[:, :, c]])
                sum_higher = np.sum(L1t[L1t > hb[:, :, c]])
                num_elements = np.prod(L1t.shape)
                dt = (sum_lower + sum_higher) * 2 / num_elements
                L1t = L1t - dt
                if np.abs(dt) < 1 / np.size(L1t):
                    break
            L1[:, :, c] = L1t

        t = L1 < lb
        L1[t] = lb[t]
        t = L1 > hb
        L1[t] = hb[t]
        L2 = I - L1

    return L1, L2


save_dirG = './results_G/'
save_dirJ = './results_J/'
save_dirconcat = './light-effects-results/'

os.makedirs(save_dirG, exist_ok=True)
os.makedirs(save_dirJ, exist_ok=True)

imgname = '0805_lowLight_1'
input_i = np.array(Image.open('./light-effects/' + imgname + '.jpg'), dtype=np.float64) / 255
H, W, D = input_i.shape
J, _ = septRelSmo(input_i, 50, np.zeros((H, W, D)), input_i, None)
j, G = septRelSmo(input_i, 25000, np.zeros((H, W, D)), input_i, None)

if imgname == 'g':
    j, G = septRelSmo(input_i, 500, np.zeros((H, W, D)), input_i, None)

end_time = datetime.datetime.now()
print(f'程序耗时:{(end_time - start_time).seconds}秒')


# plt.figure(1)
# print(f'----Finish----')

plt.figure(1,dpi=112)
plt.axis('off')   # 去坐标轴
plt.xticks([])    # 去 x 轴刻度
plt.yticks([])    # 去 y 轴刻度

#
# x = np.concatenate((input_i, G, J*2), axis=1)
# plt.imshow(x)
# plt.savefig(save_dirconcat + imgname + '.jpg',dpi=500, bbox_inches='tight', pad_inches = 0)
# plt.show()

imgname = '0805_lowLight_1_dehaze_new'
input_after = np.array(Image.open('./light-effects/dehaze/' + imgname + '.jpg'), dtype=np.float64) / 255
# x = np.concatenate((input_after+G/20+J/10, G, J), axis=1)
x = input_after+G/10+J
plt.imshow(x)
# plt.savefig(save_dirconcat + imgname + '.jpg',dpi=112, bbox_inches='tight', pad_inches = 0)
plt.show()


# Image.fromarray((G * 2).astype(np.uint8)).save(save_dirG + imgname + '_G.jpg')
# Image.fromarray((J * 2).astype(np.uint8)).save(save_dirJ + imgname + '_J.jpg')
