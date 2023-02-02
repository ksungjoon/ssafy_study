# 카운팅 정렬
# 항목들의 순서를 결정하기 위해 집합에 각 항복이 몇 개씩 있는지 세는 작업을 하여 선형 시간에 정렬하는 효율적인 알고리즘
#-------------------
# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 대 ,3장의 카드가 연속적인
# 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고한다.
# 그리고 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다
# 6자리의 숫자를 입력받아 baby-gin 여부를 판단하는 프로그램을 작성하라

# 단수하게 순열을 생성하는 방법
# 예) {1,2,3}을 포함하는 모든 순열을 생성하는 함수
# i1 = (1,2,3)
# i2 = (1,2,3)
# i3 = (1,2,3)
#
# for i1 in range(1,4):
#     for i2 in range(1,4):
#         if i2 != i1:
#             for i3 in range(1,4):
#                 if i3 != i1 and i3 != i2 :
#                     print(i1,i2,i3)
#-------------------------------------------------------------------
# 탐욕 알고리즘 (greedy)
# 탐용 알고리즘은 최적해를 구하는데 사용되는 근시안적인 방법
# 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을
# 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.
# 각 선택의 시점에서 이루어지는 결정은 지역적즈올 최적이지만,
# 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여 그것이 최적이라는 보장은 없다
# 일반적으로 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy접근이 된다

# changes = int(input()) # 거슬러 줄돈
# coin = [500,100,50,10]
# answer =0 # 정답(사용하는 동전 개수)
# index =0 # 0 = 500원 1 =100원
# while 1:
#     cnt= changes//coin[index]   # index가 0일때 500짜리 동전 개수를 cnt에 넣기
#     changes-=(cnt*coin[index])  # 거슬러 준 만큼 changes에서 빼고
#     answer+=cnt          # 동전 사용한 만큼 정답에 더해주고
#     index+=1              # 500 다음에 100짜리 사용
#     if index ==4:          # 10원짜리 까지 다 사용 했으면 break
#         break
# print(answer) # 정답 출력

# ------------------------------------------------------------------

# 연속되는 네모 세칸의 합이 가장 클 때 의 값은?
lst= [[4, 5, 2, 6, 7, 3, 1],
      [2, 9, 9, 6, 1, 6, 7]]
max = 0
a = 0
n = 3
for i in range(2):
    for j in range(8-n):
        for k in range(n):
            a += lst[i][j+k]
        if max < a:
            max = a
        a = 0
print(max)

#------------------------------------------
Max =-21e8

def getsum(a,b):
    sum =0
    for i in range(3):
        sum+=lst[a][b+i]            # 전달받은 좌표값부터 3곳의 합을 구한후
    return sum               # 구한 합을 반환하기

for i in range(2):
    for j in range(5):
        ret =getsum(i,j)             # getsum 핫무에 좌표값 전달(0,0~1,4)
        if ret>Max:                 # 반환 되는 값 중 max값 갱신하기
            Max =ret
print(Max)

#------------------------------------------
# 리스트에 숫자 4개 입력을 받은 후
# 입력받은 숫자라 lst안에 존재하면 Y를 출려
# lst 안에 존재하지 않으면 N을 출력해 주세요
# 내가 풀다가 실패한거
# lst= [[4, 5, 2, 6, 7],
#       [2, 9, 9, 6, 1],
#       [2, 9, 9, 6, 1]]
# a,b = map(int,input().split())
# c,d = map(int,input().split())
#
# new_lst = [a,b,c,d]
# for i in range(3):
#     for j in range(5):
#         for k in range(4):
#             if lst[i][j] == new_lst[k]:
#                 new_lst[k] = 'Y'
#                 break
#             else:
#                 new_lst[k] = 'N'
# print(new_lst)
#---------------------------------------------------
# lst= [[4, 5, 2, 6, 7],
#       [2, 9, 9, 6, 1],
#       [2, 9, 9, 6, 1]]
#
# arr=[list(map(int,input().split())) for _ in range(2)]
#
# def findnum(value):
#       for i in range(3):
#             for j in range(5):
#                   if lst[i][j]==value:
#                         return 1
#       return 0
#
# for i in range(2):
#       for j in range(2):
#             ret=findnum(arr[i][j])
#             if ret:
#                   print('Y',end=' ')
#             else:
#                   print('N',end=' ')
#       print()
#----------------------------
# 정수 4개 입력받고
# 패턴 존재 여부 출력하기
# 1 1 2 1
# 없음
# 5 8 5 3
# 존재함
# arr=[3,6,5,8,5,3,5,8,5,3,3,1,1,3]
# lst = list(map(int,input().split()))
# new_lst =[]
# for i in range(len(arr)-3):
#     new_lst.append([arr[i],arr[i+1],arr[i+2],arr[i+3]])
# if lst in new_lst:
#     print('존재함')
# else:
#     print('없음')

#---------------------------------

# arr=[3,6,5,8,5,3,5,8,5,3,3,1,1,3]
# pattern=list(map(int,input().split()))
#
# alen=len(arr) # 14개
#
# def isPattern(index): # 0 1 2 ... 10
#     for i in range(4):
#         if arr[index+i]!=pattern[i]:
#             return 0
#     return 1
#
# flag=0
# for i in range(alen-4+1):
#     ret=isPattern(i)
#     if ret==1:
#         flag=1
#         break;
# if flag:
#     print("존재")
# else:
#     print('없음')
#-----------------------------------------------------------
# 이차원 배열에 패턴이 몇개 존재 하는지 출력하기
#
# AB
# TT
# 발견2개

# board = [
#     ['A','B','G','K'],
#     ['T','T','A','B'],
#     ['A','C','T','T']]
# lst = list(input())
# lst2 = list(input())
# new_lst =[]
# def Count(lst,lst2):
#     count = 0
#     for i in range(3):
#         for j in range(3):
#             new_lst.append([board[i][j],board[i][j+1]])
#     for i in new_lst:
#         if i == lst or i == lst2:
#             count += 1
#     if count ==4:
#         print('발견2개')
#     else:
#         print('미발견')
#
# Count(lst,lst2)

#@@@@@@@@@@@@@문제 잘못 이해 틀림
#-------------------------------------------------------------
board = [
    ['A','B','G','K'],
    ['T','T','A','B'],
    ['A','C','T','T']]
ptn =[list(input())for i in range(2)]

def findptn(by,bx):
    for dy in range(2):
        for dx in range(2):
            if board[by+dy][bx+dx]!=ptn[dy][dx]:
                return 0
    return 1

cnt = 0
for i in range(2):
    for j in range(3):
        if findptn(i,j):
            cnt+=1
if cnt:
    print(f'발견{cnt}개')
else:
    print('미발견')
#----------------------------------------------------------------