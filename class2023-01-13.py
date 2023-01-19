num =5   #정수값
print(num)
print(type(num))

st ='5'  #문자열'5555'
print(st)
print(type(st))

# 문자열 - char
# 문장 문자열 = string '55555'

# 자료형 int, str, boolean(True or False)
bolean = (3>5)
print(bolean)
print(type(bolean))

#문자열 출력 !!
name= '김성준'
age= 27
#%string
#str. format
#f-string

print('제 이름은  %s이고 %d살 입니다.'%(name,age))
print('제 이름은  {0}이고 {1}살 입니다.'.format(name,age))
print(f'제 이름은  {name}이고 {age}살 입니다.')

# %d = 정수 소수점 없는 숫자
# %s = 문자열
# %f = 실수 소수점이 있는 숫자

a= 1
b= 2
c= 3


lst = [1,2,3,4,5,6,7,8]
lst = ['java','django','c++','ruby','python']
print(lst[0])
print(lst)
print(len(lst))
# len = 리스트의 길이를 알려주는 내장함수
print(lst[1:4]) # 인덱싱
# 1.어제 먹은 아침 점심 저녁 메뉴로 채워진 리스트 하나 만들어 보세요
a= ['고기', '생선', '회']

# 2. 아침에 먹은 메뉴를 출력해 주세요
print(a[0])
# 3. 저녁에 먹은 메뉴를 출력해 주세요.
print(a[2])

#변수
#리스트
#딕셔너리

phone_number={'최':'010','민':'9353','호':'6698',111:'굳굳'}
print(phone_number)
# 최 민 호 111 키 값
# 010 9353 6698 굳굳 값
print(phone_number['최'],phone_number['민'],phone_number['호'])
print(phone_number[111])
#자신의 이름 나이 인사말로 구성된 my info라는 딕셔너리를 하나 만들어 주세요
my_info={'name':'kimsungjoon',
         'age':'27',
         'msg':'nice too mee you',
         'study':{'startcamp':'3days',
                  'python':'2weeks',
                  'algorithm':'6weeks'},
111:'굳굳'}
print(my_info['age'])
print(my_info['study'])
print(my_info['study']['python'])

# 영화 관련 딕셔너리

movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [{'nationNm': '한국'}],
        'genres': [{'genreNm': '사극'}, {'genreNm': '드라마'}],
        'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
        'actors': [
            {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
            {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
            {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
        ],
    }
}
#
# 1 . 영화 제목 출력
print(movie['movieInfo']['movieNm'])
#2 . 다음 영화 감독의 영어 이름
print(movie['movieInfo']['directors'][0]['peopleNmEn'])
#3 . 다음 영화의 배우의 인원
print(len(movie['movieInfo']['actors']))

# 코드 작성시 고민을 하면서 적는것이 아니라
# (우리가 말할때 무슨말을 해야할지 생각하면서 말하지 않고 바로바로 말하듯이 코드를 작성해야 하는 것이 개발자 공부하는데 1순위)

# if for 함수 변수 배열(리스트)
# a = int(input())
# # if a>5:
# #     print('정답입니다')
# # print('*')
#
# if a>5:
#     print('정답입니다')
# elif a==3:
#     print("반만 정답")
# elif a > 2:
#     print('좋아요')
# else:
#     print('오답입니다')

# if a!=5:
#     print('오답입니다')

#==같다
#!=같지 않다

#if 조건이 참이면 실행
#else else문 바로 위에 조건이 거짓이면 실행
#elif 바로 위에 조건이 거짓이고 내조건(elif)참이면 실행

#먼지 별 출력문

# dust=int(input())
# if dust>150:
#     print("매우나쁨")
# elif 151>dust>80:
#     print("나쁨")
# elif 81>dust>30:
#     print("보통")
# elif 31>dust:
#     print("좋음")

#정수 1개를 입력받은후 입력받은 정수가 홀수 인지 짝수 인지 판별 하여 출력하는 코드 완성

# N= int(input())
# if N%2==0:
#     print("짝수")
# else:
#     print("홀수")
#% mod -어떠한 수를 나누고 난 후의 나머지 && 홀수 인지 짝수인지 && 어떤수의 배수인지 아닌지

# 5%3= 2
# 5%8= 5

# 6%2= 0
# 5%2= 1
# 4%2= 0

# a = int(input())
# if a%3 == 0:
#     print('a는 3의 배수')
# else:
#     print('a는 3의 배수가 아니다')

#for문
# 반복문 for, while문

# 가독성for 무한루프 while

# # 을 100번 출력
# #print ('#") *100
#
# for _ in range(10):
#     print("#",end='')
#
# for i in range (1,11):
#     print(i,end='')
#
# # while 조건:
# #     조건이 참인 경우 실행
#
# x=0
# while x<10:
#     print('#',end='')
#     x+=1
#
# i = 1
# while i <= 10:
#     print(i, end='')
#     i+=1

numbers=[1,2,3,4,5,6,7,8,9]
#리스트 홀수 만 찾아서 그값을 출력해 주세요

for i in range(9):
    if numbers[i]%2==1:
        print("%d은(는) 홀수입니다"%numbers[i])

#w while 문
# x= 0
# while(x<len(numbers)):
#     if numbers[x]%2==1:
#         print(f'{number}은(는) 홀수입니다')
#         x+=1
def abc(): # 함수를 정의 한다. def 함수이름():
    print(" ()    ()")
    print("(       )")

abc()     # 함수를 호출한다.
# 내장함수 리스트 길이 구할때 len
# 외장함수 import
# 사용자함수 방금 토끼 출력하는 함수를 직접 만들었음

import math  #모듈 !! 변수 함수 클래스들을 모아 놓은 파일
a= 3.14
b= math.ceil(a)
print(b)

import random
food =['빵','죽','치킨','오리탕','창평국밥']

#랜덤하게 1개를 뽑도록 하겠습니다.

lunch= random.choice(food) #랜덤하게 값을 1개 뽑을때 사용
print(lunch)

dinner= random.sample(food,k=2)#랜덤하게 값을 여러개 뽑을 때 사용 sample 사용시 중복 없음
print(dinner)

breakfast= random.choices(food,k=3)#랜덤하게 값을 여러개 뽑을 때 사용 choices사용시 중복 가능
print(breakfast)
