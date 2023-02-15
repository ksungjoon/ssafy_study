# 1행당 1나씩 선택했을때 합이 20보다 큰 경우의 개수
# arr = [[4,5,2],
#        [-2,1,6],
#        [3,9,-4],
#        [3,5,2]]
# cnt = 0
# sum = 0
# def abc(lev):
#     global cnt,sum
#     if lev==4:
#         if sum >20:
#             cnt+=1
#         return
#     for i in range(3):
#         sum += arr[lev][i]
#         abc(lev+1)
#         sum -= arr[lev][i]
# abc(0)
# print(cnt)
# 위에서 부터 한칸 씩 내려오면서
# 숫자 한개씩을 선택합니다,
# 선택한 숫자들을 모두 더했을 때
# 합이 20 이상인 경우가 몇가지 인지 출력해 주세요

# arr=[[4,5,2],
#      [-2,1,6],
#      [3,9,-4],
#      [3,5,2]]
#
# cnt=0
#
# def dfs(level,sum):
#     global cnt
#     if level==4:
#         if sum>20:
#             cnt+=1
#         return
#     for i in range(3):
#         dfs(level+1,sum+arr[level][i])
#
# dfs(0,0)
# print(cnt)

# 모두 곱했을때 MAX 값
# arr=[[3,5,9],
#      [7,-8,1],
#      [-10,2,3],
#      [5,1,2]]
# max = 0
# def abc(lev,gop):
#     global max
#     if lev==4:
#         if gop>max:
#             max =gop
#         return
#     for i in range(3):
#         abc(lev+1,gop*arr[lev][i])
# abc(0,1)
# print(max)


# 위에서 부터 한칸 씩 내려오면서
# 숫자 한개씩을 선택합니다.
# 계단을 밑으로 내려오면서 이동할 수 있는 범위는
# 7시방향 6시방향 5시방향 입니다.
# 선택한 숫자들을 모두 더했을 때
# 합이 30 이상인 경우가 몇가지 인지 출력해 주세요

# arr=[[3,5,9,6],
#      [7,-8,1,6],
#      [-10,2,3,9],
#      [5,1,2,8],
#      [4,7,1,8]]
# cnt=0
# def dfs(now,level,sum):
#      global cnt
#      if level==5:
#           if sum>30:
#                cnt+=1
#           return
#      for i in range(3):
#          direct=[-1,0,1]
#          dy=level
#          dx=now+direct[i]
#          if dx<0 or dx>3: continue
#          dfs(dx,level+1,sum+arr[dy][dx])
#
# for i in range(4):
#      dfs(i,1,arr[0][i])     #now level sum
# print(cnt)
#
# 미로찾기
# 0,0,0,0
# 1,0,1,0
# 1,0,1,0
# 0,0,0,0
# 0,0 에서 출발해서 3,3까지 도착하고자 한다.
# 방탈출이 가능한지 불가능 한지 출력해 주세요

# 내가 푼거
# arr = [[0,0,0,0],
#        [1,0,1,0],
#        [1,0,1,0],
#        [0,0,0,0]]
# result = 0
#
# def abc (nowy,nowx):
#     global result
#     if nowy==3 and nowx==3:
#         result +=1
#         return
#     for i in range(4):
#         diry = [-1, 0, 0, 1]
#         dirx = [0, -1, 1, 0]
#         dy =diry[i] + nowy
#         dx = dirx[i] +nowx
#         if 0<=dy<4 and 0<=dx<4:
#             if arr[dy][dx] == 0:
#                 arr[dy][dx] = 1
#                 abc(dy,dx)
#                 arr[dy][dx] = 0
# abc(0,0)
# if result !=0:
#     print('완료')
# elif result == 0:
#     print('실패')
# print(result)

# 교수님이 푼거
#
# arr=[[0,0,0,0],
#      [1,0,1,0],
#      [1,0,1,0],
#      [0,0,0,0]]
#
# visit=[[0]*4 for _ in range(4)]
# directy=[-1,1,0,0]
# directx=[0,0,-1,1]
# flag=0
# def dfs(y,x):
#     global flag
#     if y==3 and x==3:
#         flag=1
#         return
#
#     for i in range(4):
#         dy=y+directy[i]
#         dx=x+directx[i]
#         if dy<0 or dx<0 or dy>3 or dx>3: continue
#         if arr[dy][dx]==1: continue
#         if visit[dy][dx]==1: continue
#         visit[dy][dx]=1
#         dfs(dy,dx)
#         if flag==1:
#             return
# visit[0][0]=1
# dfs(0,0)   # 시작점의 좌표값을 넣어주기
# if flag==1:
#     print('도착가능')
# else:
#     print('불가능')
#
# # 미로찾기
# # 0,0,0,0
# # 1,0,1,0
# # 1,0,1,0
# # 0,0,0,0
# # 0,0 에서 출발해서 3,3까지 도착하고자 한다.
# # 방탈출이 가능한지 불가능 한지 출력해 주세요
# arr = [[0, 0, 0, 0],
#        [1, 0, 1, 0],
#        [1, 0, 1, 0],
#        [0, 0, 0, 0]]
#
# directy = [-1, 1, 0, 0]
# directx = [0, 0, -1, 1]
# flag = 0
#
#
# def dfs(y, x):
#     global flag
#     if y == 3 and x == 3:  # 원하는 도착점에 도착 했을 시
#         flag = 1  # flag 1 켜주고 (why? 원하는 목적 달성하고 dfs탐색을 종료 하기 위함)
#         return
#
#     for i in range(4):
#         dy = y + directy[i]  # 현재 위치에서의 4방향 좌표값을 dy,dx에 넣고
#         dx = x + directx[i]
#
#         if dy < 0 or dx < 0 or dy > 3 or dx > 3: continue  # 배열 범위 검사
#         if arr[dy][dx] == 1: continue  # 벽 검사
#         if arr[dy][dx] == 2: continue  # 중복체크 검사가 다 통과가 되었다면!!
#
#         arr[dy][dx] = 2  # 중복 방지를 위해 앞으로 들어갈 곳을 2 체크하고
#         dfs(dy, dx)  # 들어가기!!!!
#         if flag == 1:  # 원하는바 찾았으면 무조건 리턴하기(더이상 dfs 탐색 안하기)
#             return
#
#
# arr[0][0] = 2  # 시작점의 좌표를 2로 바꿔주기 (중복체크를 위함)
# dfs(0, 0)  # 시작점의 좌표값을 넣어주기
# if flag == 1:
#     print('도착가능')
# else:
#     print('불가능')

# arr=[[0,0,0,0],
#      [1,0,1,0],
#      [1,0,1,0],
#      [0,0,0,0]]
# result = 0
#
# def abc(nowy,nowx):
#     global result
#     if nowy==3 and nowx==3:
#         result += 1
#         return
#     for i in range(4):
#         diry = [-1,0,0,1]
#         dirx = [0,-1,1,0]
#         dy = diry[i]+nowy
#         dx = dirx[i]+nowx
#         if 0 <= dy <4 and 0<=dx<4:
#             if arr[dy][dx]==0:
#                 arr[dy][dx]=1
#                 abc(dy,dx)
#                 arr[dy][dx]=0
#                 if result == 1:
#                     return
# abc(0,0)
# if result == 1:
#     print('완료')
# else:
#     print('실패')
#
# 0,0에서 1,3 까지 최단 거리 구하기
# 내가 푼거
# arr=[[0,0,0,0,1],
#      [1,0,1,0,1],
#      [1,0,1,0,1],
#      [1,0,1,0,1],
#      [1,0,1,0,1]]
# count = 0
# mincnt = 21e9
# def abc(nowy,nowx):
#     global mincnt,count
#     if nowy==1 and nowx==3:
#         if mincnt>count:
#             mincnt = count
#             return
#     for i in range(4):
#         diry = [-1,1,0,0]
#         dirx = [0,0,-1,1]
#         dy = diry[i]+nowy
#         dx = dirx[i]+nowx
#         if 0<=dy<5 and 0 <=dx<5:
#             if arr[dy][dx]==0:
#                 arr[dy][dx]=1
#                 count+=1
#                 abc(dy,dx)
#                 count-=1
#                 arr[dy][dx]=0
# abc(0,0)
# print(mincnt)

# 교수님이 푼거

# 0,0 좌표에서 1,3 까지의 최단거리 구하기 (DFS 이용)
# arr=[[0,0,0,0,1],
#      [1,0,1,0,1],
#      [1,0,1,0,1],
#      [1,0,1,0,1],
#      [0,0,0,0,0]]
# visit=[[0]*5 for _ in range(5)]
#
# directy=[0,0,-1,1]
# directx=[1,-1,0,0]
# Min=int(21e8)
# def dfs(y,x,level):
#     global Min
#     if y==1 and x==3:
#         # 최소레벨 갱신
#         if level<Min:
#             Min=level
#         return
#     for i in range(4):
#         dy=y+directy[i]
#         dx=x+directx[i]
#         if dy<0 or dx<0 or dy>4 or dx>4: continue
#         if visit[dy][dx]==1: continue
#         if arr[dy][dx]==1: continue
#         visit[dy][dx]=1
#         dfs(dy,dx,level+1)
#         visit[dy][dx]=0
#
# visit[0][0]=1
# dfs(0,0,0)  # y,x,level
# print(Min)











