# 두배열 merge 하기 민코딩  훈련반 1 20.5

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# result = []
# A_index = 0
# B_index = 0
# while(1):
#
#     if A_index > 3 and B_index > 3:
#         break
#     elif A_index > 3:
#         result.append(B[B_index])
#         B_index += 1
#     elif B_index > 3:
#         result.append(A[A_index])
#         A_index += 1
#     elif A[A_index] >= B[B_index]:
#         result.append(B[B_index])
#         B_index += 1
#     elif A[A_index] < B[B_index]:
#         result.append(A[A_index])
#         A_index += 1
#
# print(*result, sep=' ')


# merge 사용하여 정렬하기 merge sort
# arr=[3,4,1,7,2,9,8,3]
# result=[0]*8
# def merge(start,end):
#     mid=(start+end)//2
#     if start>=end: return
#
#     merge(start,mid)
#     merge(mid+1,end)
#
#     a=start
#     b=mid+1
#     index=0
#
#     while 1:
#         if a>mid and b>end: break
#         if a>mid:
#             result[index]=arr[b]
#             index+=1
#             b+=1
#         elif b>end:
#             result[index]=arr[a]
#             index+=1
#             a+=1
#         elif arr[a]<=arr[b]:
#             result[index]=arr[a]
#             index+=1
#             a+=1
#         else:
#             result[index]=arr[b]
#             index+=1
#             b+=1
#     for i in range(index):
#         arr[start+i]=result[i]
#
# merge(0,7)
#
# print(*arr)


# quick 정렬 -- 민코딩 23.5 자기자리 찾기
# lst = list(map(int,input().split()))
#
# pivot = lst[0]
# a= 1
# b= len(lst)-1
# while b>=a:
#     if pivot < lst[a] and pivot > lst[b]:
#         lst[a], lst[b] = lst[b], lst[a]
#     elif lst[a]<pivot:
#         a += 1
#     elif lst[b]>pivot:
#         b -= 1
# lst[0],lst[b]=lst[b],lst[0]
# print(lst)


# 교수님 꺼
# 퀵 핵심 코드
#
# arr=list(map(int,input().split()))
# pivot=arr[0]
# a=1
# b=len(arr)-1
#
# while 1:
#     while a<len(arr) and arr[a]<=pivot:
#         a+=1
#     while b>0 and arr[b]>pivot:
#         b-=1
#     if a>b: break
#     arr[a],arr[b]=arr[b],arr[a]
# arr[b],arr[0]=arr[0],arr[b]
# print(*arr)

# quick sort
# lst = [4,1,7,9,6,3,3,6]
# def quick (st,ed):
#     if st >= ed:
#         return
#     pivot = st
#     a = st +1
#     b =ed
#     while b >= a:
#         if lst[pivot] < lst[a] and lst[pivot] > lst[b]:
#             lst[a], lst[b] = lst[b], lst[a]
#         elif lst[a]<=lst[pivot]:
#             a += 1
#         elif lst[b]>=lst[pivot]:
#             b -= 1
#     lst[pivot],lst[b]=lst[b],lst[pivot]
#
#     quick(st, b-1)
#     quick(b+1,ed)
#
#
# quick(0,7)
# print(lst)
#


# 퀵 소트

# arr=[4,1,7,9,6,3,3,6]


# def quick(start,end):
#     if start>=end: return
#
#     pivot=start
#     a=start+1
#     b=end
#     while 1:
#         while a<=end and arr[a]<=arr[pivot]: a+=1
#         while b>=start and arr[b]>arr[pivot]: b-=1
#         if a>b: break
#         arr[a],arr[b]=arr[b],arr[a]
#
#     arr[pivot],arr[b]=arr[b],arr[pivot]
#
#     quick(start,b-1)
#     quick(b+1,end)
#
# quick(0,7)
# print(*arr)