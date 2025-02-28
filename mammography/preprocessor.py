#!/usr/bin/env python3

import os
import json
import shutil
import numpy as np
from torchvision.io import read_image
from PIL import Image


def uploadImages(images_dir = "", out_dir = "", source_json = ""):
    # get images 
    
    
    # for each image, 
    #   get last splitted uid string 
    #   join dcm and png
    pass


# Creating Train / Test folders (One time use)
root_dir = 'raw_data/vtb-balanced-patients-202107091800'
out_dir = 'raw_data/data'


def split_directory_names(root_dir = root_dir, 
                            out_dir = out_dir,
                            train_size = 0.7):
    """
        Train-val-test split of patients' directory names:
        since the images from the same patient shall remain within the same group (train, validation or test),
        shuffle the names of the directories, split them (70-15-15), and return them.
    """
    # Make train, vali and test directories
    for dirname in ['train', 'validation', 'test']:
        os.makedirs('/'.join([out_dir, dirname]), exist_ok=True)
    
    
    # Get every patient's directory
    allPatientDirNames = [f for f in os.listdir(root_dir) if f.startswith('vtb')] # helps avoid hidden files and directories
    
    # Shufffle all the directories
    np.random.shuffle(allPatientDirNames)
    
    # Split all the directories
    ts = int(train_size * len(allPatientDirNames)) # size of train 
    vs = (len(allPatientDirNames) - ts) // 2 # size of val (and test)
    train_DirNames, val_DirNames, test_DirNames = allPatientDirNames[:ts], allPatientDirNames[ts:ts+vs], allPatientDirNames[ts+vs:]
    
    return train_DirNames, val_DirNames, test_DirNames
    
    




if __name__ == "__main__":
    split_train_val_test(root_dir, out_dir)
        