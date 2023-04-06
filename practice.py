# from collections import deque
# T = int(input())
# for test_case in range(1,T+1):
#     V,E = map(int,input().split())
#     lst = [list(map(int,input().split()))for i in range(E)]
#     S,G = map(int,input().split())
#     used = [0]*(V+1)
#     arr = [[0]*(V+1)for i in range(V+1)]
#     for i in range(E):
#         arr[lst[i][0]][lst[i][1]]=1
#         arr[lst[i][1]][lst[i][0]]=1
#
#     def bfs (st):
#         que = deque()
#         que.append((st,0))
#         while que:
#             now ,cnt = que.popleft()
#             if now ==G:
#                 return cnt
#             for i in range(V+1):
#                 if used[i]==0 and arr[now][i]==1:
#                     used[i]=1
#                     que.append((i,cnt+1))
#         return 0
#     used[S]=1
#     print(f'#{test_case} {bfs(S)}')

from collections import deque
T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    que = deque()
    result = []
    for i in range(N):
        que.append((i,lst[i]))
    while que:
        num,che = que.popleft()
        che = che//2
        if che !=0:
            que.append((num,che))
        else:
            if N==M:
                continue
            result.append(num)
            que.append((N,lst[N]))
            N+=1
    print(result)




