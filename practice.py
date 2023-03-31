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



N = int(input())
lst = [list(map(int,input().split()))for i in range(N)]
counts_ru = []
counts_rd = []
for i in range(N):
    for j in range(N):
        if lst[i][j]==1:
            counts_ru.append(i+j)
            counts_rd.append(i-j)
for i in range(N):
    for j in range(N):

