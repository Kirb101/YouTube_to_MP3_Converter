import os

parent_dir = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(parent_dir):
    if file.endswith('.mp4'):
        file_path = os.path.join(parent_dir, file)
        new_file_path = os.path.splitext(file_path)[0] + '.mp3'
        os.rename(file_path, new_file_path)
