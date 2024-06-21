import os
from PIL import Image


def crop_image(image_path, output_folder, crop_box):
    with Image.open(image_path) as img:
        cropped_img = img.crop(crop_box)

        os.makedirs(output_folder, exist_ok=True)

        file_name = os.path.basename(image_path)
        new_file_name = f"emoji_{file_name}"

        output_path = os.path.join(output_folder, new_file_name)

        cropped_img.save(output_path)


def process_images(directory, crop_box):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(root, file_name)

                output_folder = os.path.join(root, 'cropped_images')

                crop_image(image_path, output_folder, crop_box)


while True:
    if __name__ == "__main__":
        directory_path = input("Please enter the path where the HD Head Textures are stored: ")

        crop_size = int(input("Enter the crop height/width: "))
        crop_x = int(input("Enter the X coordinate to start cropping: "))
        crop_y = int(input("Enter the Y coordinate to start cropping: "))

        # (left, upper, right, lower)
        crop_box = (crop_x, crop_y, crop_x + crop_size, crop_y + crop_size)

        process_images(directory_path, crop_box)

        print("Image processing complete.")
