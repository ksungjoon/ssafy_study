# 알고리즘 스터디
N = int(input())  # 주사위 개수 입력받음
lst = [list(map(int,input().split()))for i in range(N)] # 주사위 입력 받음
def abc(lev,x): # 재귀문 현재 주사위 = lev  주사위 아랫면=x
    global result  # result 전역변수로 함수로 설정
    if lev == N:  # 주사위가 N일때 리턴
        return
    for i in range(6): # 6번 반복
        if lst[lev][i]==x: # 아래 숫자인 x값의 인덱스 번호를 찾고 그에 반대에 위치해 있는 숫자 index값 찾기
            if i == 0:
                z = 5
            if i == 1:
                z = 3
            if i == 2:
                z = 4
            if i == 3:
                z = 1
            if i == 4:
                z = 2
            if i == 5:
                z = 0
    stack[lev].remove(x) # 스택에서 주사위 아랫면값 삭제
    stack[lev].remove(lst[lev][z]) # 스택에서 주사위 윗면값 삭제
    abc(lev+1,lst[lev][z])# 주사위 첫번째 위면을 두번째 아래면 주사위로 두고 재귀문 들어가기

mmax = 0 # max변수 생성
for i in range(1, 7): # 1~6까지 반복
    stack = [[1, 2, 3, 4, 5, 6] for i in range(N)] # stack 생성
    result = 0 # result 변수 생성
    abc(0,i) # abc 위의 함수를 1~6까지 반복
    for j in range(N): # stack 을 주사위 갯수만큼 반복해 stack list의 최댓값 들 계속 더함
        result+=max(stack[j])
    mmax = max(result, mmax) # 아랫면이 1~6까지 일때 최댓값중 최댓값 도출

print(mmax) # 최댓값 출력










# T = int(input())
# for test_case in range(1,T+1):
#     n = int(input())
#     lst = [list(map(int,input()))for i in range(n)]
#     result = 0
#     diry=[-1,0,0,1]
#     dirx = [0,-1,1,0]
#     for i in range(n):
#         for j in range(n):
#             if lst[i][j] == 2:
#                 starty = i
#                 startx = j
#                 lst[i][j] = 0
#             if lst[i][j] ==3:
#                 endy=i
#                 endx=j
#                 lst[i][j]=0
#     def abc(y,x):
#         global result
#         for i in range(4):
#             dx=dirx[i]+x
#             dy=diry[i]+y
#             if 0 <= dy <n and 0 <= dx <n:
#                 if lst[dy][dx]==0 :
#                     lst[dy][dx] = 1
#                     abc(dy,dx)
#                     lst[dy][dx] = 0
#                     if result == 1:
#                         return
#
#
#     abc(starty,startx)
#     print(f'#{test_case} {result}')
