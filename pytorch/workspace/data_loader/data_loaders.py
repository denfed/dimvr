from torchvision import datasets, transforms
from base import BaseDataLoader
from .data_sets import DIMLDataset
from utils import random_squarecropper


class MnistDataLoader(BaseDataLoader):
    """
    MNIST data loading demo using BaseDataLoader
    """
    def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
        trsfm = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
        self.data_dir = data_dir
        self.dataset = datasets.MNIST(self.data_dir, train=training, download=True, transform=trsfm)
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)


class DIMLDataLoader(BaseDataLoader):
    """
    First testing dataloader for the DIML training dataset
    """
    def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
        transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.ToTensor()
        ])
        self.data_dir = data_dir
        self.cropper = random_squarecropper
        self.dataset = DIMLDataset(data_dir, transform=transform, cropper=random_squarecropper)
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)