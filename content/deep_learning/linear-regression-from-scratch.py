import torch
import random

# Generating data sets using formula y = 2.5 * x1 - 1.5 x2 + 1.8
# add some noise to the generated labels (std = 0.01)
num_inputs = 2
num_examples = 1000
true_w = torch.tensor([2.5, -1.5])
true_b = 1.8
features = torch.zeros(size=(num_examples, num_inputs)).normal_(1, 2)
labels = torch.matmul(features, true_w) + true_b
labels += torch.zeros(size=labels.shape).normal_(std=0.01)


# ----- create data generator --------
def data_generator(batch_size, features, labels):
    num_examples = features.shape[0]
    indices = list(range(num_examples))
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = indices[i: min(i + batch_size, num_examples)]
        yield features[batch_indices], labels[batch_indices]


batch_size = 10
for X, y in data_generator(batch_size, features, labels):
    print(X, y)
    break


# -------- Define the Model -------
def linear_reg(X, w, b):
    return torch.matmul(X, w) + b


# -------- Define the Loss Function -------
def squared_loss(y_hat, y):
    """
    The constant 1/2 is just for mathematical convenience, ensuring that after we take the derivative of the loss,
    the constant coefficient will be 1.
    """
    return (1 / 2) * (y_hat - y.reshape(y_hat.shape)) ** 2


# Define the Optimization
def sgd(params, lr, batch_size):
    for param in params:
        param.data.sub_(lr * param.grad / batch_size)  # param = param - gradient
        param.grad.data.zero_()  # set gradient to zero


# ----- training ------
lr = 0.03
num_epochs = 100
net = linear_reg
loss_func = squared_loss

# initial model parameters
w = torch.zeros(size=(num_inputs, 1)).normal_(std=0.01)
b = torch.zeros(size=(1,))

# configure automatic gradient
w.requires_grad_(True)
b.requires_grad_(True)

for epoch in range(num_epochs):
    for X, y in data_generator(batch_size, features, labels):
        loss = loss_func(net(X, w, b), y)
        loss.mean().backward()  # calculate gradient
        sgd([w, b], lr, batch_size)

    with torch.no_grad():
        train_loss = loss_func(net(features, w, b), labels)
        print('epoch {}, loss {}'.format(epoch + 1, train_loss.mean().numpy()))
