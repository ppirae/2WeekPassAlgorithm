def recur(idx, dan, ji, tan, vi, price, idx_list):
    global answer, answer_list

    if idx == N:
        if dan >= a and ji >= b and tan >= c and vi >= d:
            result = price
            if answer > result:
                answer = result
                answer_list = sorted(idx_list)
            elif answer == result:
                if answer_list > idx_list:
                    answer_list = idx_list
        return

    recur(idx+1, dan+ingre[idx][0], ji+ingre[idx][1], tan+ingre[idx][2], vi+ingre[idx][3], price+ingre[idx][4], idx_list+[idx+1])

    recur(idx+1, dan, ji, tan, vi, price, idx_list)


N = int(input())
a, b, c, d = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 99999999999
answer_list = []

recur(0, 0, 0, 0, 0, 0, [])
if answer == 99999999999:
    print(-1)
else:
    print(answer)
if answer_list:
    print(*answer_list)



# 100퍼에서 틀림
# 반례
# 3
# 0 0 0 1
# 0 0 0 1 1
# 0 0 0 0 0
# 0 0 0 0 0

# 답
# 1
# 1