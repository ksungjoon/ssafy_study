
# num = int(input())
# if num%2 == 0:
#     print("짝수")
# else:
#     print("홀수")
#
# members = ['민수','영희','철수']
#
# for i, id in enumerate(members):
#     print(i, id)
#
# list comprehension
# 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
# [code for 변수 in iterable]
# [code for 변수 in iterable if 조건식]
# ex)
# cubic_list=[number **3 for number in range(1, 4)]
# print (cubic_list)
# 조건식 붙은건 찾아보기
# cubic_dict={}
#
# for number in range(1,4):
#     cubic_dict[number] = number **3
# print(cubic_dict)
# ---------------------------------------------------------
# cubic_dict = {number: number ** 3 for number in range(1, 4)}
# print(cubic_dict)

# -----------
# 조건문
# 반복문
# 함수
# map filter
# lamda
# ------------
#
# a= int( input())
# if a>5:
#     print('오삼')
# elif a>3:
#     print('불고기')
# elif a>4 or a==-1:
#     print('재시도')
# else:
#     print('오삼불고기')

# 숫자 2개를 입력받은후
# 둘중 큰수를 출력해 주세요
# a,b = map(int,input().split())
# # if a>b:
# #     print(a)
# # elif b>a:
# #     print(b)
#
# result = a if a>b else b # 조건표현식 if 다음에 들어가는 조건이 참이면 앞에 값 반환
# print(result) # 거짓이면 뒤에값 반환

#1~100 까지 for 문으로 출력
#  #을 100번 출력하는 코드
#
# for i in range(1,101):
#     print(i,end=' ')
#
# for i in range(100):
#     print('#',end='')

# a=0
# while a<100:
#     print('#',end='')
#     a+=1
# print()
# a=1
# while a<=100:
#     print(a,end='')
#     a+=1

#리스트 출력 for 이용하여 출력하기
# lst=[[1,2,3],[4,5,6]]
# print(lst[0][1])
#
# for i in range(0,2):
#     for j in range(0,3):
#         print(lst[i][j],end='')

# 1차원 리스트
# 빈리스트 하나 만든후 lst의 값에 제곱을 한 값으로 채워넣기
# 새로 만들어진 리스트를 출력하기

# lst = [[1,2,3],[4,5,6]]
# multi=[]
# for i in range(2):
#     for j in range(3):
#         multi.append(lst[i][j]**2)
# print(*multi,sep='')
#
# for i in multi:
#     print(i,end='')

# web
# 프로그래밍 언어 + 알고리즘 = 가장 중요하고가장어려운 것이 for문 잘돌리기
# lst = [[1,2,3],[4,5,6]]
# multi=[]
# for i in range(2):
#     temp=[]
#     for j in range(3):
#         temp.append(lst[i][j]**2)
#     multi.append(temp)
# print(multi)

# 딕셔너리
# di = {'kebin':1,'jhon':2,'bob':3}
# print(di)
#
# for i in di:
#     print(i,di[i])
#
# for i,j in di.items():
#     print(i,j)
#
# print(di.items())

# break 반복문을 중간에 멈추고 싶을때 for while 함수 종료가 아님
# return 함수의 값을 반환하거나 또는 그냥 함수 종료
# lst= [10,20,30,40,50,60,70]
# for i in lst:
#     if i == 50:
#         break
#     print(i,end=' ')
#
# a=3
# print(a)

# lst = [[1,2,3],[1,2,3],[1,2,3]]
# for i in range(3):
#     for j in range(4):
#         if lst[i][j]==3:
#             break
#         print(lst[i][j],end='')
# # 가까운 반복문만 끈다
# flag=0
# for i in range(3):
#     for j in range(4):
#         if lst[i][j]==3:
#             flag=1
#             break
#         print(lst[i][j],end='')
#     if flag: # if flag ==1: 과 같은 말
#         break

# continue 아래코드는 실행하지않고 맨위로 다시 올라감

# lst = [1,2,3,4,5,6,7]
# for i in lst:
#     if i==5:
#         continue
#     print(i,end=' ')

# lst = [[1,2,3],[1,2,3],[1,2,3]]
# for i in range(3):
#     for j in range(3):
#         if lst[i][j]==2:
#             continue
#         print(lst[i][j],end=' ')
# continue 아래코드는 실행하지않고 아래있는 반복문의 위로 올라가는것

#두 숫자를 전달 받고 합을 돌려주는 함수를 만들도록
# def getsum(a,b): # 매개변수 parameter
#     return a+b
# print(getsum(3,4)) # getsum(3,4)인자값 argument
# a=3
# b=7
# ret = getsum(a,b)
# print(ret)
#
#
# #값 두개 반환 전역변수 사용하기
#
# sum1=0
# gop1=0
# def getsum2(a,b):
#     global sum1,gop1
#     sum1 = a+b
#     gop1 = a*b
#
# getsum2(5,6)
# print(sum1, gop1)
#
# def abc():
#     global aa,bb
#     aa=3
#     bb=5
#     print(aa,bb)
# #aa,bb 위에서 지역변수 전역변수로 사용하려면 global쓰면 된다.
# abc()
# print(aa,bb)
# def getsum(a,b=7,c=7):
#     return a+b+c
# ret= getsum(6,5,6)
# print(ret)
# 패킹
# num=[1,2,3,4,5]
# num2=(1,2,3,4,5)
# print(num,num2)
# # 언패킹
# a,b,c,d,e=num
# print(a,b,c,d,e)
# a,b,c,d,e=num2
# print(a,b,c,d,e)
# a,b,*c=num
# print(c)
# a,b,*c=num2
# print(c)

#아스트리스크 *
#아스트랄 *

# def getsum(*a):
#     sum= 0
#     for i in a:
#         sum+=i
#     return sum
#
# result = getsum(1,1,3)
# print(result)
# # 함수문에 아스트랄 쓰면 튜플의 형태로 변환된다
# def print_info(**args):
#     print(args)
#     for i,j in args.items():
#         print(i,j)
# print_info(kebin=1,jhon=2,bob=3)
# a={'dkfk':2,'fksdfl':4,'sfkdk':6}
# print(print_info(**a))


#map
# 리스트나 튜플같은 순회가능한 데이터 구조 값들에
# 함수를 일괄적으로 적용하고
# 적용후 값을 map이라는 객체로 반환
# 사용법 map(함수,iterebles)
#
# num = ['1','2','3']
# lst1=[]
# for i in num:
#     lst1.append(int(i))
# print(lst1)
#
# lst2= map(int,num)
# print(lst2)
# print(list(lst2))#리스트 형태로 바꿔서 출력
#
# lst1=[1,2,3]
# lst2=[4,5,6]
# # lst3 라는 리스트에 lst1과 lst2의 합을 저장하는 리스트로 만든 후 출력
#
# def func(a,b):
#     return  a+b
#
# lst3 = list(map(func,lst1,lst2))
# print(lst3)