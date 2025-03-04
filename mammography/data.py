#!/usr/bin/env python3

import torch
from pathlib import Path
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from torchvision.io import read_image
import matplotlib.pyplot as plt



IMAGE_DIR = Path('../raw_data/data')
IMAGE_ANNOTATIONS_TRAIN = IMAGE_DIR / f'train_image_annotations.csv'
IMAGE_ANNOTATIONS_VAL = IMAGE_DIR / f'val_image_annotations.csv'
IMAGE_ANNOTATIONS_TEST = IMAGE_DIR / f'test_image_annotations.csv'


class MammogramDataset(Dataset):
    """Retrieves dataset’s features and labels one sample at a time."""
    def __init__(self, image_directory, annotations_file, transform=None, target_transform=None):
        self.image_directory = image_directory
        self.image_labels = pd.read_csv(annotations_file)
        self.transform = transform  # padding etc, check out within pytorch
        self.target_transform = target_transform
      
    
    def __len__(self):
        return len(self.image_labels)
     
    
    def __getitem__(self, index):
        image_path =  Path(self.image_directory / self.image_labels.iloc[index, 0])
        image = read_image(image_path)  # converts that to a tensor
        label = self.image_labels.iloc[index, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
            

def show_images():
    pass


if __name__ == "__main__":
    pass