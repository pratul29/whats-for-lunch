# images_bbox contains - all ingredient names (eg. bellpepper) subfolders - bellpepper/ann bellpepper/img
images_bbox_directory = "images_bbox"
# subfolders in each ingredient after downloading from supervisely
img = "img"
ann = "ann"
# bbox json file, contents
size = "size"
height = "height"
width = "width"
objects = "objects"
points = "points"
exterior = "exterior"
# multi_image_details directory contains all images and corresponding bboxs in YOLO format
all_image_details_directory = "multi_image_details"
# train - test split definations
training_image_list_file = "train.txt"
testing_image_list_file = "test.txt"
test_split_ratio = 20