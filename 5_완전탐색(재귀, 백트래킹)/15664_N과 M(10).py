import itertools

N, M = map(int, input().split())
num_arr = sorted(list(map(int, input().split())))
arr = []

p = sorted(list(set(itertools.combinations(num_arr, M))))
for i in p:
    print(*i)