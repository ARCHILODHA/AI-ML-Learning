import torch
import torch.nn as nn

layer = nn.Linear(10, 5)

# Xavier Initialization
nn.init.xavier_uniform_(layer.weight)

print(layer.weight)
