import os
import random
import shutil

base_path = "Database1/Database1" # Add ypur dataset path here
image_exts = ['.jpg', '.jpeg', '.png']
image_dir = os.path.join(os.getcwd(), base_path)

output_img_train = os.path.join("images", "train")
output_img_val = os.path.join("images", "val")
output_lbl_train = os.path.join("labels", "train")
output_lbl_val = os.path.join("labels", "val")

for folder in [output_img_train, output_img_val, output_lbl_train, output_lbl_val]:
    os.makedirs(folder, exist_ok=True)

image_files = [f for f in os.listdir(image_dir) if os.path.splitext(f)[1].lower() in image_exts]

random.shuffle(image_files)
split_idx = int(0.8 * len(image_files))
train_images = image_files[:split_idx]
val_images = image_files[split_idx:]

def copy_files(file_list, img_dst, lbl_dst):
    for img_file in file_list:
        name, _ = os.path.splitext(img_file)
        img_src = os.path.join(image_dir, img_file)
        lbl_src = os.path.join(image_dir, f"{name}.txt")

        # Only proceed if label file exists
        if os.path.exists(lbl_src):
            shutil.copy(img_src, os.path.join(img_dst, img_file))
            shutil.copy(lbl_src, os.path.join(lbl_dst, f"{name}.txt"))

copy_files(train_images, output_img_train, output_lbl_train)
copy_files(val_images, output_img_val, output_lbl_val)

print("Dataset successfully split into train and val sets.")
