import os
import shutil
from PIL import Image
import pillow_heif
from pathlib import Path
# Test From WSL
if __name__ == "__main__":
    
    
    months=list(range(1,13))
    for month in months:
        dir=f"Z:/2021/{month}"

        
        if not os.path.exists(os.path.join(dir,'heic')):
            os.makedirs(os.path.join(dir,'heic'))
            
        files = Path(dir).glob('*')
        for file in files: #file.name, file.stem, file.suffix,
            try:
                if file.stem.startswith('.'):
                    os.remove(os.path.join(dir, file.name))
                elif file.suffix in ['.BIF','bif']:
                    os.remove(os.path.join(dir, file.name))
                elif file.suffix in ['.HEIC','.heic']:
                    pillow_heif.register_heif_opener()
                    img = Image.open(os.path.join(dir,file.name))
                    img.save(os.path.join(dir,file.stem+'.jpeg'))
                    shutil.move(os.path.join(dir, file.name), os.path.join(dir,'heic'))
                elif file.suffix in ['.XMP','.AAE']:
                    shutil.move(os.path.join(dir, file.name), os.path.join(dir,'heic'))
            except:
                continue
                

            