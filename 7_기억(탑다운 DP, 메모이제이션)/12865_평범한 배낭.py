N, K = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(100_001)] for _ in range(N)]

def recur(idx, w):
    global answer
    if w > K:
        return -999999999

    if idx == N:
        return 0

    if dp[idx][w] != -1:
        return dp[idx][w]

    dp[idx][w]  = max(recur(idx+1, w+item[idx][0]) + item[idx][1], recur(idx+1, w))

    return dp[idx][w]

recur(0, 0)
# print(dp)
print(max(max(dp)))