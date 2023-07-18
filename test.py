import torch

max_len = 5

position = torch.arange(0, max_len, dtype=torch.float)
print(position)
position = position.unsqueeze(1)
print(position)

print(-1e9)