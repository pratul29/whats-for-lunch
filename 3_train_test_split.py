import os
import glob
from variables import *

train_file_handler = open(training_image_list_file, 'w')
test_file_handler = open(testing_image_list_file, 'w')

all_image_list = glob.glob(f"{all_image_details_directory}/*.jpg")

prepend = "/content/data_for_colab"
idx = round(len(all_image_list) / test_split_ratio)

idx_counter = 1
for file in all_image_list:
    if idx_counter == idx:
        idx_counter = 1
        test_file_handler.write(f"{prepend}/{file}\n")

    else:
        idx_counter += 1
        train_file_handler.write(f"{prepend}/{file}\n")