import torch
print("CuDNN available:", torch.backends.cudnn.enabled)
print(torch.cuda.is_available())  # 检查是否有可用的 CUDA 设备
print(torch.version.cuda)          # 检查 PyTorch 支持的 CUDA 版本
