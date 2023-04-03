# N castle 문제 민코딩 알고리즘 탑 backtracking top
# N = int(input())
# cnt = 0
# arr = [[0]*N for _ in range(N)]
# def cont(lev):
#     global cnt
#     if lev == N:
#         cnt += 1
#         return
#     for i in range(N):
#         if castle(lev,i):
#             arr[lev][i]=1
#             cont(lev+1)
#             arr[lev][i]=0
#
# def castle (i,j):
#     diry,dirx = -1,0
#     for k in range(N):
#         dy = diry*k+i
#         dx = dirx*k+j
#         if 0<=dy<N and 0<=dx<N:
#             if arr[dy][dx]==1:
#                 return 0
#     return 1
# cont(0)
# print(cnt)

# N queen 문제 민코딩 알고리즘 탑 backtracking top
# import sys
# sys.setrecursionlimit(15000)
# N = int(input())
# cnt = 0
# arr = [[0]*N for _ in range(N)]
# def cont(lev):
#     global cnt
#     if lev == N:
#         cnt += 1
#         return
#     for i in range(N):
#         if queen(lev,i):
#             arr[lev][i]=1
#             cont(lev+1)
#             arr[lev][i]=0
#
# def queen (i,j):
#     for diry,dirx in [[-1,0],[-1,-1],[-1,1]]:
#         for k in range(N):
#             dy = diry*k+i
#             dx = dirx*k+j
#             if 0<=dy<N and 0<=dx<N:
#                 if arr[dy][dx]==1:
#                     return 0
#     return 1
# cont(0)
# print(cnt)


# queen 을 우상향 우하향을 사용한 풀이 (교수님 풀이)

n=int(input())
dat=[0]*n
rup=[0]*n*2
rdown=[0]*n*2
cnt=0

def abc(level):
    global cnt;
    if level==n:
        cnt+=1
        return
    for i in range(n):
        if dat[i]==1: continue
        if rup[level+i]==1: continue
        if rdown[(level-i)+n-1]==1: continue
        rup[level + i] = 1
        rdown[(level - i) + n - 1]=1
        dat[i]=1
        abc(level+1)
        dat[i]=0
        rup[level+i]=0
        rdown[(level - i) + n - 1]=0

abc(0)
print(cnt)


# DIJKSTRA- 최단 거리구할때쓰는 공식
#
# 다익스트라 (O n^2) 속도 코드
# 다익스트라 : 한 정점에서 다른 모든 도착점 까지의 최소비용을 구하는 알고리즘


# name='ABCDE'
# inf=int(21e8)
# arr=[
#     [0,3,inf,9,5],
#     [inf,0,7,inf,1],
#     [inf,inf,0,1,inf],
#     [inf,inf,inf,0,inf],
#     [inf,inf,1,inf,0]
# ]
# used=[0]*5 # 경유지 선택 여부 체크
# result=[0,3,inf,9,5] # 시작점에서 모든 정점까지 최소비용 갱신 테이블
# used[0]=1 # A에서 시작할 것임으로 0번인덱스에 1체크
#
# def select_ky():
#     Min=int(21e8)
#     Minindex=0
#     for i in range(5):
#         if used[i]==0 and result[i]<Min: # 경유지로 선택한 적이 없고 그리고
#             Min=result[i]                   # 시작점에서 경유지까지 드는 비용 중 최소비용드는 곳을
#             Minindex=i                          # 우선적으로 경유지로 선택!!
#     return Minindex
#
#
# def dijkstra():
#     # 경유지 선택
#     for i in range(4):
#         via=select_ky()
#         used[via]=1
#         # 경유지 선택 후 모든 정점까지의 최소비용 갱신하기
#         for j in range(5):
#             baro=result[j] # 시작점에 -> 다른 모든 도착점까지 비용
#             ky=result[via]+arr[via][j] # 시작점->경유   +    경유 -> 도착점
#             if baro>ky:
#                 result[j]=ky
# dijkstra()
# print(*result)