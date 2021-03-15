import os

filepath = r"D:\git_repo\wpa2-wordlists\Wordlists"

outputfile = r"D:\git_repo\wpa2-wordlists\Wordlists\bulk_words\complete_words.txt"
with open(outputfile, "w") as fo:
    for root, dir, filename in os.walk(filepath):
        for file in filename:
            if file.endswith('.txt'):
                file2copy = os.path.join(root,file)

                with open(file2copy, encoding='cp1252', errors='ignore') as fin:
                    print("opening file: ", fin)
                    for line in fin:
                        fo.write(line)
                    print("written file: ", file)


# count the number of words in this wordlist
n_words = len(list(open(outputfile, "r")))
# print the total number of passwords
print("Total passwords written to file is: ", n_words)