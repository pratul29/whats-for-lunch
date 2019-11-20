from google_images_download import googleimagesdownload
import os
import json

ingredients_file = "ingredients.json"
number_of_images = 50
dowload_path = "Images"

ingredients_file_handler = open(ingredients_file, "r")
all_items = json.load(ingredients_file_handler)
all_items_length = len(all_items)

item_count = 0

for item in all_items:
    item_count = item_count + 1
    print(f"{item_count}. Out of {all_items_length}")

    ingredient = item['ingredient']
    descriptor = item['descriptor'][0]

    search_query = f"{ingredient} {descriptor}".strip()
    folder_name = '_'.join(ingredient.split())

    print("Search Query", search_query, sep=": ")

    exists = os.path.exists(f"{dowload_path}/{folder_name}")

    if not exists:
        print("Folder Name", folder_name, sep=": ")

        response = googleimagesdownload()
        absolute_image_paths = response.download({
            "keywords": search_query,
            "limit": number_of_images,
            "image_directory": folder_name,
            "output_directory": dowload_path
        })

    else:  # folder exists skipping
        stmt = f"Skipping... Folder for {ingredient} exists - {dowload_path}/{folder_name}"
        print(stmt)

    print("=" * 50)
