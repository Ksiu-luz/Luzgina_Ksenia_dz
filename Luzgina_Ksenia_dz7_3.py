import os
import shutil

my_dir = os.path.join(os.getcwd(), 'my_project', 'templates')


if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'
my_files = []

for root, dirs, files in os.walk(folder):
    for file in files:
        if '.html' in file:
            my_files.append(os.path.join(root, file))
for path in my_files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)
