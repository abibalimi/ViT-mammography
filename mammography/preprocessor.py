#!/usr/bin/env python3

import os
import json
import shutil
import numpy as np
from torchvision.io import read_image
from PIL import Image
from utils import dict_to_csv

# Creating Train / Test folders (One time use)
ROOT_DIR = 'raw_data/vtb-balanced-patients-202107091800'
ROOT_JSON = 'raw_data/vtb.balanced-patients.202107091800.json'
OUT_DIR = 'raw_data/data'
IMAGE_ANNOTATIONS_TRAIN = 'raw_data/train_image_annotations.csv'
TRAIN_SIZE = 0.7


def split_directory_names():
    """
        Train-val-test split of patients' directory names:
        since the images from the same patient shall remain within the same group (train, validation or test),
        shuffle the names of the directories, split them (70-15-15), and return them.
    """
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
        Copies the (original high-resolution) images to respective train, validation and test folders
        while images from the same patient remain in the same group (i.e in train, validatoin or test folder)
        and generates a CVS file containing annotations: images and labels ("CC" or "MLO")
    """
    
    # Make train, vali and test directories
    for dirname in ['train', 'validation', 'test']:
        os.makedirs(os.path.join(OUT_DIR, dirname), exist_ok=True)
    

    # Opening JSON file
    with open(ROOT_JSON) as infile:
        data = json.load(infile)
        
        # list of dictionaries to be converted to CSV to contain annotations
        train_dico = []
        val_dico = []
        test_dico = []
        
        for key in data:
            accessionNumber = data[key]['accessionNumber'] # Patient's directory name
            label = data[key]['view'] # Future image label
            long_image_file = data[key]['uid'] # Future image file name
            
            # split uid and get the last string as image file name
            image_file = long_image_file.split(sep='.')[-1]
            image_file = '.'.join([image_file,'dcm','png'])
            
            # append annotations to list
            #dico.append({'image' : image_file, 'label' : label})
            
            # copy train_DirNames images to train group
            if accessionNumber in train_DirNames:
                # append annotations to train list
                train_dico.append({'image' : image_file, 'label' : label})
                copy_image_to_folder(accessionNumber, long_image_file, 'train', image_file)
        
          
        # generate annotations in .csv files
        # train
        dict_to_csv(dico=train_dico, headers=['image', 'label'], file_name=IMAGE_ANNOTATIONS_TRAIN)
        

def copy_image_to_folder(accessionNumber, long_image_file, split_dir, image_file):
    long_image_file = '.'.join([long_image_file, 'dcm', 'png'])
    shutil.copy(os.path.join(ROOT_DIR,accessionNumber,long_image_file), 
                                        os.path.join(OUT_DIR,split_dir,image_file))
         
         
if __name__ == "__main__":
    train, val, test = split_directory_names()
    print(f'len(train) = {len(val)}')
    
    split_train_val_test(train, val, test)
        
