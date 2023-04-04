# N = int(input())
# lst = [list(map(int,input().split()))for i in range(N)]
# rd=[]
# ru=[]
# possible=0
# Max = -21e9
# cnt = 0
#
# for i in range(N):
#     for j in range(N):
#         if lst[i][j]==1 and i+j not in ru and i-j not in rd:
#             ru.append(i+j)
#             rd.append(i-j)
#             cnt +=1
# print(cnt)


# for i in range(N):
#     for j in range(N):
#         if lst[i][j]==1:
#             possible+=1
# def dfs(lev):
#     global cnt,Max
#     if flag == 1:
#         if Max<cnt:
#             Max=cnt
#
#         return
#     for i in range(N):
#         for j in range(N):
#             lev+=1
#             if lst[i][j]==1 and (i+j) not in ru and (i-j) not in rd:
#                 lst[i][j]=0
#                 ru.append(i+j)
#                 rd.append(i-j)
#                 dfs(lev,possible)
#
#                 ru.remove(i+j)
#                 rd.remove(i-j)



# N = int(input())
# lst = [list(map(int,input().split()))for i in range(N)]
# inf = 21e9
# arr = [[inf]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         cnt = 0
#         if lst[i][j]==1:
#             diry=[-1,-1,1,1]
#             dirx=[-1,1,-1,1]
#             for z in range(4):
#                 for k in range(1, N):
#                     dy = diry[z]*k+i
#                     dx = dirx[z]*k+j
#                     if 0<=dy<N and 0<=dx<N:
#                         if lst[dy][dx]==1:
#                             cnt+=1
#             arr[i][j]=cnt
# print(arr)
# for k in range(N//2*4):
#     for i in range(N):
#         for j in range(N):
#             flag = 0
#             if arr[i][j]==k:
#                 diry = [-1, -1, 1, 1]
#                 dirx = [-1, 1, -1, 1]
#                 for z in range(4):
#                     for h in range(1, N):
#                         dy = diry[z] * h + i
#                         dx = dirx[z] * h + j
#                         if 0 <= dy < N and 0 <= dx < N:
#                             if lst[dy][dx]==2:
#                                 flag=1
#                                 break
#                     if flag==1:
#                         break
#                 if flag ==1:
#                     continue
#                 else:
#                     lst[i][j]=2
# result = 0
# for i in range(N):
#     for j in range(N):
#         if lst[i][j]==2:
#             result+=1
# print(lst)
# print(result)



def check(idx):
    c = idx%2
    i, j = idx//n, idx%n

    for d in range(4):
        x, y = i+dx[d], j+dy[d]
        while 0<=x<n and 0<=y<n:
            if visited[x*n + y]:
                return False
            x += dx[d]
            y += dy[d]
    return True

def dfs(idx, c, cnt):
    if n*n-idx+1+cnt <= ans[c] or idx >= n*n:
        return

    ans[c] = max(ans[c], cnt)
    x, y = idx//n, idx%n
    j = y
    for i in range(x, n):
        while j < n:
            v = i*n + j
            if not visited[v] and chess[i][j] == 1 and check(v):
                visited[v] = True
                dfs(v, c, cnt+1)
                visited[v] = False
            j += 2
        j = (c+1)%2 if i%2 == 0 else c

n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 1, -1], [1, 1, -1, -1]
visited = [False] * (n**2)
ans = [0, 0]

dfs(0, 0, 0)
dfs(1, 1, 0)
print(sum(ans))