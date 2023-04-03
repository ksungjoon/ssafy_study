# 우선순위 큐

# import heapq
#
# arr = []
#
# heapq.heappush(arr,1)
# heapq.heappush(arr,11)
# heapq.heappush(arr,61)
# heapq.heappush(arr,81)
# heapq.heappush(arr,13)
# heapq.heappush(arr,14)
#
# for i in range(len(arr)):
#     print(heapq.heappop(arr))
#
# 거꾸로 출력하기
# import heapq
#
# arr = []
#
# # 음수로 입력
# heapq.heappush(arr,1*-1)
# heapq.heappush(arr,11*-1)
# heapq.heappush(arr,61*-1)
# heapq.heappush(arr,81*-1)
# heapq.heappush(arr,13*-1)
# heapq.heappush(arr,14*-1)
#
# for i in range(len(arr)):
#     # print(-heapq.heappop(arr))
#     print(heapq.heappop(arr)*-1)


# import heapq
#
# arr = [88,1,6,8,34,23,4,65]
#
# heap = []


# 올림차순
# for i in range(len(arr)):
#     heapq.heappush(heap,arr[i])
#
#
# for i in range(len(arr)):
#     print(heapq.heappop(heap))
#

# 내림차순
# for i in range(len(arr)):
#     heapq.heappush(heap,-arr[i])
#
#
# for i in range(len(arr)):
#     print(-heapq.heappop(heap))

# 튜플 이용하기
# 튜플을 이용해서 max heap 출력
# for i in range(len(arr)):
#     heapq.heappush(heap,(-arr[i],arr[i]))

# print(*heap)

# for i in range(len(arr)):
#     print(heapq.heappop(heap)[1])


# heapify 이용해보기
# heapq.heapify(arr)
#
# for i in range(len(arr)):
#     print(heapq.heappop(arr))

# heapify 이용해서 max heap 출력하기
# arr2=[3,8,5,2,8,4,1,5]
# rev = lambda x:x*-1
# heap=list(map(rev,arr2))
# heapq.heapify(heap)
#
# for i in range(len(arr2)):
#     print(-heapq.heappop(heap))


# 문제 풀어보기
#
# 카드 정렬하기
#
# 정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.
#
# 매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.
#
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.
#
#
# 입력`
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.
#
#
# 출력
# 첫째 줄에 최소 비교 횟수를 출력한다.
#
# 입력
# 4
# 50
# 20
# 70
# 30
#
# 출력
# 320
#
#
# 입력
# 3
# 10
# 20
# 40
#
# 출력
# 100

# import heapq
# N = int(input())
# arr = []
# result = 0
# for i in range(N):
#     heapq.heappush(arr,int(input()))
#
# while (len(arr)>1):
#     temp1= heapq.heappop(arr)
#     temp2= heapq.heappop(arr)
#     result+= (temp1+temp2)
#     heapq.heappush(arr,temp1+temp2)
#
# print(result)
#민코 level 35 + 프로그래머스 heap (코테고득점kit)  연습해 주시면 됩니다.


import heapq
#
# 5       # 정점개수
# 7       # 간선의 개수
# 0 1 3   # 간선의 정보
# 0 4 5   # 출발index  도착index  비용
# 0 3 9
# 1 4 1
# 1 2 7
# 2 3 1
# 4 2 1
# 0 3     # 시작점 && 도착지

# 입력받기
n=int(input()) # 정점개수 입력
m=int(input()) # 간선 개수 입력
arr=[[] for _ in range(n)] # 인접 리스트 만들어주고
for _ in range(m):  # 인접리스트에 입력받기
    a,b,c=map(int,input().split()) # a 출발 b 도착 c 비용
    arr[a].append((b,c))
start,end=map(int,input().split())  # 문제에서 주어지는 시작점과 최종도착점(알고싶은값)

# 셋팅하기
name='ABCDE'
inf=int(21e8)
result=[inf]*n
result[start]=0 # 시작인덱스를 첫 경유지로 할것 인데.. 시작인덱스에 해당하는 경우지 까지의 비용을 0으로 초기 셋팅
heap=[] # 경유지를 뽑은 (우선순위큐로 뽑을) 힙 만들어 놓기


def dijkstra(start):
    heapq.heappush(heap,(0,start))  # 시작점index(첫 시작점을 첫 경유지로 놓기떄문), 비용(시작점->경유지까지)

    while heap: # 경유지 선택이 끝날때 까지

        sk,k = heapq.heappop(heap)     # k 경유지  sk 경유지까지 비용(힙 안에 있는 (시작점->경유지))

        if result[k]<sk: continue    # 이미 갱신 되어 있는 값이 뽑은 값 보다 작으면 비교할 필요 없음!!

        for i in arr[k]: # 경유지에서 다른 도착점 까지 갈수있는 횟수만큼 for 문 돌리기 (인접행렬 탐색)
            cost=sk+i[1] # cost=시작->경유  +  경유지에서 도착점 까지 가는 비용
            if cost<result[i[0]]: # cost: 시->경->도착     result[i[0]] 시작점 -> 도착
                result[i[0]]=cost # 갱신 해주고
                heapq.heappush(heap,(cost,i[0])) # 힙에 푸쉬!!

dijkstra(start)

print(*result)
print(result[end])
