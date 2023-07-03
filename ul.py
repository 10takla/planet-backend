import os
import shutil

directory = "D:/UlbiTV"

folder_names = []
for entry in os.scandir(directory):
    if entry.is_dir() and '[2 поток]' not in entry.name:
        folder_names.append(entry.name)
folder_names = folder_names[1:]
videos = []
for name in folder_names:
    for vid in os.scandir(os.path.join(directory, name)):
        if vid.is_dir():
            for item in os.listdir(os.path.join(directory, name, vid.name)):
                item_path = os.path.join(directory, name, vid.name, item)
                if os.path.isfile(item_path) and item.endswith('.ts'):
                    new_file_path = os.path.join("D:/UlbiTV/vids", vid.name + '.ts')
                    shutil.copy2(item_path, new_file_path)
                    videos.append(item)

print(videos)

