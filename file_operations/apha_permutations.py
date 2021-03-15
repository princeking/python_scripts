import timeit

code_to_test = """
from itertools import permutations
count = 0
alpha_chars =[]
for p in permutations(['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x','y','z'], 10):
    count = count +1
    #print(''.join(p))
    alpha_chars.append(''.join(p))
    
print('number of permutations: ', count)
    
"""

elapsed_time = timeit.timeit(code_to_test, number=1)
print("Time taken to execute function: ", elapsed_time)


