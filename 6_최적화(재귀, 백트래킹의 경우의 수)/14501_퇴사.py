def recur(idx, price):
    global answer
    if idx == N:
        result = price
        answer = max(answer, result)
        return
    if idx > N:
        return

    recur(idx+interview[idx][0], price+interview[idx][1])

    recur(idx+1, price)

N = int(input())

interview = [list(map(int, input().split())) for _ in range(N)]
answer = -9999999999999


recur(0, 0)
print(answer)