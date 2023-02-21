T =int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    lst = [[0]*N for i in range(N)]
    put = [list(map(int,input().split()))for i in range(M)]
    lst[N//2][N//2]=2
    lst[(N // 2)-1][(N // 2)-1] = 2
    lst[(N // 2)-1][N // 2] = 1
    lst[N // 2][(N // 2)-1] = 1
    dirx = [-1,0,1,-1,1,-1,0,1]
    diry = [-1,-1,-1,0,0,1,1,1]
    black = 0
    white = 0
    for i in range(M):
        lst[put[i][0]-1][put[i][1]-1]=put[i][2]
        for j in range(8):
            dx = dirx[j]+(put[i][1]-1)
            dy = diry[j]+(put[i][0]-1)
            if 0<=dx<N and 0<=dy<N:
                if lst[dy][dx]== 3-put[i][2]:
                    for k in range(2,N+1):
                        dx = dirx[j]*k + (put[i][1] - 1)
                        dy = diry[j]*k + (put[i][0] - 1)
                        if 0 <= dx < N and 0 <= dy < N:
                            if lst[dy][dx]==0:
                                break
                            if lst[dy][dx]==put[i][2]:
                                for z in range(k):
                                    dx = dirx[j]*z + (put[i][1] - 1)
                                    dy = diry[j]*z + (put[i][0] - 1)
                                    lst[dy][dx] = put[i][2]
                                break
    for i in range(N):
        for j in range(N):
            if lst[i][j]==1:
                black +=1
            if lst[i][j]==2:
                white +=1
    print(f'#{test_case} {black} {white}')








