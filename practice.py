# import sys
# from collections import deque
# input = sys.stdin.readline
# R,C = map(int,input().split())
# lst = [list(map(str,input()))for i in range(R)]
# fire = [[0]*C for _ in range(R)]
# work = [[0]*C for _ in range(R)]
# drx=[0,-1,1,0]
# dry=[-1,0,0,1]
# j_que=deque()
# f_que=deque()
# flag=0
# for i in range(R):
#     for j in range(C):
#         if lst[i][j]=='F':
#             f_que.append((i,j))
#         if lst[i][j]=='J':
#             j_que.append((i,j))
#
# def bfs():
#     global  j_que,f_que,flag
#     while f_que:
#         a,b = f_que.popleft()
#         for i in range(4):
#             dy=dry[i]+a
#             dx=drx[i]+b
#             if 0<=dy<R and 0<=dx<C:
#                 if lst[dy][dx]!='#' and lst[dy][dx]!='F' and fire[dy][dx]==0:
#                     fire[dy][dx]=fire[a][b]+1
#                     f_que.append((dy,dx))
#     while j_que and flag == 0:
#         c,d= j_que.popleft()
#         for j in range(4):
#             dy=dry[j]+c
#             dx=drx[j]+d
#             if 0<=dy<R and 0<=dx<C:
#                 if lst[dy][dx]!='#'and lst[dy][dx]!='F'and lst[dy][dx]!='J'and fire[dy][dx]>work[c][d]+1 and work[dy][dx]==0:
#                     work[dy][dx]=work[c][d]+1
#                     j_que.append((dy,dx))
#             else:
#                 print(work[c][d]+1)
#                 flag=1
#                 break
#     if flag==0:
#          print('IMPOSSIBLE')
#
#
#
# bfs()
#
#
from collections import deque

N,K = map(int,input().split())
cnt_lst=[0]*100001
def bfs(st):
    que = deque()
    que.append(st)
    while que:
        a = que.popleft()
        if a == K:
            return cnt_lst[a]
        for i in (a-1,a+1,a*2):
            if 0<= i <= 100000 and not cnt_lst[i]:
                cnt_lst[i]=cnt_lst[a]+1
                que.append(i)
print(bfs(N))