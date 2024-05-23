cl_lambda = 0.25

def curriculum_weight_change(d_psnr, d_ssim):
    # 两个方法的圆心
    osfd_center = [20.7, 0.84]
    gapsf_center = [24.5, 0.86]

    print(f'd_psnr:{d_psnr}|d_ssim:{d_ssim} ')

    # OSFD--20.70396511--0.848472203
    # GAPSF--24.5695557--0.869527416
    # 根据当前坐标计算距离两个方法的位置距离
    dis_osfd = pow(pow(d_psnr - osfd_center[0], 2) + pow(d_ssim - osfd_center[1], 2), 0.5)
    dis_gapsf = pow(pow(d_psnr - gapsf_center[0], 2) + pow(d_ssim - gapsf_center[1], 2), 0.5)
    print(f'dis_osfd:{dis_osfd}')
    print(f'dis_gapsf:{dis_gapsf}')

    # 结合阈值和坐标确定权重大小（推力）, 推力系数cl_lambda = 0.25
    weights = []
    weights.append(abs((1 + cl_lambda + pow(dis_osfd, -1))))
    weights.append(abs((1 - cl_lambda + pow(dis_gapsf, -1))))
    weights.append(2)
    new_weights = [i / sum(weights) for i in weights]
    return new_weights

if __name__ == '__main__':

    max_psnr = 0
    max_ssim = 0

    # ssims = [0.6741, 0.7243, 0.8571, 0.8967, 0.8888, 0.9004]
    # psnrs = [18.7642, 19.0021, 22.7131, 23.0937, 24.0445, 25.1437]

    psnrs = [0,22.7131, 23.0937, 24.0445, 25.1437, 25.0545, 26.6331, 26.6895, 26.8978, 26.9570, 26.6597, 27.5399, 27.8892,
             27.3261, 27.3252, 26.9674, 27.5339]
    ssims = [0,0.8571,0.8967,0.8888,0.9004,0.9142,0.9265,0.9326,0.9372,0.9282,0.9200,0.9367,0.9405,0.9248,0.9317,0.9249,0.9324]


    for psnr_eval, ssim_eval in zip(psnrs, ssims):
        print(f'--------------------------------------------')
        weights = curriculum_weight_change(psnr_eval, ssim_eval)
        if ssim_eval > max_ssim and psnr_eval > max_psnr:
            max_ssim = max(max_ssim, ssim_eval)
            max_psnr = max(max_psnr, psnr_eval)
            print(f'##Save_model AND Change_weight##')
            print(f'  max_psnr:{max_psnr:.4f}|max_ssim:{max_ssim:.4f} ')
            print(f'n1_weight:{weights[0]}| n2_weight:{weights[1]}| inp_weight:{weights[2]}')
        else:
            print(f'n1_weight:{weights[0]}| n2_weight:{weights[1]}| inp_weight:{weights[2]}')
        print(f'--------------------------------------------')
