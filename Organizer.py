import os
import shutil
from pathlib import Path
import dotenv
import glob
from moviepy.editor import VideoFileClip
from datetime import datetime
import pillow_heif
from PIL import Image

dotenv.load_dotenv()

def convert_to_mp4(source, target):
    clip = VideoFileClip(source)
    clip.write_videofile(target, codec='libx264')
    clip.close()

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
                    print(f"Error handling HEIC file {str_file}: {e}")
            elif file.suffix.lower() in ['.jpg', '.jpeg']:
                shutil.copy2(str_file, output_path)

        year = date_modified.strftime("%Y")
        month = date_modified.strftime("%m")
        destination_folder = os.path.join(output_dir, year, month)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.move(output_path, os.path.join(destination_folder, os.path.basename(output_path)))
        print("File moved to:", destination_folder)

        processed_files += 1
        if update_progress and total_files > 0:
            update_progress(100 * processed_files / total_files)

    print("All files have been processed.")
    update_progress(100)
    
def main_process(input_dir, output_dir, update_progress=None):
    organize_files(input_dir, output_dir, update_progress)

if __name__ == "__main__":
    input_dir = os.getenv('input_dir')
    output_dir = os.getenv('output_dir')
    main_process(input_dir, output_dir)
