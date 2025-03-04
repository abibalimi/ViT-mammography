#!/usr/bin/env python3

import json
import shutil
import random
from pathlib import Path
from utils import dict_to_csv


# Creating Train / Test folders (One time use)
ROOT_DIR = Path('raw_data/vtb-balanced-patients-202107091800')
ROOT_JSON = Path('raw_data/vtb.balanced-patients.202107091800.json')
OUT_DIR = Path('raw_data/data')
IMAGE_ANNOTATIONS_TRAIN = OUT_DIR / f'train_image_annotations.csv'
IMAGE_ANNOTATIONS_VAL = OUT_DIR / f'val_image_annotations.csv'
IMAGE_ANNOTATIONS_TEST = OUT_DIR / f'test_image_annotations.csv'
TRAIN_SIZE = 0.7
    

    
def split_train_val_test():
    """
        Splits and copies the (original high-resolution) images to respective train, validation and test folders
        while images from the same patient remain in the same group (i.e in train, validatoin or test folder)
        and generates a Cval_size file containing annotations: images and labels ("CC" or "MLO").
    """
    
    # Make training, validation and test working directories
    for split in ['train', 'validation', 'test']:
        (OUT_DIR / split).mkdir(parents=True, exist_ok=True)
        
        
    # Split patients' directory names into training, validation and test
    train_dirs, val_dirs, test_dirs = split_directory_names()
    
    # Split into working datasets
    # Load JSON file
    with ROOT_JSON.open() as infile:
        data = json.load(infile)
        
    # Prepare lists to contain annotations
    train_dico, val_dico, test_dico = [], [], []
    
    # Mapping dataset names to their corresponding sets and annotation lists
    dataset_map = {
        "train": (train_dirs, train_dico),
        "validation": (val_dirs, val_dico),
        "test": (test_dirs, test_dico),
    }
    
    # Determine dataset split and copy images
    for key, details in data.items():
        accession_number = details['accessionNumber'] # Patient's directory name
        label = details['view'] 
        image_uid = details['uid']
        
        # Extract the final part of the UID as the image file name
        image_file = f"{image_uid.split(sep='.')[-1]}.dcm.png"
        
        # Determine dataset split and copy images
        for dataset_name, (dir_set, annotation_list) in dataset_map.items():
            if accession_number in dir_set:
                annotation_list.append({"image": image_file, "label": label})
                copy_image_to_folder(accession_number, image_uid, dataset_name, image_file)
                break  # Exit loop once a match is found
    
            
    # generate annotations in .csv files
    dict_to_csv(dico=train_dico, headers=['image', 'label'], file_name=IMAGE_ANNOTATIONS_TRAIN) # train 
    dict_to_csv(dico=val_dico, headers=['image', 'label'], file_name=IMAGE_ANNOTATIONS_VAL) # validation 
    dict_to_csv(dico=test_dico, headers=['image', 'label'], file_name=IMAGE_ANNOTATIONS_TEST) # test



def split_directory_names():
    """
        Splits patient directories into train, validation and test sets.
        Ensures all images from the same patient remain in the same dataset.
    """
    # Get patient directory names while avoiding hidden files
    patient_dirs = [d.name for d in ROOT_DIR.iterdir() if d.is_dir() and d.name.startswith("vtb")]

    # Shufffle directories
    random.shuffle(patient_dirs)
    
    # Train-Val-Test Split (70-15-15)
    train_size = int(TRAIN_SIZE * len(patient_dirs)) # size of train 
    val_size = (len(patient_dirs) - train_size) // 2 # size of val (and test)
    
    return (
        patient_dirs[:train_size], # train_dirs
        patient_dirs[train_size : train_size + val_size], # validation_dirs
        patient_dirs[train_size + val_size:] # test_dirs
    )


def copy_image_to_folder(accession_number: str, image_uid: str, dataset_name: str, image_file: str):
    """
    Copies an image file from the patient's folder to the respective dataset folder.
    
    Args:
        accession_number (str): The unique identifier for the patient's folder.
        image_uid (str): The UID of the image to be copied, used to construct the full image path.
        dataset_name (str): The name of the target dataset folder (e.g., 'train', 'validation', 'test').
        image_file (str): The name of the image file to be saved in the target dataset folder.

    """
    source_path = ROOT_DIR / accession_number / f"{image_uid}.dcm.png"
    destination_path = OUT_DIR / dataset_name / image_file

    shutil.copy(source_path, destination_path)
         
         
if __name__ == "__main__":
    split_train_val_test()
        
