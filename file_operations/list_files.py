import os
file_path = r"/Volumes/Untitled/"

for root, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith('.txt'):
            print(file)