# sw 1979 어디에 단어가 들어갈 수 있을까?
# sw 1974 스도쿠 검증
# sw 1961 숫자 배열 회전
# sw 1211. Ladder2


# sw 1979 어디에 단어가 들어갈 수 있을까?
# T = int(input())
# for test_case in range(1, T + 1):
#     N,K =map(int,input().split())
#     lst = [list(map(int,input().split()))for i in range(N)]
#     count = 0
#     result = 0
#     y = 0
#     x = 0
#     while 0<=x<N and 0<=y<N:
#         while lst[y][x] == 1 and x < N:
#             count += 1
#             x += 1
#             if x == N:
#                 break
#         if count == K:
#             result += 1
#             count = 0
#             x += 1
#         else:
#             count = 0
#             x += 1
#         if x >= N:
#             x = 0
#             y += 1
#             continue
#     y = 0
#     x = 0
#     while 0<=x<N and 0<=y<N:
#         while lst[x][y] == 1 and x < N:
#             count += 1
#             x += 1
#             if x == N:
#                 break
#         if count == K:
#             result += 1
#             count = 0
#             x += 1
#         else:
#             count = 0
#             x += 1
#         if x >= N:
#             x = 0
#             y += 1
#             continue
#     print(f'#{test_case} {result}')

# sw 1974 스도쿠 검증
# def solve(arr):
#     for lst in arr:  # 행을 체크
#         if len(set(lst)) != 9:  # 스도쿠 실패
#             return 0
#
#     arr_t = list(zip(*arr))
#     for lst in arr_t:  # 열을 체크
#         if len(set(lst)) != 9:  # 스도쿠 실패
#             return 0
#
#     for i in (0, 3, 6):
#         for j in (0, 3, 6):  # 3*3 격자
#             lst = arr[i][j:j + 3] + arr[i + 1][j:j + 3] + arr[i + 2][j:j + 3]
#             if len(set(lst)) != 9:
#                 return 0
#     return 1
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#
#     ans = solve(arr)
#     print(f'#{test_case} {ans}')





# sw 1961 숫자 배열 회전
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = [input().split() for _ in range(N)]
#     arr_t = list(map(list, zip(*arr)))
#     a1 = [[0] * N for _ in range(N)]  # 90도
#     a2 = [[0] * N for _ in range(N)]
#     a3 = [[0] * N for _ in range(N)]
#
#     # [2] 전치배열과 읽는 방향에 따른 처리
#     print(f'#{test_case}')
#     for i in range(N):
#         print(f'{"".join(arr_t[i][::-1])} {"".join(arr[N - 1 - i][::-1])} {"".join(arr_t[N - 1 - i])}')

    # # [1] 회전각도에 따른 위치값을 저장
    # for i in range(N):
    #     for j in range(N):
    #         a1[i][j] = arr[N-1-j][i]
    #         a2[i][j] = arr[N-1-i][N-1-j]
    #         a3[i][j] = arr[j][N-1-i]
    # print(f'#{test_case}')
    # for a,b,c in zip(a1,a2,a3):
    #     print(f'{"".join(a)} {"".join(b)} {"".join(c)}')

# sw 1211. Ladder2
# T = 10
# for test_case in range(1, T + 1):
#     _ = int(input())
#     arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
#     mn = 100 * 100
#     for sj in range(1, 101):
#         # [1] 시작지점 찾기
#         si = 0
#         if arr[si][sj] != 1:
#             continue
#         cnt, dj = 0, 0
#         ci, cj = si, sj
#         while ci < 99:
#             cnt += 1
#             if dj == 0:
#                 if arr[ci][cj - 1] == 1:  # 좌측
#                     dj = -1
#                     cj -= 1
#                 elif arr[ci][cj + 1] == 1:  # 우측
#                     dj = 1
#                     cj += 1
#                 else:
#                     ci += 1
#             else:
#                 if arr[ci][cj + dj] == 1:
#                     cj += dj
#                 else:  # 진행방향이 막힌경우 아래로
#                     dj = 0
#                     ci += 1
#         if mn >= cnt:
#             mn, ans = cnt, sj - 1
#
#     print(f'#{test_case} {ans}')
#==================================================================================
# 재귀 진도
# arr = [3,4,5,1,6,9]
# 누적합 출력하기 !!
# 3 7 12 13 19 28 13 12 7 3
#
# 1 sum을 매개변수로 놓고 코드 작성해 보기
# def abc(lev,sum):
#     print(sum,end=' ')
#     if lev ==5:
#         return
#     abc(lev+1,sum+arr[lev+1])
#     print(sum,end=' ')
# abc(0,3)
# 2 sum을 전역 로 놓고 코드 작성해 보기
# sum = 3
# def abc (level):
#     global sum
#     print(sum,end=' ')
#     if level == 5:
#         return
#     sum += arr[level+1]
#     abc(level+1)
#     sum -= arr[level + 1]
#     print(sum,end=' ')
# abc(0)
# 개구리가 점프하는 하고 돌아 오는 발자취
# arr = [2,0,1,1,1,3,5,1]
#
# def abc(lev):
#     if lev>=len(arr):
#         return
#     abc(lev+arr[lev])
#     print(arr[lev],end='')
# abc(0)

# 지역변수 사용
# lst = [3,7,1,2]
# def abc (lev,sum):
#     if lev == 3:
#         print(sum,end=' ')
#         return
#     for i in range(4):
#         abc(lev + 1,sum+lst[i])
#
# abc(0,0)

# 전역변수 사용
# sum=0
#
# def abc(level):
#     global sum
#     if level==3:
#         print(sum,end=' ')
#         return
#     for i in range(4):
#         sum+=lst[i]
#         abc(level+1)
#         sum-= lst[i]
# abc(0)
# n개의 카드 묶음에서 각각 1개씩 카드를 뽑아서 더했을때 합이 20이 넘는 경우는 몇가지??
# arr = [2,7,1,4,3]
# n = int(input())
# count = 0
# sum = 0
# def abc(lev,sum):
#     global count
#     # if sum > 20:   # n 을 4라고 가정했을때 더하다가 20 넘으면 그냥 바로 카운트하고 리턴
#     #     count += 1
#     #     return
#     if lev == n:
#         if sum>20:
#             count+=1
#         return
#     for i in range(5):
#         abc(lev+1,sum+arr[i])
# abc(0,0)
# print(count)
#
# 최소 동전 개수로 거슬러 주는법 서로 배수가 아닐때
# changes=int(input())
# coin=[110,70,10]
# min=21e8
# def abc(level,changes):
#     global min
#     if changes<0:
#         return
#     if changes==0:
#         if level<min:        # 최소레벨
#             min=level
#             return
#     for i in range(3):
#         abc(level+1,changes-coin[i])
# abc(0,changes)
# print(min)

# 중복 순열
# lst = ['A','B','C']
# path = [0,0]
# def abc(lev):
#     global path
#     if lev ==2:
#         print(*path,sep='')
#         return
#     for i in range(3):
#         path[lev] = lst[i]
#         abc(lev+1)
# abc(0)

# 주사위 던졌을때 나올수 있는 모든 경우의 수
lst = [1,2,3,4,5,6]
n =int(input())
path = [0]*n
def abc(lev):
    if lev==n:
        print(*path,sep='')
        return
    for i in range(6):
        path[lev] = lst[i]
        abc(lev+1)
abc(0)

# for문 연습2문제 간단한것
# 마지막 input challenge