# File Organizer Script

## Overview

The **File Organizer Script** is a Python program that automatically organizes files in a directory based on their extensions or MIME types. The script sorts files into categorized subdirectories like:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, etc.
- **Documents**: `.pdf`, `.txt`, `.docx`, `.xlsx`, etc.
- **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, etc.
- **Audio**: `.mp3`, `.wav`, `.aac`, etc.
- **Archives**: `.zip`, `.rar`, `.7z`, etc.
- **Others**: Any unsupported file types.

It also supports a **dry-run mode**, allowing users to preview the organization process without making any changes.

## Features

- **Automatic File Categorization**: Sorts files into folders based on their extensions or MIME types.
- **Dry-Run Mode**: Allows previewing the organization without moving files.
- **Logging**: Tracks actions, successes, and errors in a log file.
- **Error Handling**: Handles permission issues and general errors during file operations.
- **Cross-Platform Support**: Works on Linux, Windows, and macOS by properly handling file paths.

## Installation

### Prerequisites

- Python 3.x installed.

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourgithubusername/file-organizer-script.git
cd file-organizer-script





______________________



Running the Script

Navigate to the Project Directory:

cd /path/to/your/file-organizer-script


Run the Script:

Execute the script with:

python file_organizer.py


You will be prompted to provide the directory you want to organize and choose whether you want a dry-run (no files will be moved in dry-run mode).

Dry-Run Mode:

If you want to test the file movement without actually making changes, input yes when asked:

Enter the path to the folder you want to organize: /path/to/your/folder
Do you want a dry run? (yes/no): yes


This will simulate the process and display where each file would go, without moving any files.

File Organization:

Once the script is run without dry-run mode, files will be moved into their respective categorized subfolders.

Example output:

Moved file1.jpg to Images
Moved file2.pdf to Documents


The following folders will be created if they don’t exist:

Images/

Documents/

Videos/

Audio/

Archives/

Others/