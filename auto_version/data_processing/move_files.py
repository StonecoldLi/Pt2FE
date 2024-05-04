import os
import shutil

def move_specified_files(source_folder, destination_folder, file_list):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Move each specified file
    for file_name in file_list:
        source_file = os.path.join(source_folder, file_name)
        if os.path.exists(source_file):
            shutil.move(source_file, os.path.join(destination_folder, file_name))
        else:
            print(f"File {file_name} does not exist in {source_folder}")
