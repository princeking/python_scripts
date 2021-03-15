from itertools import product

for p in product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=8):
    print("".join(p) + "\n")
#with open('myfile', 'w') as file:
    #for p in product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=8):
        #file.write("".join(p) + "\n")