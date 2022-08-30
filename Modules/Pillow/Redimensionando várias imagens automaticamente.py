'''
Redimensionando várias imagens automaticamente com
o módulo pillow e os
'''
import os
from PIL import Image

def main(images_folder, new_width=1080):
    if not os.path.isdir(images_folder):
        raise NotADirectoryError(f'{images_folder} does not exist!...')
    
    for root, dirs, files in os.walk(images_folder):
        for file in files:
            if '.JPG' in file:
                full_path = os.path.join(root, file)
                file_name, extension = os.path.splitext(file)
                new_file = file_name + '_CONVERTED' + extension
                new_file_path = os.path.join(root, new_file)

                if os.path.isfile(new_file_path):
                    print(f'{new_file_path} already exists...')
                    continue

                if '_CONVERTED' in full_path:
                    continue

                img_pillow = Image.open(full_path)
                
                width, height = img_pillow.size
                new_height = round(new_width * height / width)

                new_image = img_pillow.resize((new_width, new_height), Image.LANCZOS)
                new_image.save(
                    new_file_path,
                    optimize=True,
                    quality=70,
                    exif=img_pillow.info['exif']
                )

                print(f'{full_path} successfully converted...')
                img_pillow.close()

if __name__ == '__main__':
    path_images_folder = r'C:\Users\55119\Documents\Estudos\Python\Módulos\Pillow'
    main(path_images_folder)