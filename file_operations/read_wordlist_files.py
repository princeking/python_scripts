import os
count = 0

for root, dir, files in os.walk(r"D:\data science"):
    for names in files:
        if names.endswith('uniq'):
            wordlist = os.path.join(root,names)
            with open(wordlist, errors='ignore') as fh:
                for line in fh:
                    count = count +1
                    print(line.rstrip())
                print(f" file {wordlist} contains: {count}")