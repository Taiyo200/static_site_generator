import os
import shutil


def copy_static(source, destination):

    if os.path.exists(destination):
        print(f"Removing existing directory: {destination}")
        shutil.rmtree(destination)

    os.makedirs(destination, exist_ok=True)

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")
        elif os.path.isdir(src_path):
            copy_static(src_path, dest_path)