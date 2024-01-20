import os
import shutil
from PIL import Image
import pillow_heif
from pathlib import Path
import dotenv
import numpy as np

dotenv.load_dotenv();

if __name__ == "__main__":
    #"\\192.168.2.93\photos\Mobile backup"
    input_dir = os.getenv('input_dir')
    output_dir = os.getenv('output_dir')
    
    files = Path(input_dir).glob('*') #Currently not working to read through subfolders
    
    for file in files:
        if file.stem.startswith('.'):
            continue
        elif file.suffix in ['.mov', '.MOV']:
            #convert to mp4
            #extract date taken information
            #organize in a new folder based on date taken
            pass
        elif file.suffix in ['.heic', '.HEIC']:
            pillow_heif.register_heif_opener()
            input_path = os.path.join(input_dir,file.name)
            img = Image.open(input_path)
            
            # img.save(os.path.join(output_dir,file.stem+'.jpeg'))
            
            timestamp = os.path.getmtime(input_path)

            
            # Finding the date of the image (not working yet)
            #img_data = img.getexif()
            #date_gen = img_data.get(36867)
            #print(date_gen)
            
            #convert to jpg
            #extract date taken information
            #organize in a new folder based on date taken
            continue
        

    
    # # months=list(range(1,13))
    # for month in months:
        
    #     if not os.path.exists(os.path.join(input_dir,'heic')):
    #         os.makedirs(os.path.join(input_dir,'heic'))
            
    #     files = Path(input_dir).glob('*')
    #     for file in files: #file.name, file.stem, file.suffix,
    #         try:
    #             if file.stem.startswith('.'):
    #                 os.remove(os.path.join(input_dir, file.name))
    #             elif file.suffix in ['.BIF','bif']:
    #                 os.remove(os.path.join(input_dir, file.name))
    #             elif file.suffix in ['.HEIC','.heic']:
    #                 pillow_heif.register_heif_opener()
    #                 img = Image.open(os.path.join(input_dir,file.name))
    #                 img.save(os.path.join(input_dir,file.stem+'.jpeg'))
    #                 shutil.move(os.path.join(input_dir, file.name), os.path.join(input_dir,'heic'))
    #             elif file.suffix in ['.XMP','.AAE']:
    #                 shutil.move(os.path.join(input_dir, file.name), os.path.join(input_dir,'heic'))
    #         except:
    #             continue
                

            