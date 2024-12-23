import os
import shutil

# Taking input folder path from User.
folder_path = input('Enter the folder path which you want to organize :')
checking_exist =os.path.exists(folder_path)

# Checking valid path.

if checking_exist == True:
    print('Path is valid.')
    
else:
    while checking_exist == False or checking_directory == False:
        print()
        print('enter valid path!')
        print('"Ctrl + C if you want to exit loop."')
        folder_path = input('Enter the folder path which you want to organize :')
        checking_exist =os.path.exists(folder_path)
        checking_directory =os.path.isdir(folder_path)

print(20*'-')

# Listing folder files.

listing_directory = os.listdir(folder_path)
print(listing_directory)

print(20*'-')

# File extensions.

file_extensions = {
    "Text": [".txt", ".md", ".csv", ".log", ".json", ".xml"],
    "Images": [".jpg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Video": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".html", ".rtf"],
    "Archives": [".zip", ".tar", ".rar", ".7z", ".gz"],
    "Scripts": [".py", ".sh", ".bat", ".js", ".php"],
    "Data": [".db", ".sql", ".sqlite", ".h5"],
    "Executables": [".exe", ".dll", ".bin", ".apk"]
}

extensions_values = list(file_extensions.values())

# Creating a destination folder.
destination_path = input('Enter the destination path for organized folders:')

# Creating a new folder inside the specified directory
new_folder = 'Destination Folder'
destination_folder = os.path.join(destination_path, new_folder)
if not os.path.exists(destination_folder):
    making_directory = os.makedirs(destination_folder)
    print(f'Destination {destination_folder} created successfully.')
else:
    print(f'Directory {destination_folder} already exists.')

print(20*'-')

# Creating sub-folders with file_extension keys.
sub_folders = list(file_extensions.keys())
for subdir in sub_folders:
    dir_path = os.path.join(destination_folder, subdir)
    os.makedirs(dir_path, exist_ok= True)
    print(f'Sub folders {sub_folders} created successfully.')

print(20*'-')
      
# Match the file based on its extension
for file_name in listing_directory:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_name)[1].lower()
        for category, extensions in file_extensions.items():
            if file_ext in extensions:
                dest_path = os.path.join(destination_folder, category, file_name)
                shutil.move(file_path, dest_path)
                print(f"Moved '{file_name}' to {dest_path}")
                break
