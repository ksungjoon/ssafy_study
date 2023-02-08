# 주사위 N개 재귀함수
# n = int(input())
# def abc(level,path):
#     if level == n:
#         print(path)
#         return
#     for i in range(1,7):
#         abc(level+1,path+str(i))
# abc(0,'')

# 재귀 함수 진행 방향 생각해보기
# def abc(level):
#     if level ==5:
#         return
#     print(level)
#     abc(level+1)
#     print(level)
#
# abc(0)

#7 6 5 4 3 2 2 3 4 5 6 7
# def abc(lev):
#     if lev == 1:
#         return
#     print(lev,end='')
#     abc(lev-1)
#     print(lev,end='')
# abc(7)

# 정수 하나 입력 받은후
# 함수를 3번 호출하면서 입력받은 수에 2씩 더한다
# 리턴되면서 출력
# 1 입력시 7 5 3 1
# 2 입력시 8 6 4 2
# 3 입력시 9 7 5 3
# n = int(input())
# def abc (lev,value):
#     if lev == 3:
#         print(value)
#         return
#     abc(lev+1,value+2)
#     print(value)
#
# abc(0,n)

# 3,7,12,13,19,28, 출력하기 (누적합)
# 전역변수
arr= [3,4,5,1,6,9]
# sum =arr[0]
# def abc(lev):
#     global sum
#     print(sum)
#     if lev ==5:
#         return
#     sum += arr[lev+1]
#     abc(lev+1)
# abc(0)
# 지역변수
# def abc(lev,sum):
#     print(sum)
#     if lev==5:
#         return
#     abc(lev+1,sum+arr[lev+1])
# abc(0,arr[0])

# 28 19 13 12 7 3 출력하기 (누적합)
# accumulated sum 누적합

# 1. sum 매개변수 (지역변수로 활용)
# def abc(lev,sum):
#     if lev == 5:
#         print(sum)
#         return
#     abc(lev+1,sum+arr[lev+1])
#     print(sum)
# abc(0,arr[0])

# 2. sum 전역변수 (globals활용)
sum = arr[0]
def abc(lev):
    global sum
    if lev == 5:
        print(sum)
        return
    sum += arr[lev+1]
    abc(lev+1)
    print(sum)
abc(0)

