def recur(number):
    if number == M:
        print(*arr)
        return

    for i in range(1, N+1):
        arr.append(num_arr[i-1])
        recur(number+1)
        arr.pop()


N, M = map(int, input().split())
num_arr = sorted(list(map(int, input().split())))
arr = []

recur(0)