import os
import shutil
import subprocess

source_folder = "D:/_Python/Sort files/recovered/TobeSorted/"
destination_folder = "D:/_Python/Sort files/sorted/"
max_size = 100000

def check_creation_date(date_check):
    if len(date_check) > 0:
        return True
    else:
        return False


# Check the filetype
for root, dirs, files in os.walk(source_folder):
    for file in files:
        source_file_path = os.path.join(root, file)
        try:
            file_type = subprocess.check_output(['exiftool', '-MIMEType', '-b', source_file_path]).decode('utf-8').strip()
            file_size = subprocess.check_output(['exiftool', '-FileSize', '-b', source_file_path]).decode('utf-8').strip()
            creation_check1 = subprocess.check_output(['exiftool', '-CreateDate', '-b', '-d', '%Y-%m-%d',
                                                       source_file_path]).decode('utf-8').strip()
            creation_check2 = subprocess.check_output(['exiftool', '-DateTimeOriginal', '-b', '-d', '%Y-%m-%d',
                                                       source_file_path]).decode('utf-8').strip()
        except subprocess.CalledProcessError:
            destin_path = os.path.join(destination_folder + "Others")
            os.makedirs(destin_path, exist_ok=True)
            shutil.move(source_file_path, os.path.join(destin_path, file))
            continue

        if check_creation_date(creation_check1):
            year = creation_check1[:4]
            month = creation_check1[5:7]
            day = creation_check1[8:10]
        else:
            year = creation_check2[:4]
            month = creation_check2[5:7]
            day = creation_check2[8:10]

        if "video" in file_type:
            if int(file_size) < max_size:
                destin_path = os.path.join(destination_folder, "Videos", "SmallFiles")
                os.makedirs(destin_path, exist_ok=True)
                shutil.move(source_file_path, os.path.join(destin_path, file))
            elif check_creation_date(creation_check1) or check_creation_date(creation_check2):
                destin_path = os.path.join(destination_folder + "Videos", year, month, day)
                os.makedirs(destin_path, exist_ok=True)
                shutil.move(source_file_path, os.path.join(destin_path, file))
            else:
                destin_path = os.path.join(destination_folder + "Videos", "NoDate")
                os.makedirs(destin_path, exist_ok=True)
                shutil.move(source_file_path, os.path.join(destin_path, file))
        elif "image" in file_type:
            if int(file_size) < max_size:
                destin_path = os.path.join(destination_folder, "Photos", "SmallFiles")
                os.makedirs(destin_path, exist_ok=True)
                shutil.move(source_file_path, os.path.join(destin_path, file))
            elif check_creation_date(creation_check1) or check_creation_date(creation_check2):
                destin_path = os.path.join(destination_folder + "Photos", year, month, day)
                os.makedirs(destin_path, exist_ok=True)
                shutil.move(source_file_path, os.path.join(destin_path, file))
            else:
                destin_path = os.path.join(destination_folder + "Photos", "NoDate")
                os.makedirs(destin_path, exist_ok=True)
                shutil.move(source_file_path, os.path.join(destin_path, file))
        else:
            destin_path = os.path.join(destination_folder + "Others")
            os.makedirs(destin_path, exist_ok=True)
            shutil.move(source_file_path, os.path.join(destin_path, file))
        print(f"Moved {file} to {destin_path}")
print("Sorting complete!")


