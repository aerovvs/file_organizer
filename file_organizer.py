import os
import shutil
import sys

# source directory
source_dir = "/Users/cjhosea/Downloads"

# mapping extensions to organized folders
file_types = {
    ".jpeg": "images",
    ".jpg": "images",
    ".png": "images",
    ".gif": "images",
    ".heic": "images",
    ".mp4": "videos",
    ".mov": "videos",
    ".mp3": "music",
    ".m4a": "music",
    ".wav": "music",
    ".zip": "archives",
    ".exe": "executables",
    ".dmg": "executables",
    ".docx": "documents",
    ".doc": "documents",
    ".xlsx": "documents",
    ".xls": "documents",
    ".csv": "documents",
    ".pdf": "documents",
    ".pptx": "documents",
    ".txt": "documents",
}

# create folders if they don't exist
for folder in file_types.values():
    folder_path = os.path.join(source_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# function that move files to corresponding folders
def organize_files():
    for filename in os.listdir(source_dir):
        if filename != "file_organizer.py":  # exclude the script file itself
            src = os.path.join(source_dir, filename)
            if os.path.isfile(src):
                file_ext = os.path.splitext(filename)[1]
                if file_ext in file_types:
                    dest_folder = file_types[file_ext]
                    dest = os.path.join(source_dir, dest_folder, filename)
                    shutil.move(src, dest)
                    print(f"Moved {filename} to {dest_folder} folder.")

# run organizer and exit
if __name__ == "__main__":
    organize_files()
    print("files have been sorted.")
    sys.exit(0)
