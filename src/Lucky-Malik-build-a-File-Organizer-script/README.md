# File Organizer Script

## Project Description

This Python script provides a simple yet effective solution for organizing files within a specified directory. It automatically categorizes files based on their extensions and moves them into corresponding subdirectories (e.g., `Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Code`, `Executables`, `Others`). This helps in maintaining a clean and structured file system, making it easier to locate and manage your digital assets.

## How to Run the Project

### Prerequisites

To run this script, you need Python 3.x installed on your system. No external libraries are strictly required beyond the standard Python library, but `shutil` and `os` are used for file operations.

### Installation

1.  **Clone the repository (or download the files):**

    If you are cloning from a Git repository, use:
    ```bash
    git clone <repository_url>
    cd manus-build-a-file-organizer-script
    ```

    If you downloaded the files, navigate to the `src/manus-build-a-file-organizer-script/` directory.

2.  **Navigate to the project directory:**

    ```bash
    cd src/manus-build-a-file-organizer-script/
    ```

### Usage

1.  **Open the `organizer.py` file:**

    You can open it in any text editor to review the code and understand its functionality.

2.  **Modify `if __name__ == "__main__":` block (Optional but Recommended):**

    The script includes a demonstration section within the `if __name__ == "__main__":` block. For actual use, you should modify this section to specify your desired source and destination directories.

    Locate these lines:
    ```python
    dummy_source = 'test_source'
    dummy_destination = 'test_destination'
    organize_files(dummy_source, dummy_destination)
    ```

    Replace `dummy_source` with the path to the directory you want to organize, and `dummy_destination` with the path where you want the organized files to be moved. For example:

    ```python
    source_directory = '/home/user/Downloads' # Your messy downloads folder
    destination_directory = '/home/user/OrganizedFiles' # Where you want files to go
    organize_files(source_directory, destination_directory)
    ```

3.  **Run the script:**

    Execute the script from your terminal:
    ```bash
    python3 organizer.py
    ```

    The script will then process the files in your specified source directory and move them to the appropriate subdirectories within the destination directory.

## Output Sample

When you run the script, you will see log messages indicating the creation of directories and the movement of files. For example:

```
2025-10-04 10:30:00,123 - INFO - Created destination directory: test_destination
2025-10-04 10:30:00,124 - INFO - Created category directory: test_destination/Documents
2025-10-04 10:30:00,125 - INFO - Created category directory: test_destination/Images
2025-10-04 10:30:00,126 - INFO - Created category directory: test_destination/Videos
2025-10-04 10:30:00,127 - INFO - Created category directory: test_destination/Audio
2025-10-04 10:30:00,128 - INFO - Created category directory: test_destination/Archives
2025-10-04 10:30:00,129 - INFO - Created category directory: test_destination/Code
2025-10-04 10:30:00,130 - INFO - Created category directory: test_destination/Executables
2025-10-04 10:30:00,131 - INFO - Created category directory: test_destination/Others
2025-10-04 10:30:00,132 - INFO - Moved 'document.pdf' to 'Documents'
2025-10-04 10:30:00,133 - INFO - Moved 'image.jpg' to 'Images'
2025-10-04 10:30:00,134 - INFO - Moved 'video.mp4' to 'Videos'
2025-10-04 10:30:00,135 - INFO - Moved 'archive.zip' to 'Archives'
2025-10-04 10:30:00,136 - INFO - Moved 'script.py' to 'Code'
2025-10-04 10:30:00,137 - INFO - Moved 'unknown.xyz' to 'Others'
File organization complete.
Demonstration complete. Check 'test_destination' folder.
```

After execution, your `test_destination` (or your specified destination) directory will contain subfolders like `Images`, `Documents`, etc., with the organized files inside them.
