T = int(input())
for test_case in range(1,T+1):
    lst = list(map(int,input().split()))
    N = lst[0]
    stop = lst[1:]
    Min = 21e9
    def dfs (start, battery,cnt):
        global Min
        if cnt >Min:
            return
        if start>= N-1:
            if cnt <Min:
                Min = cnt
            return

        for i in range(stop[start],0,-1):
            dfs(start+i,battery-i+stop[i],cnt+1)
    dfs(0,stop[0],-1)
    print(f'#{test_case} {Min}')