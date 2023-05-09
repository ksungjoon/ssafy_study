N,M = map(int,input().split())
lst = [i for i in range(1,N+1)]
path = [0]*M

def dfs(lev,start):
    if lev==M:
        print(*path,sep=' ')
        return
    for i in range(start,N):
        path[lev]= lst[i]
        dfs(lev+1,i)
        path[lev] = 0

dfs(0,0)
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

lst = [list(map(int,input().split()))for i in range(9)]
def result(lst):
    set(lst)