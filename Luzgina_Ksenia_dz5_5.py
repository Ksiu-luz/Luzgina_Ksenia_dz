import sys
from time import perf_counter

start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [src[i] for i in range(len(src)) if src.count(src[i]) == 1]

result = tuple(result)

print(perf_counter() - start)
print(*result)
print(sys.getsizeof(result))
