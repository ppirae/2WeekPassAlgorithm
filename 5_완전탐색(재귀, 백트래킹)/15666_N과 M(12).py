import itertools

N, M = map(int, input().split())
num_arr = sorted(list(set(map(int, input().split()))))

p = itertools.combinations_with_replacement(num_arr, M)
for i in p:
    print(*i)