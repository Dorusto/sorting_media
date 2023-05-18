import os
import shutil
import subprocess

source_folder = "D:/_Python/Sort files/recovered/TobeSorted"
destin_folder = "D:/_Python/Sort files/sorted"

for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            creation_date = subprocess.check_output(['exiftool', '-CreateDate', '-b', '-d', '%Y-%m-%d', file_path]).decode('utf-8').strip()
        except subprocess.CalledProcessError:
            print(f"Skipping {file_path} due to missing creation date.")
            continue
        year = creation_date[:4]
        month = creation_date[5:7]
        day = creation_date[8:10]
        destin_path = os.path.join(destin_folder, year, month, day)
        os.makedirs(destin_path, exist_ok=True)
        shutil.move(file_path, os.path.join(destin_path, file))
        print(f"Moved {file} to {destin_path}")
print("Sorting complete!")