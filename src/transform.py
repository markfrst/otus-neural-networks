import torch
from torch import utils
from torchvision import datasets, transforms

path = './MNIST_data'

class CustomTransform():
    def __init__(self, base_mean, base_std):
        self.base_mean = base_mean
        self.base_std = base_std
        pass

    def __call__(self, tensor):
        return (tensor - self.base_mean) / self.base_std


def mnist(batch_size=20, shuffle=False, path='./MNIST_data'):
    base_data = datasets.MNIST(
        path, train=True, download=True, transform=transforms.ToTensor())

    base_data_loader = utils.data.DataLoader(base_data, batch_size=60000)
    base_list = next(iter(base_data_loader))

    base_mean = torch.mean(base_list[0].flatten()).item()
    base_std = torch.std(base_list[0].flatten()).item()

    transform = transforms.Compose([
        transforms.ToTensor(),
        CustomTransform(base_mean, base_std),
    ])

    train_data = datasets.MNIST(
        path, train=True, download=True, transform=transform)
    train_loader = utils.data.DataLoader(
        train_data, batch_size=batch_size, shuffle=shuffle)

    print("Tensor mean: %f" % torch.mean(train_data[0][0]))
    print("Tensor std: %f" % torch.std(train_data[0][0]))

    return train_loader


mnist()


# RESULT:
# Tensor mean: 0.022777
# Tensor std: 1.014410
