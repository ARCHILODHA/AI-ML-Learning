import torch

model = torch.nn.Linear(10, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for _ in range(5):
    data = torch.randn(1, 10)
    target = torch.randn(1, 1)

    output = model(data)
    loss = (output - target).pow(2).mean()

    optimizer.zero_grad()
    loss.backward()

    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

    optimizer.step()
