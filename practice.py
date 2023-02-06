T = int(input())
for test_case in range(1, T + 1):
    result = 0
    lst = [[0]*10 for i in range(10)]
    N = int(input())
    lst2 = [list(map(int,input().split()))for i in range(N)]
    for i in range(N):
        for j in range(lst2[i][2]-lst2[i][0]+1):
            for k in range(lst2[i][3]-lst2[i][1]+1):
                lst[lst2[i][0]+j][lst2[i][1]+k] += lst2[i][4]
    for i in range(10):
        for j in range(10):
            if lst[i][j]==3:
                result += 1
    print(f'#{test_case} {result}')