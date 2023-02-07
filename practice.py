# import sys
# sys.stdin = open("input.txt", "r")
T = 10
for test_case in range(1, T + 1):
    N =int(input())
    lst = [list(map(int,input().split()))for i in range(100)]
    y=99
    x=0
    for i in range(100):
        if lst[y][i]==2:
            x=i
    while True:
        if lst[y][x-1]==1:
            x -= 1
        elif lst[y][x+1] == 1:
            x += 1
        elif lst[y-1][x] == 1:
            y -= 1
        if y == 0:
            print(f'#{test_case} {x}')
            break

