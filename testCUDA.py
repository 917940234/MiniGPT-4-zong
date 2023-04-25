import torch

print("cuda是否存在", torch.cuda.is_available())
print("cudnn版本号:", torch.backends.cudnn.version())
print("pytorch版本号:", torch.__version__)
print("cuda版本号:", torch.version.cuda)