import os
from helper import remove_hidden_folder
from variables import *

item_list = [d for d in os.listdir(images_bbox_directory) if os.path.isdir(os.path.join(images_bbox_directory, d))]
item_list = sorted(remove_hidden_folder(item_list))

for pos in range(len(item_list)):
    ingredient = item_list[pos]
    if ingredient != "":
        image_list = os.listdir(f"{images_bbox_directory}/{ingredient}/{img}")
        annotation_list = os.listdir(f"{images_bbox_directory}/{ingredient}/{ann}")

        image_list = sorted(remove_hidden_folder(image_list))
        annotation_list = sorted(remove_hidden_folder(annotation_list))

        for image_name, annotation_name in zip(image_list, annotation_list):
            idx_ = image_name[:image_name.index(".")]

            new_image_name = f"{pos}-{ingredient}-{idx_}.jpg"
            new_annotation_name = f"{pos}-{ingredient}-{idx_}.jpg.json"

            print(f"Renaming image file {image_name} to {new_image_name}")
            os.rename(f"{images_bbox_directory}/{ingredient}/img/{image_name}",
                      f"{images_bbox_directory}/{ingredient}/img/{new_image_name}")

            print(f"Renaming annotation file {annotation_name} to {new_annotation_name}")
            os.rename(f"{images_bbox_directory}/{ingredient}/ann/{annotation_name}",
                      f"{images_bbox_directory}/{ingredient}/ann/{new_annotation_name}")