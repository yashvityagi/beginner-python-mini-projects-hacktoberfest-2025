import os
import shutil
import logging
from mimetypes import guess_type
from pathlib import Path

logging.basicConfig(filename='file_organizer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".txt", ".docx", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".tar", ".rar", ".7z"],
    "Others": []
}

def organize_files(src_directory, dry_run=False):
    """
    Organizes files in the source directory into categorized folders.
    If dry_run=True, the files will not be moved but only listed.
    """
    if not os.path.exists(src_directory):
        logger.error(f"Error: The directory {src_directory} does not exist.")
        print(f"Error: The directory {src_directory} does not exist.")
        return

    for folder in file_types.keys():
        folder_path = os.path.join(src_directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for filename in os.listdir(src_directory):
        file_path = os.path.join(src_directory, filename)

        if os.path.isdir(file_path):
            continue
        
        file_extension = os.path.splitext(filename)[1].lower()
        mime_type, _ = guess_type(filename)

        if mime_type:
            category = categorize_by_mime(mime_type)
        else:
            category = categorize_by_extension(file_extension)

        if category is None:
            category = 'Others'

        target_folder = os.path.join(src_directory, category)
        target_path = os.path.join(target_folder, filename)
        
        if dry_run:
            print(f"Would move {filename} to {category}")
        else:
            try:
                shutil.move(file_path, target_path)
                logger.info(f"Moved {filename} to {category}")
                print(f"Moved {filename} to {category}")
            except PermissionError as e:
                logger.error(f"Permission error moving {filename}: {e}")
                print(f"Permission error moving {filename}: {e}")
            except Exception as e:
                logger.error(f"Failed to move {filename}: {e}")
                print(f"Failed to move {filename}: {e}")

    print("File organization complete!" if not dry_run else "Dry run complete!")

def categorize_by_extension(extension):
   
    for category, extensions in file_types.items():
        if extension in extensions:
            return category
    return None

def categorize_by_mime(mime_type):
   
    if mime_type:
        if mime_type.startswith('image'):
            return "Images"
        elif mime_type.startswith('audio'):
            return "Audio"
        elif mime_type.startswith('video'):
            return "Videos"
        elif mime_type == 'application/zip':
            return "Archives"
        elif mime_type.startswith('text') or mime_type == 'application/pdf':
            return "Documents"
    return None

if __name__ == "__main__":
    src_dir = input("Enter the path to the folder you want to organize: ")
    dry_run_input = input("Do you want a dry run? (yes/no): ").strip().lower()
    dry_run = dry_run_input == 'yes'
    organize_files(src_dir, dry_run)
