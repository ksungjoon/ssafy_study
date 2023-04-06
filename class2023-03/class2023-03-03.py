from collections import deque
arr =[[0,0,0,0,1],[1,0,1,0,1],[1,0,1,0,0],[0,0,0,0,0]]
diry = [-1,0,0,1]
dirx = [0,-1,1,0]
cnt = 0
def abc(sty,stx,edy,edx):
    que =deque()
    que.append([sty,stx,0])
    used = [[0] * 5 for i in range(4)]
    used[sty][stx]=1
    while que:
        now =que.popleft()
        yy,xx,lev = now[0],now[1],now[2]
        if edy== yy and edx ==xx:
            return lev
        for i in range(4):
            dy =diry[i]+yy
            dx =dirx[i]+xx
            if 0<=dy<4 and 0<=dx<5:
                if used[dy][dx] ==0:
                    if arr[dy][dx]==0:
                        used[dy][dx]=1
                        que.append([dy,dx,lev+1])

cnt += abc(0,0,3,0)
cnt += abc(3,0,3,4)

print(cnt)
#
# 교수님이 푼거
#
# from collections import deque
# arr=[
#     [0,0,0,0,1],
#     [1,0,1,0,1],
#     [1,0,1,0,0],
#     [0,0,0,0,0],
# ]
# # 0,0에서 3,0 사료를 먹고 3,4 여자친구를 만나는데 최소 몇번 이동할까요?
# directy=[0,0,-1,1]
# directx=[1,-1,0,0]
# answer=0
#
# def bfs(sty,stx,edy,edx):
#     q=deque()
#     q.append([sty,stx,0])               # bfs 시작점 큐에 넣고 시작하기
#     used = [[0] * 5 for _ in range(4)]  # 중복체크 배열 선언하기
#     used[sty][stx]=1                    # 시작점좌표에 해당하는 중복체크 배열에 1체크
#     while q:
#         node=q.popleft()
#         yy,xx,level=node[0],node[1],node[2]         # 시작좌표 // level = 이동거리
#         if yy==edy and xx==edx:         # 도착점에 도착을 했을 경우
#             return level
#         for i in range(4):
#             dy=directy[i]+yy
#             dx=directx[i]+xx
#             if not (0<=dy<4 and 0<=dx<5): continue      # 배열범위 check
#             if used[dy][dx]==1: continue                # 중복 check
#             if arr[dy][dx]==1: continue                 # 벽이면 진입 못함 check
#             used[dy][dx]=1                      # 중복방지위한  1 체크
#             # if dy==edy and dx==edx:
#             #     return level+1
#             q.append([dy,dx,level+1])
# answer+=bfs(0,0,3,0)
# answer+=bfs(3,0,3,4)
# print(answer)


# 섬 크기 측정 bfs
# 내가 푼거
# from collections import deque
# lst =[[0,0,1,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]]
# diry = [-1,0,0,1]
# dirx = [0,-1,1,0]
# sty=0
# stx=0
# flag = 0
# for i in range(5):
#     for j in range(5):
#         if lst[i][j]==1:
#             sty,stx=i,j
#             flag=1
#             break
#     if flag == 1:
#         break
# cnt = 0
# def abc(y,x):
#     global cnt
#     que = deque()
#     que.append([y,x])
#     while que:
#         now = que.popleft()
#         for i in range(4):
#             dy = diry[i]+now[0]
#             dx = dirx[i]+now[1]
#             if 0<=dy<5 and 0<=dx<5:
#                 if lst[dy][dx]==1:
#                     lst[dy][dx]=0
#                     que.append([dy,dx])
#                     cnt+=1
# abc(sty,stx)
# print(cnt)

# 교수님이푼거
# from collections import deque
# map=[
#     [0,0,1,0,0],
#     [0,0,1,0,0],
#     [0,1,1,1,0],
#     [0,0,1,0,0],
#     [0,0,0,0,0],
# ]
# directy=[1,-1,0,0]
# directx=[0,0,1,-1]
#
# def bfs(y,x):
#     q=deque()
#     q.append([y,x])
#     size=0              # 섬개수 cnt
#     while q:
#         y,x=q.popleft()
#         for i in range(4):
#             dy=y+directy[i]
#             dx=x+directx[i]
#             if 0<=dy<5 and 0<=dx<5:             # 배열범위
#                 if map[dy][dx]==1:              # 섬이라면!!
#                     q.append([dy,dx])           # 큐에 넣기
#                     map[dy][dx]=0               # 섬을 바다로 바꾸기 (중복체크용도!!)
#                     size+=1                     # 섬 개수 1증가 (큐에 좌표를 넣을때 마다 1씩 증가)
#     return size
# for y in range(5):
#     for x in range(5):
#         if map[y][x]==1:
#             print(bfs(y,x))


# 섬들의 크기와 개수 조사 누가 최대값인지 최소값인지 출력

#  내가 푼거
# from collections import deque
# map=[
#     [0,0,1,0,1],
#     [0,0,1,0,1],
#     [0,1,1,1,0],
#     [0,0,1,0,0],
#     [1,0,0,1,1],
# ]
# directy=[1,-1,0,0]
# directx=[0,0,1,-1]
# size = []
# def bfs(y,x):
#     cnt = 0
#     que =deque()
#     que.append([y,x])
#     map[y][x]=0
#     while que:
#         cnt += 1
#         now = que.popleft()
#         for i in range(4):
#             dy =directy[i]+now[0]
#             dx =directx[i]+now[1]
#             if 0<=dy<5 and 0<=dx<5:
#                 if map[dy][dx]==1:
#                     que.append([dy,dx])
#                     map[dy][dx]=0
#
#     return cnt
# resultcnt=0
# for i in range(5):
#     for j in range(5):
#         if map[i][j]==1:
#             size.append(bfs(i,j))
#             resultcnt+=1
# print(resultcnt)
# print(max(size))
# print(size)

# 교수님이 푼 거거

# from collections import deque
# arr=[
#     [0,0,1,0,1],
#     [0,0,1,0,1],
#     [0,1,1,1,0],
#     [0,0,1,0,0],
#     [1,0,0,1,1],
# ]
# directy=[1,-1,0,0]
# directx=[0,0,1,-1]
#
# def bfs(y,x):
#     q=deque()
#     q.append([y,x])
#     size = 0                # 섬의 크기
#     while q:
#         size+=1             # 섬 크기 1씩 증가
#         now=q.popleft()
#         y,x=now
#         for i in range(4):
#             dy,dx=y+directy[i],x+directx[i]
#             if dy<0 or dy>4 or dx<0 or dx>4: continue # 배열범위
#             if visit[dy][dx]==1: continue       # 중복체크
#             if arr[dy][dx]==0: continue         # 바다라면 안됨
#             visit[dy][dx]=1                     # 방문체크 해주고
#             q.append([dy,dx])                   # 큐 등록
#     return size
#
# cnt=0
# visit=[[0]*5 for _ in range(5)]
#
# for y in range(5):
#     for x in range(5):
#         if arr[y][x]==1 and visit[y][x]==0:         # 섬이고 방문한적이 없다면
#             visit[y][x]=1                           # 방문체크 해주고
#             cnt+=1                                  # 섬 개수 1증가 시켜주고
#             print(f'{cnt}번 째 섬 크기는 {bfs(y,x)}')     # bfs 들어가기
# print(f'섬의 총 개수는 {cnt}')