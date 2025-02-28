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
ROOT_DIR = 'raw_data/vtb-balanced-patients-202107091800'
ROOT_JSON = 'raw_data/vtb.balanced-patients.202107091800.json',
OUT_DIR = 'raw_data/data'
IMAGE_ANNOTATIONS = '/raw_data/annotaions.json'
TRAIN_SIZE = 0.7

def split_directory_names():
    """
        Train-val-test split of patients' directory names:
        since the images from the same patient shall remain within the same group (train, validation or test),
        shuffle the names of the directories, split them (70-15-15), and return them.
    """
    # Make train, vali and test directories
    for dirname in ['train', 'validation', 'test']:
        os.makedirs('/'.join([OUT_DIR, dirname]), exist_ok=True)
    
    
    # Get every patient's directory
    allPatientDirNames = [f for f in os.listdir(ROOT_DIR) if f.startswith('vtb')] # helps avoid hidden files and directories
    
    # Shufffle all the directories
    np.random.shuffle(allPatientDirNames)
    
    # Split all the directories
    ts = int(TRAIN_SIZE * len(allPatientDirNames)) # size of train 
    vs = (len(allPatientDirNames) - ts) // 2 # size of val (and test)
    train_DirNames, val_DirNames, test_DirNames = allPatientDirNames[:ts], allPatientDirNames[ts:ts+vs], allPatientDirNames[ts+vs:]
    
    return train_DirNames, val_DirNames, test_DirNames
    
    
    
def split_train_val_test(train_DirNames, val_DirNames, test_DirNames):
    """
        Copies the (original high-resolution) images to respective train, validation and test folders, 
        images from the same patient remain in the same group (i.e in train, validatoin or test folder)
        #and generates json file indicating the groups each image sample belongs to
        and generates a CVS file containing each image and its class ("CC" or "MLO")
    """
    
    # uid = "2.16.250.828871699.0.8.66439853151992126525607928262870674476065"
    # uid = uid.split(sep=".")[-1]
    # uid = '.'.join([uid, 'dcm', 'png'])
    # uid
    




if __name__ == "__main__":
    train, val, test = split_directory_names()
    print(f'len(train) = {len(val)}')
        