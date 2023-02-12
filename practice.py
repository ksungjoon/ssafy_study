# T = int(input())
# def abc(a,lst):
#     lst[2][2]=a
#     return result
#
#
# for test_case in range(1, T + 1):
#     a= input()
#     lst= [['..#..'],['.#.#.'],['#.a.#'],['.#.#.'],['..#..']]
#     result = []
#     abc(a[0],lst)
#     for i in range(1,len(a)):
#         result = [x+y for x,y in zip(result, abc(a[i],lst))]
#     print(result)

def cross(y, x):  ## 십자모양 분사
    sum = 0
    movey = [-1, 0, 1, 0]
    movex = [0, 1, 0, -1]
    for i in range(4):
        for j in range(1, M):
            ny = y + movey[i] * j
            nx = x + movex[i] * j
            if 0 <= ny < N and 0 <= nx < N:
                sum += lst[ny][nx]
    sum += lst[y][x]

    return sum


def X(y, x):  ## x자모양 분사
    sum = 0
    movey = [-1, -1, 1, 1]
    movex = [-1, 1, 1, -1]
    for i in range(4):
        for j in range(1, M):
            ny = y + movey[i] * j
            nx = x + movex[i] * j
            if 0 <= ny < N and 0 <= nx < N:
                sum += lst[ny][nx]
    sum += lst[y][x]
    return sum


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    maxkill = 0

    for i in range(N):
        for j in range(N):
            p = cross(i, j)
            x = X(i, j)
            if p > maxkill:
                maxkill = p
            if x > maxkill:
                maxkill = x
    print(f'#{tc} {maxkill}')

