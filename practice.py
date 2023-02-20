# 알고리즘 스터디
# N = int(input())
# lst = [list(map(int,input().split()))for i in range(N)]
# stack= [[1,2,3,4,5,6]for i in range(N)]
# result = 0
# result_stack = []
# def abc(lev,x):
#     global result
#     if lev == N:
#         return
#     for i in range(6):
#         if lst[lev][i]==x:
#             if i == 0:
#                 z = 5
#             if i == 1:
#                 z = 3
#             if i == 2:
#                 z = 4
#             if i == 3:
#                 z = 1
#             if i == 4:
#                 z = 2
#             if i == 5:
#                 z = 0
#     stack[lev].remove(x)
#     stack[lev].remove(lst[lev][z])
#     abc(lev+1,lst[lev][z])
# abc(0,5)
# for i in range(N):
#     result+=max(stack[i])
# print(result)


T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    lst = [list(map(int,input()))for i in range(n)]
    result = 0
    diry=[-1,0,0,1]
    dirx = [0,-1,1,0]
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 2:
                starty = i
                startx = j
                lst[i][j] = 0
            if lst[i][j] ==3:
                endy=i
                endx=j
                lst[i][j]=0
    def abc(y,x):
        global result
        if y==endy and x==endx:
            result = 1
            return
        for i in range(4):
            dx=dirx[i]+x
            dy=diry[i]+y
            if 0 <= dy <n and 0 <= dx <n:
                if lst[dy][dx]==0 :
                    lst[dy][dx] = 1
                    abc(dy,dx)
                    lst[dy][dx] = 0
                    if result == 1:
                        return


    abc(starty,startx)
    print(f'#{test_case} {result}')
