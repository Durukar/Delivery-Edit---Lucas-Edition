import os
import re
import logging
from datetime import datetime
import shutil
from time import sleep
from babel.dates import format_date

class MediaFileMover:
    def __init__(self, src_dir, dst_dir):
        logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.INFO, datefmt='%Y-%m-%dT%H:%M:%S.%fZ')
        self.src_dir = src_dir
        self.dst_dir = dst_dir

    def move_files(self):
        for root, dirs, files in os.walk(self.src_dir):
            for file in files:
                file_path = os.path.join(root, file)
                date_match = re.search(r'\d{6}$', root)
                if date_match:
                    date_str = f'{date_match.group()[:2]}-{date_match.group()[2:4]}-20{date_match.group()[4:]}'
                    date = datetime.strptime(date_str, '%d-%m-%Y')
                    month_path = format_date(date, 'MMMM', locale='pt_BR').upper()
                    day = date.strftime('%d')
                    dir_name = os.path.basename(root)

                    dst_path = os.path.join(self.dst_dir, month_path, day, dir_name)

                    if not os.path.exists(dst_path):
                        os.makedirs(dst_path)
                    shutil.move(file_path, dst_path)
                    logging.info(f'Successfully moved {file} to >> {dst_path}')

        # remove somente as pastas vazias dentro do caminho inicial 
        for root, dirs, files in os.walk(self.src_dir):
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                if not os.listdir(folder_path):
                    os.rmdir(folder_path)
                    logging.info(f'Successfully removed empty folder {folder_path}')

mover = MediaFileMover('C:/Path/path/path', 'C:/Path/path/path')
while True:
    mover.move_files()
    sleep(30)
