import torch
import torch.nn as nn
import numpy as np
import random

num_inputs = 2
num_samples = 1000


def synthesize_data(num_inputs, num_samples):
    true_w = torch.zeros(size=(num_inputs,)).normal_()
    true_b = torch.randn(1)
    features = torch.randn(size=(num_samples, num_inputs))
    labels = torch.matmul(features, true_w) + true_b + torch.normal(0, 1, size=(num_samples,))

    return features, labels, true_w, true_b


features, labels, true_w, true_b = synthesize_data(num_inputs, num_samples)


# create data generator
def data_generator(batch_size, features, labels):
    num_samples = features.shape[0]
    indices = list(range(num_samples))
    random.shuffle(indices)
    for i in range(0, num_samples, batch_size):
        batch_indices = indices[i: min(i + batch_size, num_samples)]
        yield features[batch_indices], labels[batch_indices]


# for X, y in data_generator(5, features, labels):
#     print(X, y)
#     break


# define model
class LinearRegressionNet(nn.Module):
    def __init__(self, num_inputs):
        super(LinearRegressionNet, self).__init__()
        self.l1 = nn.Linear(num_inputs, 1, bias=True)

    def forward(self, x):
        y_pred = self.l1(x)
        return y_pred


net = LinearRegressionNet(num_inputs=num_inputs)

# define loss function
loss_func = torch.nn.MSELoss(reduction='mean')

# define optimization algorithm
optim = torch.optim.SGD(net.parameters(), lr=0.03)

# training loop
# net.l1.weight.data = torch.Tensor(np.random.normal(size=(1, num_inputs), scale=0.01, loc=0))
# net.l1.bias.data = torch.Tensor([0])
num_epochs = 1000
batch_size = 20
for epoch in range(num_epochs):
    for X, y in data_generator(batch_size, features, labels):
        pred_y = net(X)
        loss = loss_func(pred_y, y.reshape(pred_y.shape))
        optim.zero_grad()  # set gradients to zeros
        loss.backward()  # calculate gradients
        optim.step()  # update parameters with calculated gradients

    with torch.no_grad():
        epoch_loss = loss_func(net(features), labels)
        print('epoch {}, loss {}'.format(epoch + 1, epoch_loss))


print(list(net.parameters()))
print(true_w)
print(true_b)