T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split()))for i in range(N)]
    Min = 21e9
    used = [0]*N

    def dfs(now,result):
        global Min
        if 0 not in used:
            if Min >result:
                Min = result
            return
        for i in range(N):
            if i == 0 and 0 in used[1:]: continue
            if used[i]==0 and lst[now][i]>0:
                used[i]=1
                dfs(i,result+lst[now][i])
                used[i] = 0

    dfs(0,0)
    print(f'#{test_case} {Min}')

    # def dfs(lev):
    #     global Min,result
    #     if lev == N:
    #         if Min >result:
    #             Min = result
    #         return
    #     for i in range(N):
    #         if used[i]==0 and  i!= lev:
    #             used[i]=1
    #             result += lst[lev][i]
    #             dfs(lev+1)
    #             used[i]=0
    #             result -= lst[lev][i]
    # used[0]=1
    # dfs(0)
    # print(Min)