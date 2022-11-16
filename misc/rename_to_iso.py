import os
import sys
from datetime import datetime

if len(sys.argv) > 2:
    print('usage: python3 rename_to_iso.py <dir>')
    exit()

path = sys.argv[1]
print(path)

files = os.listdir(path)
format = '%Y,%b,%d,%a,%H:%M:%S'

for file in files:
    stripped_file = '2022,' + file.strip('.gif')
    try:
        new_file = path + datetime.strptime(stripped_file, format).isoformat() + '.gif'
        path_and_file = path + file
        os.rename(path_and_file, new_file)
        print(f'renaming {path_and_file} to {new_file}')
    except ValueError:
        print(f'skipping {file}')
        pass
