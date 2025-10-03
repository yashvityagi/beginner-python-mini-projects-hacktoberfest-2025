
import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_files(source_dir, destination_dir):
    """
    Organizes files from a source directory into category-based subdirectories
    within a destination directory.
    """
    if not os.path.exists(source_dir):
        logging.error(f"Source directory not found: {source_dir}")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        logging.info(f"Created destination directory: {destination_dir}")

    # Define file categories and their corresponding extensions
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.ppt', '.pptx', '.xls', '.xlsx'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.php', '.go', '.rb'],
        'Executables': ['.exe', '.dmg', '.app', '.deb', '.rpm'],
        'Others': [] # Files that don't match any specific category
    }

    # Create category subdirectories if they don't exist
    for category_name in categories.keys():
        category_path = os.path.join(destination_dir, category_name)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            logging.info(f"Created category directory: {category_path}")

    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in categories.items():
            if file_extension in extensions:
                destination_path = os.path.join(destination_dir, category, filename)
                try:
                    shutil.move(source_path, destination_path)
                    logging.info(f"Moved '{filename}' to '{category}'")
                    moved = True
                except Exception as e:
                    logging.error(f"Error moving '{filename}': {e}")
                break
        
        if not moved:
            # Move to 'Others' category if no specific category is found
            destination_path = os.path.join(destination_dir, 'Others', filename)
            try:
                shutil.move(source_path, destination_path)
                logging.info(f"Moved '{filename}' to 'Others'")
            except Exception as e:
                logging.error(f"Error moving '{filename}': {e}")

    logging.info("File organization complete.")

if __name__ == "__main__":
    # Example usage (replace with actual paths or command-line arguments)
    # For demonstration, let's create some dummy files and directories
    
    # Create a dummy source directory
    dummy_source = 'test_source'
    os.makedirs(dummy_source, exist_ok=True)
    
    # Create dummy files
    with open(os.path.join(dummy_source, 'document.pdf'), 'w') as f: f.write('dummy')
    with open(os.path.join(dummy_source, 'image.jpg'), 'w') as f: f.write('dummy')
    with open(os.path.join(dummy_source, 'video.mp4'), 'w') as f: f.write('dummy')
    with open(os.path.join(dummy_source, 'archive.zip'), 'w') as f: f.write('dummy')
    with open(os.path.join(dummy_source, 'script.py'), 'w') as f: f.write('dummy')
    with open(os.path.join(dummy_source, 'unknown.xyz'), 'w') as f: f.write('dummy')
    
    dummy_destination = 'test_destination'
    
    print(f"\nOrganizing files from '{dummy_source}' to '{dummy_destination}'...")
    organize_files(dummy_source, dummy_destination)
    print("\nDemonstration complete. Check 'test_destination' folder.")

    # Clean up dummy directories and files for re-runnability
    # shutil.rmtree(dummy_source)
    # shutil.rmtree(dummy_destination)
    # logging.info("Cleaned up dummy directories.")


