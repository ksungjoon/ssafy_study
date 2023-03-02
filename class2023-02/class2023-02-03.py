# sw 역량테스트
# 입력 TC를 처리하여 정확한 출력을 내보내는 것
# 빠르게 읽기 (조약/제약 체크) ->  Tc손풀기 'cpu방법' -> 50% 시간 지나고 안되면 다시 정독

# 문제 풀이-----------------------------

# 6485.

# import sys
# sys.stdin = open('input.txt','r')
T = int(input())
for test_case in range(1, T +1):
    N = int(input())

    cnts =[0]*5001
    for _ in range(N):
        S,E = map(int,input().split())
        for i in range(S, E+1):
            cnts[i] += 1
    P = int(input())
    alst = []
    for _ in range(P):
        p = int(input())
        alst .append(cnts[p])
    print(f'#{test_case}',*alst)
#-----------------------------------------
# 1945 간단한 소인수 분해
# divs = [2,3,5,7,11]
# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     cnts = [0]*len(divs)
#
#     for i in range(len(divs)):
#         while N% divs[i] == 0:
#             cnts[i] +=1
#             N = N//divs[i]
#
#     print(f'#{test_case}',*cnts)
#---------------------------

# T = int(input())
# for test_case in range(1,T+1):
#     N = int(input())
#     lst = list(map(int,input()))
#     ans = cnt = 0
#     for i in range(N):
#         if lst[i]==0:
#             cnt = 0
#         else:
#             cnt+=1
#             if ans<cnt:
#                 ans =cnt
#     print(f'#{test_case}',ans)
# -----------------------------------------
# 입력받은 두개의 인덱스 범위 내에서 1차원 문자 배열을 회전 시켜주세요
# 내가 푼거
# import copy
# lst = ['T','B','T','S','A','K','L','I','Z','C']
# lst2 = copy.deepcopy(lst)
# a,b = map(int,input().split())
# for i in range(a,b+1):
#     if i+2>b:
#         lst2[i+2-b] = lst[i]
#     else:
#         lst2[i+2] = lst[i]
# print(*lst2)
#
# 교수님이 푼거

# arr=['T','B','T','S','A','K','L','I','Z','C']
# index=list(map(int,input().split()))

# def LMove(st,ed):
#     temp=arr[st]
#     for i in range(st,ed,1):
#         arr[i]=arr[i+1]
#     arr[ed]=temp
#
# def RMove(st,ed):
#     temp=arr[ed]
#     for i in range(ed,st,-1):
#         arr[i]=arr[i-1]
#     arr[st]=temp
#
# for i in range (2):
#     RMove(index[0],index[1])
#
# print(*arr)

#--------------------------------------
# 시험힌트
# 코드 나오고 코드의 실행 결과값은?
# 재귀 피보나치 코드분석
# 리스트 관련 메서드
# 조건표현식
# 인스턴스메서드
# super
# 형변환
# 함수가변인자
# 함수 실행순서
# 깊은 복사 얕은복사
# and or 논리연산자