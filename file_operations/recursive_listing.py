import os
for root, dirs, files in os.walk('/Users/edwin'):
    for filenames in files:
        #if filenames.endswith('.txt'):
        file2open = os.path.join(root, filenames)
        print(file2open)