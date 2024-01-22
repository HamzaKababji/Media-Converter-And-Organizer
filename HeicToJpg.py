import os
import shutil
from PIL import Image
import pillow_heif
from pathlib import Path
import dotenv
import glob

dotenv.load_dotenv();

if __name__ == "__main__":
    input_dir = os.getenv('input_dir')
    output_dir = os.getenv('output_dir')
    
    files = glob.glob(os.path.join(input_dir,'**','*'), recursive=True)
    for str_file in files:
        file = Path(str_file)
        if file.stem.startswith('.'):
            
            continue
        
        elif file.suffix in ['.mov', '.MOV']:
            #convert to mp4
            #extract date taken information
            #organize in a new folder based on date taken
            pass
        
        elif file.suffix in ['.heic', '.HEIC']:
            pillow_heif.register_heif_opener()
            img = Image.open(file)
            img.save(os.path.join(output_dir,file.stem+'.jpeg'))
            
            #timestamp = os.path.getmtime(file)
        
        elif file.suffix in ['.jpg', '.JPG']:  
            if file.suffix == '.jpg':
                shutil.copy2(str_file,os.path.join(output_dir,file.stem+'.jpeg'))
            else:
                shutil.copy2(str_file,os.path.join(output_dir,file.stem+'.jpeg'))
                

            
            # Finding the date of the image (not working yet)
            #img_data = img.getexif()
            #date_gen = img_data.get(36867)
            #print(date_gen)
            
            #convert to jpg
            #extract date taken information
            #organize in a new folder based on date taken

        

    
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
                

            