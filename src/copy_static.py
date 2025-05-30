import os
import shutil

def copy_static(source_dir, destination_dir):
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    shutil.copytree(source_dir, destination_dir)
    print(f"Copied static files from {source_dir} to {destination_dir}")