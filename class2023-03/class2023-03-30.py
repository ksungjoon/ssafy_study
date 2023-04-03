# 최대 공약수 (greatest common divisor) GCD
#
# 숫자 두개가 있다.

# 38 8
# 2 부터 8까지의 수로 두 수를 나누었을때
# 각각 0으로 떨어지는 수 들 중에서 가장 큰수

# answer = 0
# a,b = map(int,input().split())
# for i in range(2,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         answer = i
# print(answer)

# 유클리드 호제법(최대 공약수를 구하는 알고리즘)

# answer = 0
# a,b = map(int,input().split())
# while b:
#     answer=a%b
#     a=b
#     b=answer
# print(a)

# 최소 공배수 -> (Leat common multiple) LCM
# a,b, 의 최소 공배수를 구하자
# answer = gcd*(a/gcd)*(b/gcd)


# 숫자 하나 입력 받으면
# 입력받은 그 숫자가 소수 인지 아니니 출력해주셍
# 소수-  1과 자기 자신으로만 나눌 수 있는 수

# a = int(input())
# flag = 0
# for i in range(2,a):
#     if a%i == 0:
#         flag = 1
#         break
# if flag: print('소수아님')
# else: print('소수임')
# 에라토스테네스의 체

# 문제 숫자하나 입력 받은후 입력받은 숫자보다 작은 소수들 모두 출력하시오

# a = int(input())
# result = []
# for i in range(1,a):
#     flag = 0
#     for j in range(2,i):
#         if i%j ==0:
#             flag =1
#             break
#     if flag!=1:
#         result.append(i)
# print(result)

# 교수님이 푼 문제

a = int(input())
check=[1]*(a+1)
answer = []

for i in range(2,a+1):
    if check[i] ==1 :
        answer.append(i)
    for j in range(i+i,a+1,i):
        check[j]=0
print(*answer)

# 제곱근의 쉬운코드
import math
a=int(input())
check=[1]*(a+1)
answer=[]

for i in range(2,int(math.sqrt(a))+1):
    if check[i]==0: continue
    for j in range(i+i,a+1,i):
        check[j]=0

for i in range(2,a+1):
    if check[i]==1:
        print(i,end=' ')