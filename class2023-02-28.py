# DFS
# 코_테
# mincoding - 42,42.5
# programers - lev2 dfs, lev3 dfs
# A 형을 봐야한다
# swea
# 신한 ict 코테
# 백준 골드 1,2 정도


# dfs 연습
# a  b c   d e  f g
# 49 6 54 80 3 18 70전투력
# 전투력 차이의 최소값?
# 이진트리 형태 내가푼거
# lst = [49,6,54,80,3,18,71]
# lst_sum = sum(lst)
# ateam=0
# bteam = lst_sum-ateam
# bteam_lst = []
# check = [1,0]
# ateam_lst = []
# min = 21e9
# def abc(lev):
#     global ateam,lst_sum
#     if lev == 7:
#         ateam_lst.append(ateam)
#         bteam_lst.append(lst_sum-ateam)
#         return
#     for i in range(2):
#         ateam +=lst[lev]*check[i]
#         abc(lev+1)
#         ateam -= lst[lev] * check[i]
# abc(0)
# print(ateam_lst)
# print(bteam_lst)
#
# for i in range(len(ateam_lst)):
#     if min> abs(ateam_lst[i]-bteam_lst[i]):
#         min = abs(ateam_lst[i]-bteam_lst[i])
# print(min)

# 조합
# lst = [49,6,54,80,3,18,71]
# Min = int(21e8)
# check = [0]*7
#
# def dfs(start,level,sum):
#     global Min
#     against = 0
#     for i in range(7):
#         if check[i]==0:
#             against+=lst[i]
#     gap =abs(sum-against)
#     Min = min(Min,gap)
#     if level == 6:
#         return
#     for i in range(start,7):
#         check[i]=1
#         dfs(i+1,level+1,sum+lst[i])
#         check[i]=0
#
# dfs(0,0,0)
# print(Min)

#  중복순열 ,순열 ,조합, 중복조합 연습해보기


# 미로 찾기 연습 dfs
# directy=[-1,0,0,1]
# directx=[0,-1,1,0]
# arr = [[0,0,0,0],[1,0,1,0],[1,0,1,0],[0,0,0,0]]
# cnt = 0
# def dfs (a,b):
#     global cnt
#     if a==3 and b==3:
#         cnt +=1
#         return
#     for i in range(4):
#         dy = directy[i]+a
#         dx = directx[i]+b
#         if 0<=dy<4 and 0<=dx<4:
#             if arr[dy][dx]==0:
#                 arr[dy][dx]=1
#                 dfs(dy,dx)
#                 arr[dy][dx] = 0
#
# arr[0][0]=1
# dfs(0,0)
# if cnt!=0:
#     print('가능')
# else:
#     print('불가능')
# print(cnt)

# dfs 마지막 문제
#
# 3*3 배열에 땅을 총 3번 팠을때
# 모든 땅의 가치 합의 MAx 값 출력하기 (중복 땅파기 가능함)

import copy
arr=[[3,2,7],[4,5,1],[7,2,8]]
Max=-21e8


def digging(y,x):           # 땅을 파는 함수
    directy=[0,-1,1,0,0]
    directx=[0,0,0,-1,1]
    for i in range(5):
        dy=directy[i]+y
        dx=directx[i]+x
        if dy<0 or dx<0 or dy>2 or dx>2: continue
        arr[dy][dx]=(arr[dy][dx]*7)%10


def getsum():       # 배열의 합을 구한후 리턴
    sum=0
    for i in range(3):
        for j in range(3):
            sum+=arr[i][j]
    return sum

def dfs(level):
    global Max,arr
    backup=copy.deepcopy(arr)    #원상복구를 위해 미리 arr배열을 backup에 카피 해 놓기!!

    if level==3:                # 바닥에 왔을떄
        result=getsum()         # 배열합 구하고
        Max=max(Max,result)     # Max 값 갱신
        return

    for i in range(3):
        for j in range(3):
            digging(i,j)        # 땅파고
            dfs(level+1)        # dfs 깊이로 들어가고
            arr=copy.deepcopy(backup)   # 다녀와서는 원상복구 ************************** 핵심

dfs(0)          # dfs level = 0
print(Max)