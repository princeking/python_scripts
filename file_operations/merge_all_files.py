import os

outfilename = r"D:\data science\complete_wordlist.txt"

files = os.listdir(path)
with open(outfilename, 'w') as outfile:
    for fname in filenames:
        with open(fname, 'r') as readfile:
            outfile.write(readfile.read() + "\n\n")