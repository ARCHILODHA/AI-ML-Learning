import torch

def custom_loss(output, target):
    return torch.mean((output - target)**2 + 0.1 * torch.abs(output))

output = torch.tensor([2.0, 3.0])
target = torch.tensor([1.0, 2.0])

print(custom_loss(output, target))
