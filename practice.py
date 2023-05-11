# N,M = map(int,input().split())
# lst = [i for i in range(1,N+1)]
# path = [0]*M
#
# def dfs(lev,start):
#     if lev==M:
#         print(*path,sep=' ')
#         return
#     for i in range(start,N):
#         path[lev]= lst[i]
#         dfs(lev+1,i)
#         path[lev] = 0
#
# dfs(0,0)
# name ='tkab'
# cnt = 0
# path=['']*3
#
# def abc(lev,start):
#     global cnt
#     if lev ==3:
#         for i in range(3):
#             print(path[i],end='')
#         print()
#         cnt+=1
#         return
#     for i in range(start,4):
#         path[lev]=name[i]
#         abc(lev+1,i)  # +1 만 지운거
#         path[lev]=0
# abc(0,0) # lev start
# print(cnt)
#
N = int(input())
lst = list(map(int,input().split()))
sign_lst = list(map(int,input().split()))
Max = -21e9
Min = 21e9
def dfs(lev,result):
    global Min,Max
    if lev==N-1:
        if result<Min:
            Min=result
        if result>Max:
            Max=result
        return
    for i in range(4):
        if sign_lst[i] != 0:
            sign_lst[i]-=1
            if i == 0:
                dfs(lev + 1, result+lst[lev+1])
            elif i == 1:
                dfs(lev + 1, result-lst[lev+1])
            elif i == 2:
                dfs(lev + 1, result*lst[lev+1])
            elif i == 3:
                dfs(lev + 1, result//lst[lev+1])
            sign_lst[i] += 1


dfs(0,lst[0])
print(Max)
print(Min)
