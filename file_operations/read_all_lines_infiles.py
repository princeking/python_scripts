import os

#filepath = r"D:\git_repo\wpa2-wordlists"
filepath = r"D:\git_repo\wpa2-wordlists\PlainText"

def processfile(the_file):
    count = 0
    with open(the_file) as fh:
        for data in fh:
            #print(data, end='\n')
            #print(data.split())
            count = count +1
    print("number of lines: ", count)

for root, dirs, files in os.walk(filepath):
    for file in files:
        if file.endswith('.txt'):
            file2open = os.path.join(root, file)
            print(file2open)
            processfile(file2open)



