#!/usr/bin/env python3

import os
import json
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchvision.io import read_image


class MammoImageDataset(Dataset):
    def __init__(self, image_directory, image_labels, transform=None, target_transform=None):
        self.image_directory = "asbolute_or_relative_image_dir_path_from_json"
        self.image_labels = "labels_from_json" # check out how to extract labels i.e "view" from json as dico (check old)
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
            

if __name__ == "__main__":
    pass