# T = int(input())
# for test_case in range(1,T+1):
#     N,M = map(int,input().split())
#     lst = [list(map(int,input().split()))for i in range(N)]
#     diry = [-1,0,0,1]
#     dirx = [0,-1,1,0]
#     Max = -21e9
#     def cost(k):
#         a = k*k+(k-1)*(k-1)
#         return a
#     def dfs(a,b,cnt):
#         if cnt>=N:
#             return
A,B = map(int,input().split)
print(A*B)