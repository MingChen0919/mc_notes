import torch
import torch.nn.functional as F


num_samples = 10
num_inputs = 3
X = torch.randn((num_samples, num_inputs))
W1 = torch.randn((num_inputs, 4), requires_grad=True)
b1 = torch.randn((1, 4), requires_grad=True)
Z1 = torch.matmul(X, W1) + b1
A1 = F.sigmoid(Z1)

W2 = torch.randn((4, 1), requires_grad=True)
b2 = torch.randn((1, 1), requires_grad=True)
Z2 = torch.matmul(Z1, W2) + b2
A2 = F.relu(Z2)

A2.backward(A2)

print(W1.grad)
print(b1.grad)
print(W2.grad)
print(b2.grad)


X = torch.tensor([[1, 1, 1], [2, 2, 2]], dtype=torch.float32)
W = torch.randn(size=(3, 4), requires_grad=True)
print(X)
print(W)
Z = torch.matmul(X, W)
print(Z)
Z.backward(Z)
print(W.grad)
print(X.grad)