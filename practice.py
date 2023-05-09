# N,M = map(int,input().split())
# lst = [i for i in range(1,N+1)]
# path = [0]*M
#
# def dfs(lev,start):
#     if lev==M:
#         print(*path,sep=' ')
#         return
#     for i in range(start,N):
#         path[lev]= lst[i]
#         dfs(lev+1,i)
#         path[lev] = 0
#
# dfs(0,0)
# name ='tkab'
# cnt = 0
# path=['']*3
#
# def abc(lev,start):
#     global cnt
#     if lev ==3:
#         for i in range(3):
#             print(path[i],end='')
#         print()
#         cnt+=1
#         return
#     for i in range(start,4):
#         path[lev]=name[i]
#         abc(lev+1,i)  # +1 만 지운거
#         path[lev]=0
# abc(0,0) # lev start
# print(cnt)
#
lst = [list(map(int,input().split()))for i in range(9)]
exp=[1,2,3,4,5,6,7,8,9]
empty = [(i,j) for i in range(9) for j in range(9) if lst[i][j]==0]

def result(lst):
    possible = [i for i in exp if i not in lst]
    return possible
def result2(x):
    if 0<=x<=2:
        return [0,1,2]
    elif 3<=x<=5:
        return [3,4,5]
    elif 6<=x<=8:
        return [6,7,8]
def is_possible(y,x):
    possible = result(lst[y])
    sero = [lst[k][x] for k in range(9)]
    possible2 = result(sero)
    possible = [i for i in possible if i in possible2]
    s_sero = result2(y)
    s_garo = result2(x)
    s_box = [lst[k][z] for z in s_garo for k in s_sero]
    possible3 = result(s_box)
    possible = [i for i in possible if i in possible3]
    return possible
flag=0

def dfs(z):
    global flag
    if flag==1:
        return
    if z == len(empty):
        for i in range(9):
            print(*lst[i])
        flag=1
        return
    for k in is_possible(empty[z][0],empty[z][1]):
        lst[empty[z][0]][empty[z][1]]=k
        dfs(z+1)
        lst[empty[z][0]][empty[z][1]] = 0

dfs(0)
































# def result(lst):
#     lst1 = [i for i in exp if i not in lst]
#     return lst1
# def result2(x):
#     if 0<=x<=2:
#         return [0,1,2]
#     elif 3<=x<=5:
#         return [3,4,5]
#     elif 6<=x<=8:
#         return [6,7,8]
# flag = 1
#
# while(flag):
#     for i in range(9):
#         for j in range(9):
#             if lst[i][j]==0:
#                 collect=result(lst[i])
#                 if len(collect)==1:
#                     lst[i][j]=collect[0]
#                     continue
#                 sero=[lst[k][j] for k in range(9)]
#                 collect2 = result(sero)
#                 if len(collect2)==1:
#                     lst[i][j]=collect2[0]
#                     continue
#                 collect3 = [l for l in collect if l in collect2]
#                 if len(collect3)==1:
#                     lst[i][j]=collect3[0]
#                     continue
#                 sero2 = result2(i)
#                 garo = result2(j)
#                 lst2=[lst[x][y] for x in sero2 for y in garo]
#                 collect4 = result(lst2)
#                 if len(collect4)==1:
#                     lst[i][j]=collect4[0]
#                 collect5 = [l for l in collect3 if l in collect4]
#                 if len(collect3)==1:
#                     lst[i][j]=collect5[0]
#                     continue
#     for o in range(9):
#         if 0 not in lst[o]:
#             flag=0
#
# for i in range(9):
#     print(*lst[i])



















