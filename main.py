import os
from PIL import Image  # pip install pillow
from PIL import UnidentifiedImageError


with os.scandir('ImagesToConvert/') as entries:
    for entry in entries:
        try:
            if entry.name == '.gitignore' or entry.name == '.DS_Store':
                continue
            image = Image.open('ImagesToConvert/' + entry.name)
            image.thumbnail((512, 512), Image.ANTIALIAS)
            image.save('ConvertedImages/' + entry.name.split('.')[0] + '.png')
        except FileNotFoundError:
            print(f'Not find file: {entry.name}')
        except UnidentifiedImageError:
            print(f'Can\'t open file: {entry.name}')
        except IsADirectoryError:
            print(f'You are trying to open directory: {entry.name}')
        except IOError:
            print(f'Can\'t create thumbnail for file: {entry.name}')
