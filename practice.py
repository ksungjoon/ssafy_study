T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    chess = [[0]*N for i in range(N)]
    cnt = 0
    def check(i):
        global cnt
        if i ==N:
            cnt+=1
            return
        for j in range(N):
            if possible(i,j):
                chess[i][j]=1
                check(i+1)
                chess[i][j]=0
    def possible(i,j):
        for diry,dirx in [[-1,-1],[-1,0],[-1,1]]:
            dy = i+diry
            dx = j+dirx
            while 0<=dy<N and 0<=dx<N:
                if chess[dy][dx]:
                    return 0
                dy += diry
                dx += dirx
        return 1
    check(0)
    print(f'#{test_case} {cnt}')








    # def f(i):
    #     global cnt
    #     if i ==N:
    #         cnt+=1
    #     else:
    #         for j in range(N):
    #             if promising(i,j):
    #                 chess[i][j]=1
    #                 f(i+1)
    #                 chess[i][j]=0
    #
    # def promising(y,x):
    #     for dy, dx in [[-1,-1],[-1,0],[-1,1]]:
    #         ny, nx = y+dy,x+dx
    #         while 0<=ny<N and 0<=nx<N:
    #             if chess[ny][nx]:
    #                 return 0
    #             ny,nx = ny+dy, nx+dx
    #     return 1
    #
    # f(0)
    # print(f'#{test_case} {cnt}')



