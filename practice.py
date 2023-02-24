N,K = map(int,input().split())
lst = [list(map(int,input().split()))for i in range(N)]





















# N,K=map(int,input().split())
# lst = list(map(int,input().split()))
# arr = [[0]*101 for i in range(101)]
# path = []
# used = [0]*101
# result_lst =[]
# result = [K]
# for i in range(N):
#     if i%2==0:
#         arr[lst[i]][lst[i+1]]=1
#
# from collections import deque
# def abc(start):
#     global path,result
#     que = deque()
#     que.append(start)
#     while que:
#         result_lst.append(result)
#         result = []
#         now =que.popleft()
#         path.append(now)
#         for i in range(101):
#             if used[i]==0 and arr[now][i]==1:
#                 used[i]=1
#                 result.append(i)
#                 que.append(i)
#
# used[K]=1
# abc(K)
# print(result_lst)
#
#
# def bfs(s):
#     # [0] q, v, 필요한 flag 생성
#     q = []
#     v = [0] * 101
#     ans = s
#
#     # [1] q에 초기데이터(들) 삽입, v표시
#     q.append(s)
#     v[s] = 1
#
#     while q:
#         c = q.pop(0)  # [2] q에서 한개 꺼냄 + 필요시 정답처리
#         if v[ans] < v[c] or v[ans] == v[c] and ans < c:
#             ans = c
#
#         # [3] 4/8 연결방향 등 반복처리
#         for n in adj[c]:
#             if v[n] == 0:
#                 q.append(n)
#                 v[n] = v[c] + 1
#     return ans
#
#
# T = 10
# for test_case in range(1, T + 1):
#     N, S = map(int, input().split())
#     lst = list(map(int, input().split()))
#     # [1] 인접리스트에 연결 저장
#     adj = [[] for _ in range(101)]
#     for i in range(0, len(lst), 2):
#         s, e = lst[i], lst[i + 1]
#         adj[s].append(e)
#
#     ans = bfs(S)
#     print(f'#{test_case} {ans}')
#
#
