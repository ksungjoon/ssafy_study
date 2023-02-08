T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    lst = [list(map(str,input()))for i in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            a = []
            b = []
            for k in range(j,j+M):
                b.append(lst[i][k])
            for k in range(j+M-1,j+1,-1):
                a.append(lst[i][k])
            if a == b:
                print(f'#{test_case}',end=' ')
                print(*a,sep='')
    for i in range(N):
        for j in range(N-M+1):
            a=[]
            b=[]
            for k in range(j,j+M):
                b.append(lst[k][i])
            for k in range(j+M-1,j+1,-1):
                a.append(lst[k][i])
            if a == b:
                print(f'#{test_case}',end=' ')
                print(*a,sep='')

    # for i in range(M):
    #     a = []
    #     b = []
    #     for j in range(N):
    #         a.append(lst[j][i])
    #         b.append(lst[N-1-j][i])
    #     if a == b:
    #         print(f'#{test_case}',end=' ')
    #         print(*a,sep='')







    # for i in range(N):
    #     a = []
    #     b = []
    #     for j in range(M):
    #         a.append(lst[i][j])
    #         b.append(lst[i][-(j+1)])
    #     if a == b:
    #         print(f'#{test_case}',end=' ')
    #         print(*a,sep='')
    # for i in range(M):
    #     a = []
    #     b = []
    #     for j in range(N):
    #         a.append(lst[j][i])
    #         b.append(lst[N-1-j][i])
    #     if a == b:
    #         print(f'#{test_case}',end=' ')
    #         print(*a,sep='')