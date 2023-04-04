# Floyd warshall algorithm
# 모든 정점에서 모든 정점으로의 최단 경로
# (feat-dijkstra-시작점(한 정점)에서 모든 정점까지의 최단 경로)
# inf=int(21e8)
# arr=[
#     [0,5,inf,8],
#     [7,0,9,inf],
#     [2,inf,0,4],
#     [inf,inf,3,0]
# ]
#
# for ky in range(4):
#     for si in range(4):
#         for do in range(4):
#             if arr[si][do]>arr[si][ky]+arr[ky][do]:
#                 arr[si][do]=arr[si][ky]+arr[ky][do]
#
# for i in range(4):
#     for j in range(4):
#         print(arr[i][j],end=' ')
#     print()

# 연습해볼만한 문제
# 백준 11403 경로찾기
# 백준 11404 가장빠른버스노선구하기
# 백준 2458 키순서


# anagram
# ex)
# flow - wolf
# listen - silent
# elvis - lives


# 내가 푼것
# arr1 = list(input())
# arr2 = list(input())
#
# def anagram():
#     for i in arr1:
#         if i not in arr2:
#             return 'noanagram'
#     return 'anagram'
#
# print(anagram())

# 문자열 2개를 입력받고

# 입력예제
# wasdfzz
# asdfz
#
# 출력예제
# 2

# 입력시.. 최소 몇개의 글자를 지우면 두 문자열이 anagram이 되나요??
# 문자열 2개를 입력받은후
# 최소 몇개의 글자를 삭제하면 두 문자열이 아나그램 관계가 되는지 출력해 주세요
# (두문자열은 반드시 1개의 아나그램이 존재한다고 가정)

# 입력예제
# applepie
# pizzapple
#
# 출력예제
# 3

# arr1 = input()
# arr2 = input()
# lst1 = [0]*26
# lst2 = [0]*26
# result = 0
# for i in arr1:
#     lst1[ord(i)-97]+=1
# for j in arr2:
#     lst2[ord(j)-97]+=1
# for k in range(26):
#     result+= abs(lst1[k]-lst2[k])
#
# print(result)

# 문자열 2개 입력받은후 arr2의 연속 부분 문자열 중 arr1의 아나그램 개수를 출력하라
# (arr1의 문자열의 길이가 arr2의 길이보다짧다)

# 입력예제
# abcab
# aabbcbbaa
# 출력
# aabbc cbbaa


# arr1 sort 한 것이랑 arr2 sort 비교( sliding window )

# arr1=input()
# arr2=input()
# cnt=0
# for i in range(len(arr2)-len(arr1)+1):
#     if sorted(arr1)==sorted(arr2[i:i+len(arr1)]):
#         cnt+=1
# print(cnt)

#위상 정렬

from collections import deque
name=['cs','language','datastructure','algorithm','project','codingtest','to be a programmer']
arr=[
    [0,0,0,0,0,0,1],
    [0,0,1,1,0,0,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0]]

acc=[0]*7   # 사전 작업 개수
used=[0]*7  # 작업 들어갈지 check

q=deque()
for j in range(7):     # acc 배열에 사전 작업 개수 넣기
    for i in range(7):
        if arr[i][j]==1:
            acc[j]+=1

for i in range(7):    # 바로 작업 착수 가능한 것들은 used에 1 체크하고 큐에 등록
    if acc[i]==0:
        used[i]=1
        q.append(i)

while q:
    now=q.popleft()
    print(name[now],end=' ')
    for i in range(7):
        if arr[now][i]==1 and used[i]==0:
            if acc[i]==1:
                used[i]=1
                acc[i]-=1
                q.append(i)
            else:
                acc[i]-=1