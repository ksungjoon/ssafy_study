# 교수님이 주신연습 문제
# 내가 푼 방식
# T = int(input())
# for test_case in (1,T+1):
#     N = int(input())
#     lst = [list(map(int,input().split()))for i in range(N)]
#     dirx =[-1,0,1,-1,1,-1,0,1]
#     diry =[-1,-1,-1,0,0,1,1,1]
#     max = 0
#     resultmax = 0
#     count = 0
#     resultcnt=0
#     for i in range(1,N-1):
#         for j in range(1,N-1):
#             count=0
#             max = 0
#             for k in range(8):
#                 if lst[i][j]<lst[i+diry[k]][j+dirx[k]]:
#                     count +=1
#                     if lst[i+diry[k]][j+dirx[k]]-lst[i][j]>max:
#                         max = lst[i+diry[k]][j+dirx[k]]-lst[i][j]
#             if count == 8:
#                 resultcnt+=1
#                 if resultmax<max:
#                     resultmax = max
#     print(f'#{test_case} {resultcnt} {resultmax}')

# 자료구조 -데이터를 관리하거나 저장하는 방식
# 자료구조 -저장   - 선형
#                -비선형
#
#         -관리처리  - stack -LIFO
#                  - queu -FIFO

# 구간합
# sliding window
# prefix sum
# two pointer
# n개의 숫자 연속된 m개의 숫자의 합이 max
# sliding window
# n,m=map(int,input().split())
# lst = list(map(int,input().split()))
# sum = 0
# max = 0
# for i in range(m):
#     sum+= lst[i]
# for j in range(n-m):
#     sum-=lst[j]
#     sum+=lst[j+m]
#     if sum>max:
#         max = sum
#
# print(max)
# 교수님 설계대로 푼거
# for i in range(m):  # 처음 첫 m개 구간의 합 구하기
#     sum+=arr[i]
# for i in range(n-m+1):
#     if sum>Max:
#         Max=sum
#     if i==n-m:
#         break
#     sum+=arr[i+m]
#     sum-=arr[i]
# print(Max)
# 투포인터 내가 푼 문제
# n,m= map(int,input().split())
# lst =list(map(int,input().split()))
# cnt = 0
# sum =0
# for i in range(n):
#     sum = 0
#     for j in range(i,n):
#         sum += lst[j]
#         if sum == m:
#             cnt += 1
#
# print(cnt)
# 투포인터 교수님이 푼 문제
# n,m 입력
# n개의 자연수 중 연속된 숫자들을 더했을 때 합이 m이 되는 경우는 몇가지 인가요? (투포인터-구간의크키가 정해지지X)
# 예시
# 10 5
# 1 2 3 4 2 5 3 1 1 2    => 3개
#
# 10 5
# 1 2 3 4 2 5 3 1 1 5   => 4개
#
# n,target=map(int,input().split())
# arr=list(map(int,input().split()))
# cnt,sum=0,0
# high,low=0,0
#
# while(1):
#     if sum>=target or high==n:  # 합이 타겟보다 크다면 (같은때도 범위를 좁혔음)
#         sum-=arr[low]
#         low+=1
#     elif sum<target:           # 합이 타겟보다 작으면 (범위 넓히기)
#         sum+=arr[high]
#         high+=1
#     if sum==target:
#         cnt+=1
#     if low==n:  break
# print(cnt)

# st= list()
# st.append(3)
# st.append(4)
# st.append(5)
# st.append(6)
# st.append(7)
# print(st)
# st.pop()
# print(st)

# queu

# from collections import deque
#
# q =deque()
# q.append(5)
# q.append(6)
# q.append(7)
# q.append(8)
# q.append(9)
# print(q)
# print([*q])
# # qeue --FIFO
# q.popleft()
# q.popleft()
# print([*q])

# BFS

#          A
#     B            C
# D       E             F

from collections import deque
# bfs  지금 내위치에서 갈수있는곳 다적어주기
# name =list(input().split())#A B C D E F
# arr = [[0,1,1,0,0,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,0,1],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# answer=[]# 탐색순서 저장 후 출력
#
# def bfs(st): # 0 출발점
#     global  answer
#     q =deque()
#     q.append(st)
#     while q:
#         now = q.popleft()
#         answer.append(name[now])
#
#         for i in range(6):
#             if arr[now][i] ==1:
#                 q.append(i)
#
# bfs(0)
# print(answer)



# bfs 연습
# name = ['A','B','C','D','E','F']
# arr = [[0,1,0,1,0,0],
#        [0,0,1,0,1,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,1],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# from collections import deque
#
# answer = []
# def abc(now):
#     global answer
#     que=deque()
#     que.append(now)
#     while que:
#         now = que.popleft()
#         answer.append(name[now])
#         for i in range(6):
#             if arr[now][i]==1:
#                 que.append(i)
# abc(0)
# print(answer)
#
# BFS
# tree 모형이 아닌 graph
# from collections import deque
# name = ['A','B','C','D']
# arr = [[0,1,1,0],
#        [0,0,0,1],
#        [0,1,0,1],
#        [0,0,0,0]]
# used = [0]*4
# answer = []
#
# def abc(now):
#     global answer
#     que =deque()
#     que.append(now)
#     while que:
#         now = que.popleft()
#         answer.append(name[now])
#         for i in range(4):
#             if used[i] ==0 and arr[now][i]==1:
#                 used[i]=1
#                 que.append(i)
# used[0]=1
# abc(0)
# print(answer)


# from collections import deque
n=int(input()) # 3
y,x=map(int,input().split())  # 1,1 민들레 꽃씨가 떨어지는 좌표 입력
arr=[[0]*n for _ in range(n)]  # 3*3 배열 선언

arr[y][x]=1
q=deque()
q.append([y,x])   # 시작 좌표값 넣기
while q:
    now=q.popleft()
    nowy,nowx=now[0],now[1]   # 현재의 좌표값
    directy=[-1,1,0,0]
    directx=[0,0,-1,1]
    for i in range(4):
        dy=nowy+directy[i]
        dx=nowx+directx[i]
        if 0<=dy<n and 0<=dx<n: # 배열의 범위를 벗어나지 않는다면
            if arr[dy][dx]==0:  # 꽃이 아직 피지 않은 곳이라면 (중복체크)
                arr[dy][dx]=arr[y][x]+1
                q.append([dy,dx])

for i in arr:
    print(*i)
#
#


























