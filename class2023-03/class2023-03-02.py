from collections import deque
# bfs
# name = ['A','B','C','D']
# arr = [[0,1,1,0],
#        [0,0,1,1],
#        [0,1,0,1],
#        [0,0,0,0]]
# used = [0]*4
# result = []
# def bfs (strat):
#     que = deque()
#     que.append(strat)
#     while que:
#         now = que.popleft()
#         result.append(name[now])
#         for i in range(4):
#             if arr[now][i]==1 and used[i]==0:
#                 used[i]=1
#                 que.append(i)
# used[0]=1
# bfs(0)
# print(result)

# flod fill


# from collections import deque
# n=int(input()) # 맵 사이즈 입력
# arr=[[0]*n for _ in range(n)]
# y,x=map(int,input().split())    #시작좌표 입력
#
# arr[y][x]=1    # 화단의 시작좌표에 1 체크
#
# q=deque()
# q.append([y,x]) # 시작좌표 큐에 넣어주기
#
# directy=[-1,1,0,0]
# directx=[0,0,-1,1]
# answer=0
# while q:
#     now =q.popleft()
#     y,x=now[0],now[1]
#     # answer=arr[y][x]
#     for i in range(4):
#         dy=y+directy[i]
#         dx=x+directx[i]
#         if 0<=dy<n and 0<= dx<n: # 배열 범위 안이라면
#             if arr[dy][dx]==0: # 이미 꽃이 핀 곳이 아니라면
#                 arr[dy][dx]=arr[y][x]+1 #지금 현재 배열에 적힌 값 +1 한것을 적어주기
#                 answer=arr[dy][dx]  # 정답 저장하기
#                 q.append([dy,dx])
#
# print(arr) # 몇일째 화단에 꽃이 만개가 되는지 출력 !!

# 화단에 꽃을 심을 좌표 2개

from collections import deque
n = int(input()) # 배열 크기입력
flower = list(map(int, input().split())) # 좌표 입력
y1, x1 = flower[0], flower[1] # 시작 좌표값 저장
y2, x2 = flower[2], flower[3]
flower = [(y1, x1,1), (y2, x2,1)] # 좌표 level을 같이 튜플로 넣기
arr = [[0] * n for _ in range(n)]  # 화단 선언

answer=0

def bfs(flower):
    global n, arr,answer
    q=deque(flower)             # 큐에 시작좌표 넣어주기

    while q:
        nowy,nowx,level=q.popleft()

        arr[nowy][nowx]=level   # 배열에 현재 레벨 넣어주기
        answer=level            # 큐가 돌때마다 정답을 저장하기

        directy=[-1,1,0,0]
        directx=[0,0,-1,1]

        for i in range(4):
            dy=nowy+directy[i]
            dx=nowx+directx[i]
            if not(0<=dy<n and 0<=dx<n):continue # 배열범위벗어나면 안됨
            if arr[dy][dx]!=0: continue # 이미 꽃이 심어진곳 안됨
            arr[dy][dx]=arr[nowy][nowx]+1 # 화단에 표시해주기
            q.append((dy,dx,level+1)) # 큐에 푸쉬하기

bfs(flower)

for row in arr:
    print(*row,sep="")
print(answer)