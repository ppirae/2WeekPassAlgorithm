N = int(input())

def recur(idx, siin, sseun, use):
    global answer

    if idx == N:
        if use == 0:
            return
        result = abs(siin-sseun)
        answer = min(answer, result)
        return

    recur(idx+1, siin*ingre[idx][0], sseun+ingre[idx][1], use+1)

    recur(idx+1, siin, sseun, use)

ingre = [list(map(int, input().split())) for _ in range(N)]
answer = 999999999999

recur(0, 1, 0, 0)
print(answer)