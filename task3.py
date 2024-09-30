import os
import shutil

directory = input("Enter the path of the directory you want to organize: ")

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
}

for folder in file_types.keys():
    os.makedirs(os.path.join(directory, folder), exist_ok=True)

for filename in os.listdir(directory):
    file_extension = os.path.splitext(filename)[1].lower()  
    source = os.path.join(directory, filename) 
    for folder, extensions in file_types.items():
        if file_extension in extensions:
            destination = os.path.join(directory, folder, filename)
            shutil.move(source, destination)
            print(f'Moved: {filename} to {folder}/')
            break
