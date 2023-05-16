from collections import deque
R,C = map(int,input().split())
lst = [list(map(str,input()))for i in range(R)]
visited = [[0]*C for _ in range(R)]
walk = [[0]*C for _ in range(R)]
drx=[0,-1,1,0]
dry=[-1,0,0,1]
j_que=deque()
f_que=deque()
k=0
r=0
flag=0
for i in range(R):
    for j in range(C):
        if lst[i][j]=='F':
            f_que.append((i,j))
        if lst[i][j]=='J':
            j_que.append((i,j))
            k=i
            r=j

def bfs():
    global  j_que,f_que,flag
    while f_que:
        a,b = f_que.popleft()
        for i in range(4):
            dy=dry[i]+a
            dx=drx[i]+b
            if 0<=dy<R and 0<=dx<C:
                if lst[dy][dx]!='#' and lst[dy][dx]!='F' and visited[dy][dx]==0:
                    visited[dy][dx]=visited[a][b]+1
                    f_que.append((dy,dx))
    visited[k][r] = 0
    while j_que and flag == 0:
        c,d= j_que.popleft()
        for j in range(4):
            dy=dry[j]+c
            dx=drx[j]+d
            if 0<=dy<R and 0<=dx<C:
                if lst[dy][dx]!='#' and visited[dy][dx]>=visited[c][d] and lst[dy][dx]!='F':
                    visited[dy][dx]=visited[c][d]+1
                    j_que.append((dy,dx))
            else:
                print(visited[c][d]+1)
                flag=1
                break
    if flag==0:
         print('IMPOSSIBLE')



bfs()
