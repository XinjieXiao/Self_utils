
# 本代码要嵌入运行代码中使用，在加载时替换为正确的权重表达，以解决由于分布式训练，但单卡预测时造成的权重读取错误，此处只作为一个示范

model_resnet101 = get_net()
model_resnet101.cuda()
model_resnet101.load_state_dict({k.replace('module.',''):v for k,v in torch.load("densenet169_rnn_fold_1_model_best_f1.pth.tar")['state_dict'].items()})



# 以下为成功使用的C2PNet例子
net = C2PNet(gps=3, blocks=19)
net = net.to(device)
net.load_state_dict({k.replace('module.',''):v for k,v in torch.load(model_dir)['model'].items()})
net.eval()