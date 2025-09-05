import itertools

N, M = map(int, input().split())
num_arr = sorted(list(set(map(int, input().split()))))

p = itertools.product(num_arr, repeat=M)
for i in p:
    print(*i)