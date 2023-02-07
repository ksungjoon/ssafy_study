
T = 10
for test_case in range(1, T + 1):
    N =int(input())
    lst = [[0]+list(map(int,input().split()))+[0] for i in range(100)]
    y=99
    x=0
    for i in range(1,101):
        if lst[y][i]==2:
            x=i
    while y>0:
        lst[y][x]=0
        if lst[y][x-1]==1:
            x -= 1
            continue
        elif lst[y][x+1] == 1:
            x += 1
            continue
        y -= 1

    print(f'#{test_case} {x-1}')


