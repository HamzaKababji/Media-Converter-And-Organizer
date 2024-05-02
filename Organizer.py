import os
import shutil
from pathlib import Path
import dotenv
import glob
from datetime import datetime
import pillow_heif
from PIL import Image
import subprocess
import logging

dotenv.load_dotenv()

import subprocess
import logging

def convert_to_mp4(source, target):
    logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')
    
    ffmpeg_path = r'C:\Users\hamza\OneDrive - The University of Western Ontario\Personal\Projects\File-and-Folder-Converter-And-Organizer\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe'
    
    command = [ffmpeg_path, '-i', source, '-c:v', 'libx264', '-preset', 'fast', '-c:a', 'aac', target]
    
    try:
        logging.debug(f"Running command: {' '.join(command)}")
        
        subprocess.run(command, check=True)
        
        logging.debug("Conversion successful")
    except subprocess.CalledProcessError as e:
        logging.error(f"ffmpeg command failed with return code {e.returncode}")
    except Exception as e:
        logging.error(f"Failed to execute command: {e}")

def get_date_modified(file_path):
    timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(timestamp)

def organize_files(input_dir, output_dir, update_progress=None):
    files = glob.glob(os.path.join(input_dir, '**', '*'), recursive=True)
    total_files = len(files)
    processed_files = 0

    for str_file in files:
        file = Path(str_file)
        if file.stem.startswith('.') or file.is_dir():
            continue

        date_modified = get_date_modified(str_file)
        output_path = os.path.join(output_dir, file.stem + file.suffix.lower().replace('.heic', '.jpeg').replace('.mov', '.mp4'))

        if not os.path.exists(output_path):
            if file.suffix.lower() in ['.mov', '.mp4']:
                convert_to_mp4(str_file, output_path)
            elif file.suffix.lower() in ['.heic']:
                pillow_heif.register_heif_opener()
                try:
                    img = Image.open(str_file)
                    img.save(output_path)
                    img.close()
                except Exception as e:
                    logging.error(f"Error handling HEIC file {str_file}: {e}")
            elif file.suffix.lower() in ['.jpg', '.jpeg']:
                shutil.copy2(str_file, output_path)

        if os.path.exists(output_path):
            year = date_modified.strftime("%Y")
            month = date_modified.strftime("%m")
            destination_folder = os.path.join(output_dir, year, month)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(output_path, os.path.join(destination_folder, os.path.basename(output_path)))
            print("File moved to:", destination_folder)
        else:
            logging.error(f"Expected to move file but it does not exist: {output_path}")

        processed_files += 1
        if update_progress and total_files > 0:
            update_progress(100 * processed_files / total_files)

    print("All files have been processed.")
    if update_progress:
        update_progress(100)

    
def main_process(input_dir, output_dir, update_progress=None):
    organize_files(input_dir, output_dir, update_progress)

if __name__ == "__main__":
    input_dir = os.getenv('input_dir')
    output_dir = os.getenv('output_dir')
    main_process(input_dir, output_dir)