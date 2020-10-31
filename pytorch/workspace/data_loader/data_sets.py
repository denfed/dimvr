import torch.utils.data as data
import os
import cv2
import numpy as np
import torch

class DIMLDataset(data.Dataset):
    """
    Dataset for the DIML Dataset
    """
    def __init__(self, data_dir, transform=None, cropper=None):
        """
        The incoming data_dir should contain the four locations:
        """
        self.data_dir = data_dir
        self.transform = transform
        self.cropper = cropper
        data_arr = []

        for root in os.listdir(data_dir):
            location_dir = os.path.join(data_dir, root)
            for image in os.listdir(os.path.join(location_dir, "color")):
                base_image = image[:-5]
                color_image = os.path.join(location_dir, "color") + "/" + image
                depth_filled = os.path.join(location_dir, "depth_filled") + "/" + base_image + "depth_filled.png"
                data_arr.append({"color": color_image, "depth": depth_filled})

        self.data_arr = data_arr

    def __len__(self):
        return len(self.data_arr)

    def __getitem__(self, idx):
        item = self.data_arr[idx]

        color = cv2.imread(item['color'])
        color = cv2.resize(color, (512, 512))
        copy_color = np.copy(color)
        copy_color = np.moveaxis(copy_color, -1, 0)
        copy_color = torch.Tensor(copy_color)
        # depth = cv2.imread(item['depth'])
        
        if self.transform is not None:
            color = self.transform(color)
            copy_color = self.transform(copy_color)
        
        color_cropped = self.cropper(color)
        
        return color_cropped, copy_color

