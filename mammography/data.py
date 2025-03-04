#!/usr/bin/env python3

import torch
from pathlib import Path
from torch.utils.data import Dataset, DataLoader
from torchvision.io import read_image
import matplotlib.pyplot as plt



IMAGE_DIR = Path('raw_data/data')
IMAGE_ANNOTATIONS_TRAIN = 'raw_data/train_image_annotations.csv'
IMAGE_ANNOTATIONS_VAL = 'raw_data/val_image_annotations.csv'
IMAGE_ANNOTATIONS_TEST = 'raw_data/test_image_annotations.csv'


class MammogramDataset(Dataset):
    def __init__(self, image_directory, image_labels, transform=None, target_transform=None):
        self.image_directory = image_directory
        self.image_labels = image_labels
        self.transform = transform  # padding etc, check out within pytorch
        self.target_transform = target_transform
      
    
    def __len__(self):
        return len(self.image_labels)
     
    
    def __getitem__(self, index):
        image_path = os.path.join(self.image_directory, self.image_labels)
        image = read_image(image_path)
        label = self.image_labels[index]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
            

def show_images():
    pass


if __name__ == "__main__":
    pass
