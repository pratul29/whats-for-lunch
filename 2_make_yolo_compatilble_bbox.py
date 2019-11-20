import os
import json
import csv
import shutil
from helper import remove_hidden_folder
from variables import *

def convert_yolo_bbox(img_size, box, category):
    dw = 1./img_size[0]
    dh = 1./img_size[1]
    x = (int(box[0]) + int(box[2]))/2.0
    y = (int(box[1]) + int(box[3]))/2.0
    w = abs(int(box[2]) - int(box[0]))
    h = abs(int(box[3]) - int(box[1]))
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh

    return [category, x, y, w, h]

def handle_annotations(item_list):
    for ingredient in item_list:
        annotation_list = os.listdir(f"{images_bbox_directory}/{ingredient}/{ann}")
        annotation_list = remove_hidden_folder(annotation_list)
        
        category = int(annotation_list[0][:annotation_list[0].index("-")])
        print("Category", category)

        for file_name in annotation_list:
            print("Input file name", file_name)
            target_file_name = file_name[:file_name.index(".")] + ".txt"
            print("Target file name", target_file_name)

            bbox_details = json.load(
                open(f"{images_bbox_directory}/{ingredient}/{ann}/{file_name}", "r"))

            image_height = bbox_details[size][height]
            image_width = bbox_details[size][width]

            all_bboxes = bbox_details[objects]

            yolo_bbox_list = []

            for bbox in all_bboxes:
                bbox_coordinates = bbox[points][exterior]
                top_left = bbox_coordinates[0]
                bottom_right = bbox_coordinates[1]

                print("Original_points", image_height,
                    image_width, top_left, bottom_right)
                yolo_bbox = convert_yolo_bbox((image_width, image_height),
                                            (top_left[0], top_left[1], bottom_right[0], bottom_right[1]), category)
                print("Yolo_points", yolo_bbox)

                yolo_bbox_list.append(yolo_bbox)

            # write yolo_bbox_list
            csv_writer_object = csv.writer(
                open(f"{all_image_details_directory}/{target_file_name}", "w+"), delimiter=" ")
            csv_writer_object.writerows(yolo_bbox_list)

            print("="*50)


def handle_images(item_list):
    for ingredient in item_list:
        image_list = os.listdir(f"{images_bbox_directory}/{ingredient}/{img}")
        image_list = remove_hidden_folder(image_list)

        for image in image_list:
            print(f"Copying {images_bbox_directory}/{ingredient}/{img}/{image}")
            shutil.copy(f"{images_bbox_directory}/{ingredient}/{img}/{image}", all_image_details_directory)


# variables defined in file variables.py
if not os.path.isdir(all_image_details_directory):
    os.mkdir(all_image_details_directory)

item_list = [d for d in os.listdir(images_bbox_directory) if os.path.isdir(os.path.join(images_bbox_directory, d))]
item_list = sorted(remove_hidden_folder(item_list))

item_list = remove_hidden_folder(item_list)

print("Handling Annotations")
handle_annotations(item_list)
print("Handling Images")
handle_images(item_list)