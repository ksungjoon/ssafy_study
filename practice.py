# T = int(input())
# for test_case in range(1,T+1):
#     V,E = map(int,input().split())
#     lst = [list(map(int,input().split()))for i in range(E)]
#     S,G = map(int,input().split())
#     arr = [[0]*51for i in range(51)]
#     for i in range(E):
#         arr[lst[i][0]][lst[i][1]]=1
#     answer = []
#     cnt=0
#     def abc(start):
#         global answer,cnt
#         if G in answer:
#             return
#         que =[]
#         que.append(start)
#         while que:
#             now =que.pop(0)
#             answer.append(now)
#             for i in range(51):
#                 if arr[now][i] == 1:
#                     que.append(i)
#             cnt += 1
#     abc(S)
#     print(f'#{test_case} {cnt}')
# ----------------------------------------------------------


# T = int(input())
# for test_case in range(1,T+1):
#     N,M = map(int,input().split())
#     arr=[list(map(int,input().split()))for i in range(N)]
#     max_cost = 0
#     max_range = 0
#     max_cnt = -21e9
#     diry = [-1, 0, 0, 1]
#     dirx = [0, -1, 1, 0]
#     for i in range(N):
#         for j in range(N):
#             max_cost+=3*arr[i][j]
#     for K in range(60):
#         if K*K+(K-1)*(K-1)>max_cost:
#             max_range = K-1
#             break
#     for i in range(N):
#         for j in range(N):
#             used = [[0] * N for i in range(N)]
#             for k in range(max_range+1):
#
#                 cnt = 0
#                 for z in range(len(diry)):
#                     dy =diry[z]+i
#                     dx =dirx[z]+j
#                     if 0<=dy<N and 0<=dx<N:
#                         if arr[dy][dx]==1:
#                             cnt+=1
#                 if cnt*M>k*k+(k-1)*(k-1):
#                     if max_cnt<cnt:
#                         max_cnt = cnt
#     print(max_cnt)
#
# -----------------------------------------------




