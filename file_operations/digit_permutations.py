import timeit

code_to_test = """
from itertools import permutations
count = 0
for p in permutations(['1','2','3','4','5','6','7','8','9','0'], 7):
    count = count +1
    #print(''.join(p))
print('number of permutations: ', count)
"""

elapsed_time = timeit.timeit(code_to_test, number=1)
print("Time taken to execute function: ", elapsed_time)
