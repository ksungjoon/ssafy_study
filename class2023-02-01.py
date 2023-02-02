# 알고리즘!------------------------

# 알고리즘 : 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다. 주로 컴퓨터용어로 쓰이며,
# 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.

# 요약: 어떠한 문제를 해결하기 위한 절차라고 볼 수 있다.

# APS과정의 목표 중 하나는 좋은 알고리즘을 이해하고 활용하는것

# 좋은 알고리즘
# 정확성 : 얼마나 정확하게 동작하는가
# 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
# 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
# 단순성 : 얼마나 단순한가
# 최적성 : 더 이상 개선할 여지없이 최적화되었는가

# 시간 복잡도
#       - 실제 걸리는 시간을 측정
#       - 실행되는 명령문의 개수를 계산
# 시간 복잡도 -- 빅-오(O) 표기법
# 빅오 표기법
# 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에대한 항만을 표시
# 계수는 생략하여 표시
# 예를 들어
#   -  O( 3n + 2) = O(3n) = O(n)
#   -  O(2n**2 + 10n + 100) = O(n**2)
#      O(4) = O(1)
# n개의 데이터를 입력 받아 저장한 후 각 데이터에 1씩 증가시킨 후 각 데이터를 화면에
# 출력하는 알고리즘의 시간복잡도는 어떻게 되나? - O(n)

# 배열이란 무엇인가
# 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

# 배열의 필요성
# -프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여
# 자료에 접근하는 것은 매우 비효율적일 수 있다.
# -배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언할 수 있다.
# -단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다.
'''
55 7 78 12 42
for i : N-1 -> 1  # 각 구간의끝
    for j : 0 -> i-1# 비교할 왼쪽 원소
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1] # 큰 원소 오른쪽으로
'''
# N = int(input())
# arr = list(map(int,input().split()))
# for i in range(N-1, 0, -1): # 각 구간의 끝
#     for j in range(i):       # 비교할 왼쪽 원소
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j] # 큰 원소 오른쪽으로
# print(arr)
# '''
# 3
# 5
# 55 7 78 12 42
# 6
# 55 7 78 100 42 1
# 7
# 55 7 48 57 92 14 3
# '''
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     maxV = arr[0]  # 첫 원소를 최대로 가정
#     for i in range(1,N): # 나머지 원소와 비교
#         if maxV < arr[i]:
#             maxV =arr[i]
#     print(f'#{tc} {maxV}')

# 시간복잡도 = 기본연산수행시간 + 입력되는 데이터를 종합적으로 고려
# 대략적인 계산
# 1. 최선 표기법
# 2. 최악 표기법 - ps 분야에서 채택 대략적인 계산 점근적 표기법이라고도 불림
# 3. 평균 표기법
# 표기 방법: 빅오표기법


# a= 3
# print(a)
# b=6
# t =input()
# for i in range(t):
#     print('#')
# #시간복잡도 O(n+3) = O(n)


# O(1) > O(logN) >O(N) > O(NlogN) >O(n**2)
#
# number= [7,10,22,4,3,17]
#
# # 합구하기
# sum = 0
#
# for i in number:
#     sum += i
#
# print(sum)
#
# # 최대값 구하기
#
# max = 0
#
# for i in number:
#     if max<i:
#         max = i
#
# print(max)
#
# # 최솟값 구하기
#
# min = number[0]
#
# for i in number:
#     if min > i:
#         min = i
#
# print(min)
#
# # 넘버 리스트 안에 가장 큰 값이 몇개 존재 하나요?
# # 1. 가장 큰값 찾기
# # 2. 가장 큰값이 몇개 있는지 알려주세요
#
# number = [7,10,22,4,3,17,22,6,4,22]
#
# max = 0
# count = 0
# for i in number:
#     if max < i:
#         max = i
# for j in number:
#     if max == j:
#         count += 1
#
# print(max,count)

# 디버깅
#
# number = [7,10,22,4,3,17,22,6,4,22]
#
# max = 0
# count = 0
# for i in number:
#     if max < i:
#         max = i
# for j in number:
#     if max == j:
#         count += 1
#
# print(max,count)

# ctrl + f8 (breakpoint 찍기)
# shift + f9 (디버깅 실행)
# f8 (하나씩 실행)
# f9 (다음 breakpoint로 이동)
# ctrl+ f2 (디버깅 종료)
# f7 (스텝인투 함수 안으로 진입)

# def abc(y,x):
#     z = y + x
#     z += 1
#     return z
#
# a = 10
# b = 20
# print(b)
# c = 30
# a = 1000
# print(a)
# a = 100
# ret = abc(3,7)
# d = 40
# a = 10
# print(ret)
#-----------------------------------------------------------------------------------------------------------
# sort(정렬)
# 선택정렬 selection sort
# 삽입정렬 insert sort
# 버블벙렬 bubble sort
# 계수정렬 count sort
# 퀵 정렬 quick sott
# 합병정렬 merge sort
# 힙 정렬 heap sort

# 선택 정렬

# 4,7,1,8,2 > 1,7,4,8,2>1,4,7,8,2>1,2,7,8,4>1,2,4,8,7>1,2,4,7,8

lst = [4,7,1,8,2]

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j] = lst[j],lst[i]
print(lst)

# 시간 복잡도 O(n**2)
# 장점: 구현하기 쉽다. 단점: 오래걸린다.

# 삽입정렬

# 4>4,7>4,7,3>4,3,7>3,4,7>3,4,7,1>3,4,1,7>3,1,4,7>1,3,4,7>1,3,4,7,2>1,3,4,2,7>1,3,2,4,7>1,2,3,4,7

lst = [4,7,3,1,2]
arr = []
for i in range(len(lst)):
    arr.append(lst[i])
    for j in range(i,0,-1):
        if arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
        else:
            break
print(arr)

# 시간 복잡도 O(n**2)
# 장점: 이미 정렬되어있는 데이터에서 새로운 값을 정렬 할때 좋음 단점: 오래걸린다.

# 버블정렬

# 1회차{3,8,12,10,1>3,8,12,10,1>3,8,10,12,1>3,8,10,1,12}   >   2회차{3,8,10,1,12>3,8,10,1,12>3,8,1,10,12}  >     3회차{3,8,1,10,12>3,1,8,10,12}   >   4회차{1,3,8,10,12}

lst = [3,8,1,10,12]

for i in range(len(lst)-1):
    for j in range(len(lst)-1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(lst)

# 시간 복잡도 O(n**2)
# 장점: 쉽다 단점: 시간이 오래걸린다
#--------------------------------------------------------------------------------------------
# 정수 n 입력받고
# n개의 정수를 리스트에 입력받은 후
# 입력받은 정수가 b배열에 각각 몇개 있는지 출력해 주세요

# a = [3,8,5,2,5,7,2,4]
# b = [1,2,3,4]
# count = 0
# for i in b:
#     for j in a:
#         if j == i:
#             count += 1
#     print(f'{i}: {count}개')
#     count = 0
# direct address table
# 1중 포문

# bucket = [0]*10
# for i in range(len(a)-1):
#     bucket[a[i]]+=1
# for i in b:
#     print(f'{i}: {bucket[i]}개')
# print()
# for i in range(len(bucket)):
#     if bucket[i]>0:
#         print(f'{i}: {bucket[i]}개')
#

# n 개의 정수를 리스트에 입력받은 후
# 어떤 숫자가 각각 몇개씩 입력 되었는지 출력해보세요

# n = list(map(int,input().split()))
# bucket = [0]*10
# for i in range(len(n)):
#     bucket[n[i]] += 1
# for i in range(len(bucket)):
#     if bucket[i] > 0:
#          print(f'{i}: {bucket[i]}개')
#-------------------------------------
# 계수정렬

# DAT등록 -> 누적합 -> 값넣기

lst = [4,7,1,3,7,5,1]
bucket = [0] * 10
arr = [0]*7
# DAT등록
for i in range(len(lst)):
    bucket[lst[i]] += 1
# 누적합 넣기
for j in range(len(bucket)-1):
    bucket[j+1] = bucket[j]+bucket[j+1]
print(bucket)
# 값넣기
for k in lst:
    arr[bucket[k]-1]= k
    bucket[k]=bucket[k]-1
print(arr)
# 시간 복잡도 O(n)
# 장점 : 빠르다.
# 단점 : -정수나 정수로 표현할 수 있는 자료에 대해서만 적용가능:각 항목의 발생회수를
# 기록하기 위해 , 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
# -카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
