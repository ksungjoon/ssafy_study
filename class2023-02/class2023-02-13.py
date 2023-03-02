# 주사위 N개로 나올수 있는 모든 경우의 수
# lst = [1,2,3,4,5,6]
# n =int(input())
# path = [0]*n
# def abc(lev):
#     if lev==n:
#         print(*path,sep='')
#         return
#     for i in range(6):
#         path[lev] = lst[i]
#         abc(lev+1)
# abc(0)
# 주사위 N개로 나올수 있는 모든 경우의 수
# 중복 x 순열
# n=3
# dice=[1,2,3,4]
# path=['']*n
# used=[0]*4
# def abc(level):
#      if level==n:
#           for i in range(n):
#                print(path[i],end=' ')
#           print()
#           return
#      for i in range(4):
#          if used[i]==1: continue  #
#          path[level]=dice[i]
#          used[i]=1               #
#          abc(level+1)
#          #path[level] =' '
#          used[i]=0               #
#
# abc(0)

# 1번째 2나오는거 제거 다음 가지에 진입을 안하는 경우
# n = 3
# dice = [1,2,3,4]
# path = ['']*n
# used = [0,1,0,0]
# def abc(lev):
#     if lev ==n:
#         for i in range(3):
#             print(path[i],end='')
#         print()
#         return
#     for i in range(4):
#         if lev==0 and dice[i]==2: continue
#         path[lev]=dice[i]
#         abc(lev+1)
#
# abc(0)


# 일단 다음가지 진입 후 return하기 (back)하기
# n = 3
# dice = [1,2,3,4]
# path = ['']*n
# used = [0,1,0,0]
# def abc(lev):
#     if path[0]==2:
#         return
#     if lev ==n:
#         for i in range(3):
#             print(path[i],end='')
#         print()
#         return
#     for i in range(4):
#         path[lev]=dice[i]
#         abc(lev+1)
#
# abc(0)

# ABCD가 적혀있는 카드 3묶음이 있습니다.
# 각 묶음에서 카드를 1장씩 뽑았을 때
# C로 시작하는 경우는 다 제외하기

# n=3
# lst = ['A','B','C']
# path = ['']*n
# def abc(lev):
#     if path[0]=='C':
#         return
#     if lev == 3:
#         print(*path,sep='')
#         return
#     for i in range(3):
#         path[lev]=lst[i]
#         abc(lev+1)
# abc(0)

# B는 다빼기
# 아예진입을 안하는경우
# n=3
# lst = ['A','B','C']
# path = ['']*n
# def abc(lev):
#     if lev == 3:
#         print(*path,sep='')
#         return
#     for i in range(3):
#         if i ==1:
#             continue
#         path[lev]=lst[i]
#         abc(lev+1)
# abc(0)
# 진입 하고 return하는 경우
# n=3
# lst = ['A','B','C']
# path = ['']*n
# def abc(lev):
#     # if  'B' in path:   1번째 방법
#     #     return
#
#     # if lev>0 and path[lev-1]=='B':return   2번째 방법
#
#
#     if lev == 3:
#         print(*path,sep='')
#         return
#     for i in range(3):
#         path[lev]=lst[i]
#         abc(lev+1)
# abc(0)

# ABCD가 적혀있는 카드 3묶음이 있습니다
# 각 묶음에서 카드 1장씩 뽑았을때
# 연속해서 같은 카드를 뽑으면 안된다.
# n = 3
# lst = ['A', 'B', 'C','D']
# path = [''] * n

# 진입하고 return하는 경우
# def abc(lev):
#     if lev > 1 and path[lev-1]==path[lev-2]:return
#     if lev == 3:
#         print(*path, sep='')
#         return
#     for i in range(4):
#         path[lev] = lst[i]
#         abc(lev + 1)
#
# #
# abc(0)
# 진입을 아예안하는 경우
# def abc(lev):
#     if lev == 3:
#         print(*path,sep='')
#         return
#     for i in range(4):
#         if lev>0 and(path[lev-1]==lst[i]):continue
#         path[lev]=lst[i]
#         abc(lev +1)
# abc(0)

# 조합
# path배열을 활용하여 조합 구현
# candidates=['A','B','C','D']
# path=['']*10
#
# def abc(level):
#
#     if level==3:
#         for i in range(level):00
#             print(path[i],end=' ')
#         print()
#         return
#     for i in range(4):
#         #path[level - 1] # 그전에 들어온 곳
#         #candidates[i] # 앞으로 들어갈 곳
#         if level>0 and path[level-1] >= candidates[i]: continue #앞으로 들어갈 곳이 그전보다 커야함
#         path[level]=candidates[i]
#         abc(level+1)
# abc(0)
# #
# # for문을 시작하는 i를 바꿔서 조합 구현

# candidates=['A','B','C','D']
# path=['']*10
#
# def abc(level,start):
#
#     if level==3:
#         for i in range(level):
#             print(path[i],end=' ')
#         print()
#         return
#     for i in range(start,4):
#         path[level]=candidates[i]
#         abc(level+1,i+1)
# abc(0,0)  # level start(for문 시작점)

# DFS(깊이 우선 탐색)
# BFS(너비 우선 탐색)

#tree
# people = ['A','B','D','C','E','F']
# 1. 인접 행렬(이차 배열)
  #     A B D C E F
# arr = [[0,1,0,1,0,0], #A                            A
#        [0,0,1,0,0,0], #B                          B    C
#        [0,0,0,0,0,0], #D                        D     E F
#        [0,0,0,0,1,1], #C
#        [0,0,0,0,0,0], #E
#        [0,0,0,0,0,0]] #F
# 2. 인접 리스트
# lst = [[]for i in range(6)]
# lst[0].append('B')     # A -B -C
# lst[0].append('C')     # B -D
# lst[1].append('D')     # D
# lst[3].append('E')     # C -E -F
# lst[0].append('F')     # E
#                        # F

# 3. 리스트 (일차원 배열 - 이진트리)
# [_,A,B,C,D,_,E,F]


#나는솔로
# people = ['Amy','Bob','Chloe','Diane','Edger']
#
# arr = [[0,0,1,0,1],
#        [1,0,0,0,0],
#        [0,1,0,0,0],
#        [0,1,0,0,0],
#        [0,0,0,1,0]]
#
# # 여기서  가장 인기가 많은 사람은 누구인지 출력
# maxV=0
# for j in range(5):
#     sum = 0
#     for i in range(5):
#         if arr[i][j] == 1:
#             sum += 1
#     if maxV < sum:
#         maxV = sum
#         pp = people[j]
# print(pp)



#문자를 하나 입력받아 주세요
# 그리고 입력받은 문자의 형제노드를 출력해 주세요
# people =['A','B','C','D','E','F']
# arr = [[0,1,1,0,0,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,0,1],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# num = 0
# st = input()
# for i in range(len(people)):
#     if st == people[i]:
#         num =i
# parent = -1
# result = []
# for i in range(6):
#     if arr[i][num] == 1:
#         parent = i
# for j in range(6):
#     if arr[parent][j]==1 and j != num :
#         result.append(j)
# if parent == -1:
#     print('형제 없음')
# elif result==[]:
#     print('형제 없음')
# else:
#     for i in result:
#         print(people[i],end=' ')
#
