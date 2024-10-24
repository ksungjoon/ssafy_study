# Ssafy 편의점에는 ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다.
#
# 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
#
# 사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다.
#
# 예를 들어, 총 5명이 있고, P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2 인 경우를 생각해보자.
#
# [1, 2, 3, 4, 5] 순서로 줄을 선다면, 1번 사람은 3분만에 돈을 뽑을 수 있다. 2번 사람은 1번 사람이 돈을 뽑을 때 까지
#
# 기다려야 하기 때문에, 3+1 = 4분이 걸리게 된다. 3번 사람은 1번, 2번 사람이 돈을 뽑을 때까지 기다려야 하기 때문에,
#
# 총 3+1+4 = 8분이 필요하게 된다. 4번 사람은 3+1+4+3 = 11분, 5번 사람은 3+1+4+3+2 = 13분이 걸리게 된다.
#
# 이 경우에 각 사람이 돈을 인출하는데 필요한 시간의 합은 3+4+8+11+13 = 39분이 된다.
#
# 줄을 [2, 5, 1, 4, 3] 순서로 줄을 서면, 2번 사람은 1분만에, 5번 사람은 1+2 = 3분, 1번 사람은 1+2+3 = 6분, 4번 사람은
#
#  1+2+3+3 = 9분, 3번 사람은 1+2+3+3+4 = 13분이 걸리게 된다. 각 사람이 돈을 인출하는데 필요한 시간의 합은
#
#  1+3+6+9+13 = 32분이다. 이 방법보다 더 필요한 시간의 합을 최소로 만들 수는 없다.
#
# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때,
#
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최소값을 구하는 프로그램을 작성하시오.
#
#
#
# 입력 !!
# 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다.
# (1 ≤ Pi ≤ 1,000)
#
# 출력 !!
# 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.
#
# 입력
# 5
# 3 1 4 3 2
#
# 출력
# 32

# 내가 푼거

# N = int(input())
# lst = list(map(int,input().split()))
# lst = sorted(lst)
# result = 0
# for i in range(len(lst)):
#     a=1
#     a+=i
#     for j in range(a):
#         result += lst[j]
# print(result)

# 10
# 18 21
# 11 14
# 15 17
# 18 22
# 13 16
# 10 16
# 12 23
# 22 24
# 16 20
# 15 19
# 예약 개수 입력 후
# 예약시작시간 파티 마치는시간 입력 받습니다.
# Q. 최대 몇개의  party 예약을 받을 수 있나요?

# N = int(input())
#
# lst = [list(map(int,input().split()))for i in range(N)]
# lst = sorted(lst,key=lambda x:x[1])
#
# time = 0
# answer = 0
# for i in range(N):
#     if time <= lst[i][0]:
#         time = lst[i][1]
#         answer+=1
# print(answer)


# dp 동적계획법 dynamic programing

#개구리가 갈수 점프 할수 있는 경우수 +1 ,+2 ,*2 일경우 최소 값
# arr = [0, 7, 3, -5, -1, -9, -2, 6, 5, -4, 0]
# n = len(arr)
# dp = [0] * n
#
# for i in range(1, len(arr)):
#     jp1 = dp[i - 1]
#     jp2 = dp[i - 2]
#     jp3 = dp[i // 2]
#
#     dp[i] = jp1 + arr[i]
#     if dp[i] < jp2 + arr[i]:
#         dp[i] = jp2 + arr[i]
#     if i % 2 == 0 and dp[i] < jp3 + arr[i]:
#         dp[i] = jp3 + arr[i]
#
# print(dp[n - 1])


# 동적 계획법

# 우측 아래로만 갈수 있을때 출발점에 도착했을때 더하는 최소 값
# arr = [[0, 7, 1, 4, 3],
#        [1, 9, 6, 1, 5],
#        [3, 2, 5, 4, 7],
#        [1, 6, 5, 9, 8],
#        [7, 4, 3, 5, 0]]
#
# acc = [[0] * 5 for _ in range(5)]
#
#
# # 가장 우측 그리고 최 하단값 셋팅하기
# def sett():
#     for i in range(3, -1, -1):
#         acc[i][4] = acc[i + 1][4] + arr[i][4]
#         acc[4][i] = acc[4][i + 1] + arr[4][i]
#
#
# sett()

# 2중 for 돌면서
# (우측 그리고 아래 값 중 작은값) + 원본데이터값
# for i in range(3, -1, -1):
#     for j in range(3, -1, -1):
#         down = acc[i + 1][j]
#         right = acc[i][j + 1]
#
#         if down > right:
#             value = right
#         else:
#             value = down
#
#         acc[i][j] = value + arr[i][j]
# print(acc[0][0])

# 한 달 후면 국가의 부름을 받게 되는 최싸피는 여행을 가려고 한다.
# 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에,
# 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.
# 최싸피가 여행에 필요하다고 생각하는 N개의 물건이 있다.
#
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 최싸피가 V만큼 즐길 수 있다.
# 아직 행군을 해본 적이 없는 최싸피는 최대 K 만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
# 최싸피가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
#
# 입력 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 최싸피가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100, 000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
#
# 입력으로 주어지는 모든 수는 정수이며 제한시간은 2초 이다.
#
# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
#
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
#
# 출력
# 14

# n, k = map(int, input().split())
# knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  # 배열
#
# item = [[0, 0]]
# for i in range(1, n + 1):  # 아이템 입력
#     item.append(list(map(int, input().split())))
#
# for i in range(1, n + 1):  # 아이템 개수만큼 반복
#     for j in range(1, k + 1):  # 최대무게까지 반복
#
#         weight = item[i][0]
#         value = item[i][1]
#
#         if j < weight:  # 가방에 넣을 수 없으면
#             knapsack[i][j] = knapsack[i - 1][j]  # 위에 값 그대로 가져오기
#         else: # 가방에 넣을 수 있으면
#             knapsack[i][j] = max(knapsack[i - 1][j],value + knapsack[i - 1][j - weight])
#             # 위에 값 vs
#             # 현재 아이템 가치 + 그전 단계에서 구한 남은무게의 가치



# # 문제
# 10 70 110 원짜리 동전이 있다
# 거슬러 줄 돈을 입력 받은 후
# 최소 몇개의 동전을 사용하여 거슬러 줄 수 있는지 출력해 주세요
#
# # 설계
# 1. dp 테이블 셋팅 후 (2차원 배열)
# 2. "사용할 동전"으로 딱 나누어 질 때 -> 나눈 몫으로 값넣기
#                   딱 나누어 지지 않을 떄(나머지가 있을때) ->
#                   2-1 몫이 0일떄 (동전값이 너무 크다면) 윗줄에서 구한 값 넣기
#                   2-2 몫이 0이 아닐떄 (동전값이 너무 큰 것이 아니라면)
#                          윗줄에서 구한 값 vs 몫+그줄에서 구한 나머지의 최대치를 비교해서 적은값 넣기
#
# coin=[10,70,110]
# n=int(input())
# arr=[[0 for _ in range(n+1)] for _ in range(3)]  #dp 배열 만들기
# for i in range(3): # 동전의 개수만큼 for문 돌리기
#     for j in range(n+1): # j는 dp테이블의 너비를 뜻함
#         mok=j//coin[i]
#         if j%coin[i]==0:    # 나누어 질떄
#             arr[i][j]=mok
#         else:
#             if mok==0:
#                 arr[i][j]=arr[i-1][j] # 윗줄에서 구한 값
#             else:
#                 arr[i][j]=min(arr[i-1][j],mok+arr[i][j%coin[i]]) # 최소값 (윗줄에서 구한값 vs 몫+그줄에서 구한 나머지의 최대치를 비교해서 적은값 넣기)
#
# print(arr[2][n])

# dp문제 풀때 정올!!!