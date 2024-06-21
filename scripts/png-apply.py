import os


def append_png(directory):
    # Loop through all subdirectories and files
    for root, _, files in os.walk(directory):
        for file_name in files:
            # Check if the file has no extension
            if '.' not in file_name:
                # Compute the full path of the original and new file
                original_file_path = os.path.join(root, file_name)
                new_file_path = original_file_path + '.png'
                # Rename the file
                os.rename(original_file_path, new_file_path)


while True:
    if __name__ == "__main__":
        directory_path = input("Please enter the path where the HD Head Textures are stored: ")
        append_png(directory_path)

        print("Image processing complete.")
