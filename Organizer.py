import shutil
from pathlib import Path
from datetime import datetime
import pillow_heif
from PIL import Image
import subprocess
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS)
    else:
        return Path(__file__).resolve().parent

base_path = get_base_path()

def convert_to_mp4(source, target):
    ffmpeg_path = get_base_path() / 'ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe'
    ffmpeg_path = ffmpeg_path.resolve(strict=True)

    if not ffmpeg_path.exists():
        raise FileNotFoundError(f"ffmpeg executable not found at {ffmpeg_path}")

    command = [str(ffmpeg_path), '-i', str(source), '-c:v', 'libx264', '-preset', 'fast', '-c:a', 'aac', str(target)]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert video {source}. Error: {e}")
    except Exception as e:
        print(f"An error occurred during video conversion: {e}")

def get_date_modified(file_path):
    return datetime.fromtimestamp(file_path.stat().st_mtime)

def organize_files(input_dir, output_dir, update_progress=None):
    input_path = Path(input_dir).resolve()
    output_path = Path(output_dir).resolve()
    files = list(input_path.rglob('*'))  # Recursively list all files
    total_files = len(files)
    processed_files = 0

    for file in files:
        if file.name.startswith('.') or file.is_dir():
            continue

        date_modified = get_date_modified(file)
        new_suffix = file.suffix.lower().replace('.heic', '.jpeg').replace('.mov', '.mp4')
        new_file_name = file.stem + new_suffix
        new_file_path = output_path / new_file_name
        new_file_path = new_file_path.resolve()

        if not new_file_path.exists():
            if file.suffix.lower() in ['.mov', '.mp4']:
                convert_to_mp4(file, new_file_path)
            elif file.suffix.lower() in ['.heic']:
                pillow_heif.register_heif_opener()
                try:
                    img = Image.open(file)
                    img.save(new_file_path)
                    img.close()
                except Exception as e:
                    print(f"Error handling HEIC file {file}: {e}")
            elif file.suffix.lower() in ['.jpg', '.jpeg']:
                shutil.copy2(file, new_file_path)

        if new_file_path.exists():
            destination_folder = output_path / date_modified.strftime("%Y") / date_modified.strftime("%m")
            destination_folder = destination_folder.resolve()
            destination_folder.mkdir(parents=True, exist_ok=True)  # Creates the directory if it doesn't exist
            shutil.move(str(new_file_path), str(destination_folder / new_file_path.name))  # Move the file
            print("File moved to:", destination_folder)
        else:
            print(f"Expected to move file but it does not exist: {new_file_path}")

        processed_files += 1
        if update_progress and total_files > 0:
            update_progress(100 * processed_files / total_files)

    print("All files have been processed.")
    if update_progress:
        update_progress(100)

def main_process(input_dir, output_dir, update_progress=None):
    organize_files(input_dir, output_dir, update_progress)
