from collections import deque
import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
lst = [[]for i in range(N+1)]
cnt = 0
visited=[0]*(N+1)
result=[]
for i in range(M):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
for j in lst:
    j.sort()

def bfs (st):
    global cnt
    que = deque()
    que.append(st)
    while que:
        a=que.popleft()
        if a not in result:
            result.append(a)
        for i in lst[a]:
           que.append(i)

bfs(R)
print(result)
# for i in range(1,N+1):
#     print(visited[i])
