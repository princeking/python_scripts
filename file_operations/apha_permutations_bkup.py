import timeit
from itertools import permutations
count = 0
alpha_chars =[]

with open(r"D:\\data science\\alpha_wordlist_char7.txt", mode='a+') as wordlist:

    for p in permutations(['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z','!','\"','£','$','%','^','&',
        '*','(',')','-','_','=','+','\\','|','<','>','?','/','@','\'','#','~'], 8):
        count = count +1
        #print(''.join(p))
        wordlist.write(''.join(p))

    print('number of permutations: ', count)


    #for word in alpha_chars:
        #wordlist.write('\n'.join(str(item) for item in alpha_chars ))


