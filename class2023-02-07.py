# 순차 검색
# 일렬로 되어 있는 자료를 순서대로 검색하는 방법
# 가장 간단하고 직관적인 검색 방법
# 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
# 알고리즘이 단순하여 구현이 쉽지만 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임

# 2가지 경우
# 정렬되어 있지 않은 경우
# 정렬되어 있는 경우

# 검색과정
# 첫 번재 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
# 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
# 자료구조의 마지막에 이를 때가지 검색 대상을 찾지 못하면 검색 실패

# 정렬되어 있지 않은 경우
# 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
# 첫 번째 원소를 찾을 때는 1번 비교, 두 번째 원소를 찾을 때는 2번 빅
# 시간 복잡도 = O(N)

# 정렬되어 있는 경우
# 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어든다
# 시간복잡도 :O(N)

# 이진 검색
# 자료의 가운데에 있는 항복의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
# 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

# 선택 정렬
# a = [7,2,5,3,4,6,4]
# N = 7
# for i in range(N-1): # 작업 구간의 시작인덱스
#     minIndx = i         # 맨 앞이 최소라 가정
#     for j in range(i+1,N):
#         if a[minIndx] > a[j]:
#             minIndx = j
#     a[minIndx],a[i] = a[i] ,a[minIndx]
# print(a)

#---------------------------------------------------------------
# 교수님 설명
# 이진법
# arr = [1,3,4,6,8,11,13,15]
# target = int(input())
#
#
# def bs(st,ed,target):
#     while 1 :
#         mid = (st+ed)//2
#         if arr[mid] == target:
#             return 1
#         elif arr[mid] > target:
#             ed = mid-1
#         elif arr[mid] < target:
#             st = mid+1
#         if ed<st:
#             return 0
#
# answer =bs(0,len(arr)-1,target)
# if answer: print('찾았음')
# else: print('없음')
#
# 시간복잡도 :O(logN)




# 배터리가 몇 % 충전되어 있는지 O(logN)으로 검색
# bettery='******____'
# def per(st,ed):
#     max = -1
#     while True:
#         result = (st+ed)//2
#         if bettery[result] == '_':
#             ed = result-1
#         elif bettery[result] == '*':
#             max = result
#             st = result +1
#         if ed<st:
#             break
#     return max+1
# answer = per(0,9)
# print(answer*10)

# 워드 작업 중 정전으로 인하여 컴퓨터가 강제 종료 되었습니다.
# 다시 전기가 들어와 컴퓨터를 켰더니 다행이도 자동복구가 실행 되었습니다.
# 우리는 자동복구가 되었을떄 커서의 위치가 어디인지를 알려줘야 합니다.
# 커서의 위치를 알려주는 프로그램을 완성해 주세요.
# 시간복잡도 O(n^2) 보다 빨라야 합니다.

# 6*12 size 리스트 입니다.

curser=[
 '##########',
 '##########',
 '###_______',
 '__________',
 '__________',
 '__________',
]

def bs1(st,ed):
 Max=-1
 while(1):
  mid=(st+ed)//2
  if curser[mid][0]=='_':
   ed=mid-1
  elif curser[mid][0]=='#':
   Max=mid
   st=mid+1
  if st>ed:
   break
  return Max+1

def bs2(st,ed,yy):
 Maxx = -1
 while (1):
  mid = (st + ed) // 2
  if curser[yy][mid] == '_':
   ed = mid - 1
  elif curser[yy][mid] == '#':
   Maxx = mid
   st = mid + 1
  if st > ed:
   break
 return Maxx + 1

yaxis=bs1(0,5)
xaxis=bs2(0,9,yaxis-1)
print(yaxis-1,xaxis)








