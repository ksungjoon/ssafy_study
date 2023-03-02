# 2차원 배열의 선언
# 1차원 list를 묶어놓은 list

# 2 차원 배열의 접근
# 행 우선 순회
# i 행의 좌표
# j 열의 좌표
# for i in range(n):
#     for j in range(m):
#         Array[i][j]

# 열 우선 순회
# i 행의 좌표
# j 열의 좌표
# for j in range(n):
#     for i in range(m):
#         Array[i][j]

# 지그재그 순회
# i 행의 좌표
# j 열의 좌표
# for i in range(n):
#     for j in range(m):
#         Array[i][j + (m-1-2*j) * (i%2)]
        #필요한 연산 수행

# 델타를 이용한 2차 배열 탐색
# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
# arr[0...N-1][0...N-1] #NxN배열
# di[] <- [0,0,-1,1] # 상하좌우
# dj[] <- [-1,1,0,0]
# for i : 0 -> N-1
#     for j : 0 => N-1 :
#         for k in range(4) :
#             ni <- i + di[k]
#             nj <- j + dj[k]
#             if 0<=ni<N and 0<=nj<N #유효한 인데스면
#                 test(arr[ni][nj])

# di = [0,1,0,-1]
# dj = [1,0,-1,0]
# N = 3
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             ni, nj = i + di[k],j + dj[k]
#             if 0<=ni<N and 0<=nj<N:
#                 print(i,j,ni, nj)
# N = 3
# for i in range(N):
#     for j in range(N):
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni, nj = i +di, j +dj
#             if 0<=ni<N and 0<=nj<N:
#                 print(i, j , ni, nj)
# P = 3
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             for l in range(1,P+1):
#                 ni, nj = i + di[k], j + dj[k]
#                 if 0<=ni<N and 0<=nj<N:
#                     print(i,j,ni,nj)


# 부분 집합 생성하기

# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i           # 0번째 원소
#     for j in range(2):
#         bit[1] = j         # 1번째 원소
#         for k in range(2):
#             bit[2] = k      # 2번째 원소
#             for l in range(2):
#                 bit[3] = l          # 3번째 원소
#                 print_subset(bit)        # 생성된 부분집합 출력


# A  = [1,2,3,4]
# bit = [0] * 4
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit,end=' ')
#                 for p in range(4):
#                     if bit[p]:
#                         print(A[p], end=' ')
#                 print()

# 비트 연산자
# & 비트 단위로 and 연산을한다.
# | 비트 단위로 or 연산을 한다.
# << 피연산자의 비트 열을 왼쪽으로 이동시킨다.
# >> 피연산자의 비트 열을 오른쪽으로 이동시킨다.
# << 연산자
# 1 <<n:2**n 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다.
# i&(1<<j):i의 j번째 비트가 1인지 아닌지를 검사한다.

# 보다 간결하게 부분집합을 생성하는 방법
# 비트 사용
# arr = [3,6,7,1,5,4]
#
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j],end=', ')
#     print()
# print()



# ------------------------------------------
# 지난시간 한거 복습,,
# arr=[[1, 5, 4, 2],
#     [1, 3, 4, 2],
#     [3, 5, 3, 2],
#     [2, 6, 4, 1]]
#
# def getsum(a,b):
#     sum=0
#     for i in range(2):
#         for j in range(3):
#             sum+=arr[a+i][b+j]
#     return sum
#
# maxv=-21e8
# for i in range(3):
#     for j in range(2):
#         ret=getsum(i,j)
#         if ret>maxv:
#             maxv=ret
# print(maxv)

# direct배열을 활용한 코드
# 방향 배열을 활용하기
# 델타배열을 활용하기

# lst = [[3,5,1],[1,1,2],[1,3,9]]
#
# directy = [-1,1,0,0]
# directx = [0,0,-1,1]
# y,x = map(int,input().split())
# sum = 0
# for i in range(4):
#     dy = y + directy[i]
#     dx = x + directx[i]
#     # if dy<0 or dx<0 or dy>2 or dx>2: continue
#     if 0<dy<3 and 0<dx<3:
#         sum += lst[dy][dx]
# print(sum)

# 파이썬만 가능한 코드
# y,x=map(int,input().split())
# ans=0
# for yy,xx in (-1,0),(1,0),(0,-1),(0,1):
#        dy,dx=y+yy,x+xx
#        if 0<=dy<3 and 0<=dx<3:
#               ans+=arr[dy][dx]
# print(ans)



# 좌표값 하나 입력 받아 주세요
# 입력받은 좌표로 부터 대각선에 있는곳의
# 값들의 곱을 구해서 출력 해 주세요!!
# 1 2 입력시 50

arr = [ [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8],
        [1, 2, 9, 1, 2],
        [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8]]

# y,x=map(int,input().split())
# directy=[-1,1,1,-1]
# directx=[1,1,-1,-1]
# gop=1
# for i in range(4):
#         dy=directy[i]+y
#         dx=directx[i]+x
#         if dy<0 or dx<0 or dy>4 or dx>4: continue
#         gop*=arr[dy][dx]
# print(gop)

#--------------------------------------------------------------
# 위 아래 좌 우로 2칸까지 떨어진 곳들의 합을 구하기
# 2 2 입력시  18 출력
# (9+9=18)
#
# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# y, x = map(int,input().split())
#
# movey = [-1, 0, 1, 0]
# movex = [0, 1, 0, -1]
#
# sum = 0
# for i in range(4):
#     for j in range(1,4):
#         newy = y + movey[i] * j
#         newx = x + movex[i] * j
#
#         if 0 <= newy <= 4 and 0 <= newx <= 4:
#             sum += arr[newy][newx]
#
# print(sum)

arr=[[1,2,3,4],
    [1,2,9,4],
    [1,9,3,9],
    [1,2,9,4]]
# 문제 - 위 아래 좌 우 좌표 들의 합이 가장 큰 곳의 합과 그 기준 좌표값을 출력하기

# 위 아래 좌 우  좌표들의 합이 가장 큰 곳의 합과
# 그 기준 좌표값을 출력하기 !!!


def isSum(y,x):
    directy=[-1,1,0,0]
    directx=[0,0,-1,1]
    sum=0
    for i in range(4):
        dy=directy[i]+y
        dx=directx[i]+x
        if dy<0 or dx<0 or dy>3 or dx>3:continue
        sum+=arr[dy][dx]
    return sum

Maxvaule=int(-21e8)
Maxi=0
Maxj=0
for i in range(4):
    for j in range(4):
        ret=isSum(i,j)
        if ret>Maxvaule:
            Maxvaule=ret
            Maxi=i
            Maxj=j
print(Maxvaule,Maxi,Maxj)
# -------------------------------
# 정수값 10을 이진수로 표현하기
# a = 10
# print(bin(a))
# # 2진수의 값을 정수로 표현하기
# b = 0B1111
# print(b)
# # 2진수(문자)값을 정수로 출력하기
# c = '0B1111'
# print((int(c,2)))
#
# # 비트 연산 할때 and or >> <<
# # and
# a = 0b0001
# b = 0b1001
# print(a&b)
# # or 연산
# print(a|b)
# # shift 연산
# a= 0b0001
# b= 0b00101001
# print(a<<2)
# print(b<<3)
# a= 0b0011
# b= 0b00101001
# print(a>>1)
# print(b>>3)
#
