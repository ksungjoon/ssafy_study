# DFS
# BFS
#tree
# people = ['A','B','D','C','E','F']
# 1. 인접 행렬(이차 배열)
  #     A B D C E F
# arr = [[0,1,0,1,0,0], #A                            A
#        [0,0,1,0,0,0], #B                          B    C
#        [0,0,0,0,0,0], #D                        D     E F
#        [0,0,0,0,1,1], #C
#        [0,0,0,0,0,0], #E
#        [0,0,0,0,0,0]] #F
# 2. 인접 리스트
# lst = [[]for i in range(6)]
# lst[0].append('B')     # A -B -C
# lst[0].append('C')     # B -D
# lst[1].append('D')     # D
# lst[3].append('E')     # C -E -F
# lst[0].append('F')     # E
#                        # F

# 3. 리스트 (일차원 배열 - 이진트리)
# [_,A,B,C,D,_,E,F]


# DFS
# 깊이 우선 탐색
# 탐색 순서 출력하기

# tree 노드 탐색(1번씩)
#               A(0)
#         B(1)           C(2)
#    D(3)     E(4)            F(5)
# name  = list(input().split())
# arr = [[0,1,1,0,0,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,0,1],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# answer = []
# def dfs(now):
#     global answer
#     answer.append(name[now])
#
#     for i in range(6):
#         if arr[now][i] == 1:
#             dfs(i)
#
# dfs(0)
# print(*answer)

# 연습문제

# name = list(input().split())
# arr = [[0,1,1,1,0,0,0],
#        [0,0,0,0,1,1,0],
#        [0,0,0,0,0,0,1],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0]]
# result = []
# def dfs(now):
#     global result
#     result.append(name[now])
#
#     for i in range(7):
#         if arr[now][i] == 1:
#             dfs(i)
# dfs(0)
# print(*result)

# 트리 모양이 아닌 그래프 node 탐색
# 1 번씩 탐색 출력하기
# name = list(input().split()) #  B A C D
# arr = [[0,0,1,1],
#        [1,0,0,0],
#        [0,1,0,1],
#        [0,0,0,0]]
# used = [0]*4
# result = []
#
# def dfs(now):
#     global result
#     result.append(name[now])
#     for i in range(4):
#         if arr[now][i]==1: # 인접행렬 탐색하다가 1체크가 되어잇으면
#             if used[i] == 0 : # 한번도 방문한 적이 없으면
#                 used[i]=1   # 방문체크 해주고
#                 dfs(i)      # 들어가기
# used[0] = 1   # 탐색 시작 인덱스에 1 들어가고
# dfs(0)          # dfs 탐색
# print(*result)

# graph의 경로탐색
# A 에서 출발해서  D에 도착하는 경우의 수
# name = list(input().split()) #  B A C D
# arr = [[0,0,1,1],
#        [1,0,1,0],
#        [1,0,0,1],
#        [0,0,0,0]]
# used = [0]*4
# cnt = 0
# def dfs(now):
#     global cnt
#     if now ==3:
#         cnt += 1
#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i] = 1
#             dfs(i)
#             used[i] = 0
# used[1]=1
# dfs(1)
# print(cnt) # 4

# 경로 탐색
# path 배열 찍기
# name = list(input().split())  # B A C D
# arr = [
#     [0, 0, 1, 1],
#     [1, 0, 1, 0],
#     [1, 0, 0, 1],
#     [0, 0, 0, 0]]
# used = [0] * 4
# answer = 0
# path = []
# def dfs(now):
#     global answer
#     path.append(name[now])
#     if now == 3:
#         answer += 1
#         print(*path)
#         return
#     for i in range(4):
#         if arr[now][i] == 1 and used[i] == 0:
#             used[i] = 1
#             dfs(i)
#             used[i] = 0
#             path.pop()
# used[1] = 1
# dfs(1)
# print(answer)

# 해당 위치에서 원하는 위치까지 가는 경로중 최소 비용
# name = list(input().split())  # B A C D
# arr = [
#     [0, 0, 3, 14],
#     [7, 0, 19, 0],
#     [3, 0, 0, 1],
#     [0, 0, 0, 0]]
# used = [0]*4
# lst = []
# # A에서 D까지 가는데 최소비용을 구하기
# # 전역 변수
# sum = 0
# def dfs(now):
#     global sum
#     if now == 3:
#         lst.append(sum)
#         sum = 0
#         return
#     for i in range(4):
#         if arr[now][i]>=0 and used[i] == 0:
#             sum += arr[now][i]
#             used[i] =1
#             dfs(i)
# used[1]=1
# dfs(1)
# print(min(lst))

# 교수님이 푼거
# sum 을 전역으로 두었을때
# name=list(input().split())   # B A C D
# arr=[[0,0,3,14],
#     [7,0,19,0],
#     [3,0,0,1],
#     [0,0,0,0]]
#
# # A 에서 D 까지 가는 데 최소비용을 구하기
# used=[0]*4
# Min=999999999999999999999999
# sum=0
# def dfs(now):
#     global Min,sum
#     if now==3:
#         if sum<Min:     # 최소sum 구하기
#             Min=sum
#         return
#     for i in range(4):
#         if arr[now][i]>0: #이동할 수 있는 곳이라면
#             if used[i]==0: # 한번도 방문한 적이 없는 곳이라면
#                 used[i]=1
#                 sum+=arr[now][i]
#                 dfs(i)
#                 used[i]=0
#                 sum-=arr[now][i]
#
# used[1]=1
# dfs(1)     # 시작인덱스1 // sum=0
# print(Min)


# sum을 매개변수로 두었을때
# name=list(input().split())   # B A C D
# arr=[[0,0,3,14],
#     [7,0,19,0],
#     [3,0,0,1],
#     [0,0,0,0]]
#
# # A 에서 D 까지 가는 데 최소비용을 구하기
# used=[0]*4
# Min=999999999999999999999999
#
# def dfs(now,sum):
#     global Min
#     if now==3:
#         if sum<Min:     # 최소sum 구하기
#             Min=sum
#         return
#     for i in range(4):
#         if arr[now][i]>0: #이동할 수 있는 곳이라면
#             if used[i]==0: # 한번도 방문한 적이 없는 곳이라면
#                 used[i]=1
#                 dfs(i,sum+arr[now][i])
#                 used[i]=0
#
# used[1]=1
# dfs(1,0)     # 시작인덱스1 // sum=0
# print(Min)

# 연습 문제

# lst = ['A','B','C','D','E']
# a = input()
# arr = [[0,1,0,0,0],
#        [0,0,1,1,1],
#        [1,0,0,1,0],
#        [0,0,0,0,1],
#        [0,0,0,0,0]]
# used = [0]*len(arr)
# root = 0
# now = 0
# for i in range(len(lst)):
#     if lst[i]==a:
#         now = i
#
# def dfs (now):
#     global root
#     if now == 4:
#         root += 1
#         return
#     for i in range(5):
#         if arr[now][i] == 1 and used[i]==0:
#             used[i] = 1
#             dfs(i)
#             used[i] = 0
# used[now] = 1
# dfs(now)
# print(root)
#
# lst = ['A','B','C','D','E']
# a = input()
# arr = [[0,4,0,0,0],
#        [0,0,1,2,9],
#        [5,0,0,7,0],
#        [0,0,0,0,1],
#        [0,0,0,0,0]]
# used = [0]*len(arr)
# min = 21e9
# sum = 0
# now = 0
# for i in range(len(lst)):
#     if lst[i]==a:
#         now = i
# def dfs(now):
#     global sum,min
#     if now == 4:
#         if min > sum:
#             min = sum
#         return
#     for i in range(5):
#         if arr[now][i]>0 and used[i] == 0:
#             used[i]=1
#             sum += arr[now][i]
#             dfs(i)
#             used[i]=0
#             sum -= arr[now][i]
#
# used[now] = 1
# dfs(now)
# print(min)

