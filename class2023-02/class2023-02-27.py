# n =int(input())
# lst= [1,2,3,4]
# cnt = 0
# sum = 0
# def abc(lev):
#     global cnt,sum
#     if lev == n:
#         if sum == 10:
#             cnt +=1
#         return
#     for i in range(4):
#         sum += lst[i]
#         abc(lev+1)
#         sum -= lst[i]
# abc(0)
# print(cnt)
# 중복 순열
# ex ) 주사위
# 모든 경우를 출력
# 순열 #used사용
# 한번 뽑았던 숫자는 뽑지않는것
# ex) 123,124,132, 134,142,143
# 조합
#ex)123, 124 ,134, 234
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
#         abc(lev+1,i+1)
#         path[lev]=0
# abc(0,0) # lev start
# print(cnt)

# 중복조합
# ex) 111, 112, 113, 122
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

# A,B,C,D
# 부분집합
# 이진으로 활용
# check =[1,0]
# lst = ['A','B','C','D']
# path =['']*4
# def abc(lev):
#     if lev==4:
#         for i in range(4):
#             if path[i]==1:
#                 print(lst[i],end='')
#         print()
#         return
#     for i in range(2):
#         path[lev]=check[i]
#         abc(lev+1)
# abc(0)
# 조합을 활용하는 경우
# A = 'ABCD'
#
# cnt = 0
# n = int(input())
#
# def abc(level,idx=0,S=''):
#     global cnt
#     print(S)
#     cnt+=1
#
#     if level==n:
#         return
#
#     for i in range(4):
#         if i>=idx:
#             abc(level+1,i+1,S+A[i])
# abc(0)
# print(cnt)


# 한라인내에서 중복뽑기 금지


result = 21e9
line1 = [-2,3,4,9,-5,2]
line2 = [4,7,-3,-6,-1,2]
used1 = [0]*6
used2 = [0]*6
def abc(lev,sum):
    global result
    if lev == 12:
        if abs(result)>abs(sum):
            result = sum
        return
    for i in range(6):
        if lev%2==0:
            if used1[i]==0:
                used1[i]=1
                abc(lev+1,sum+line1[i]*(lev+1))
                used1[i]=0
        else:
            if used2[i]==0:
                used2[i]=1
                abc(lev+1,sum+line2[i]*(lev+1))
                used2[i]=0

abc(0,0)
print(result)

#  교수님이 푼거
# line1=[-2,3,4,9,-5,2]
# line2=[4,7,-3,-6,-1,2]
# used1=[0]*6
# used2=[0]*6
# Min=int(21e8)
# answer=0
# def dfs(level,sum):
#     global Min,answer
#     if level==12:
#         # 0에 가장 가까운 sum을 알아보기
#         if Min>abs(sum):
#             Min=abs(sum)
#             answer=sum
#         return
#     if level%2==0:
#         for i in range(6):
#             if used1[i]==1: continue
#             used1[i]=1
#             dfs(level+1,sum+(line1[i]*(level+1)))
#             used1[i]=0
#     else:
#         for i in range(6):
#             if used2[i]==1: continue
#             used2[i]=1
#             dfs(level+1,sum+(line2[i]*(level+1)))
#             used2[i]=0
#
# dfs(0,0) # level sum
# print(answer)