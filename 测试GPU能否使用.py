import torch
print(f'is_available: {torch.cuda.is_available()}') # 查看CUDA是否可用
print(f'device_count: {torch.cuda.device_count()}') # 查看可用的CUDA数量
print(f'version.cuda: {torch.version.cuda}') # 查看CUDA的版本号