# 객체 지향 프로그래밍 object-oriented programming
# 컴퓨터 프로그램을 명령어 목록으로 보는 시각에서 벗어나 여러개의 독립된 단위
# 절차 지향 프로그래밍
# 프롤그램 전체가 유기적인 흐름으로 연결
# 기능 중심의 프로그램
# 순서가 정해져 있으므로 실행이 빠름- 객체 지향 프로그래밍과 다름
#
# 단점- 수정이 힘들다
#
# 하드웨어가 발점함에 따라 소프트웨어도 점점 커지고 복잡한 설계가 요구됨
# 하드웨어어의 발전속도를 소프트웨어의 발전 속도가 따라가지 못함
# 소프트웨어 위기
#
# 절차지향 방법론 *** 생산성이 너무 낮다!!!
# 절차 대신 핵심이 되는 데이터를 중심으로 생각
#
# 객체 지향 프로그래밍이란
# 프로그램을 여러개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
# 예시
# 콘서트-
# 가수 객체
# 감독 객체
# 관객 객체
#
# 객체 지향 프로그래밍
# 데이터와 기능(메서드) 분리, 추상화된 구조(인터페이스)
#
# 객체(컴퓨터 과학)
#
# 컴퓨터 과학에서 객체 또는 오브젝트는 클래스에서 정의한 것을 토대로 메모리 에 할당된 것

# 클래스 변수와 인스턴스 변수 *** 다시보기

# 메서드의 종류
# 인스턴스 메서드
# 클래스 메서드
# 정적 메서드
class person:
    count = 0
    def __init__(self,name):
        self.name =name
        person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는{cls.count}입니다')

person1 = person('아이유')
person2 = person('이찬혁')
person.number_of_population()
person1.number_of_population()

# 객체지향 프로그래밍
#
# 오늘은 객체지향 프로그래밍이 무엇을 말하는지
# 클래스 객체 인스턴스 메서드가 무엇인지
# 클래스 변수 /인스턴스 변수/
# 인스턴스 매서드
# 클래스 매서드
# 정적 매서드 (static method)
#
#
#
# 클래스 - 인스턴스 - 메서드
#
# class calculator():
#     numberOfCalcul = 0#클래스 변수
#     def __init__(self):     # 생성자함수 constructor
#         self.result = 0
#         calculator.numberOfCalcul += 1# 인스턴스 변수
#     def getsum(self,value):
#         self.result += value
#         return  self.result
# cal1 = calculator() # <--객체라고도하지만 caulculator의 인스턴스
# # 인스턴스 변수란? 인스턴스가 개인적으로 가지고 있는 속성(attribute)
# print(cal1.getsum(3))
# print(cal1.getsum(4))
# print(cal1.getsum(5))
# cal2 = calculator()
# print(cal2.getsum(6))
# print(cal2.getsum(7))
# print(cal2.getsum(1))
# # 클래스 변수란 ?
# # 한 클래스의 모든 인스턴스가 공유하는 값을 의미
# print(cal1.numberOfCalcul)
# print(cal2.numberOfCalcul)
# # 주의점 !!
# # 클래스 변수 "값을 변경시" 무조건 항상
# # 클래스.클래스 변수 형식으로 변경해야함
# calculator.numberOfCalcul = 6
# print(cal1.numberOfCalcul)
# print(cal2.numberOfCalcul)
# # _________________________________이러면 안됨
# cal1.numberOfCalcul =10
# print(cal2.numberOfCalcul)
# #cal1.numberOfCalcul =10에서 새로운 인스턴스 변수가 만들어짐
# calculator.numberOfCalcul = 20
# print(cal1.numberOfCalcul)
# print(cal2.numberOfCalcul)

# ---------------------------
# 클래스/인스턴스(객체)
#
# 클래스 - 속성/매서드
#
# 속성 - 클래스변수/ 인스턴스 변수
#
# 3. 매서드
#     1. 인스턴스 매서드
#     2. 클래스 매서드
#     3. 스태틱 매서드
# 1. 인스턴스 매서드 알아보기
#
# 생성자 함수 없이 만들기

# class plus_minus:
    # def data(self,first,second):
    #     self.first = first
    #     self.second = second
#     def __init__(self,first,second): #<--- 매직 매서드
#         self.first=first
#         self.second=second
#     def plus(self):
#         pass
#         result = self.first+self.second
#         return result
#     def minus(self):
#         pass
#         result = self.first-self.second
#         return result
#
# a= plus_minus(3,5)
# print(a.plus())
# print(a.minus())

# a= plus_minus()
# a.data(3,5)
# b = plus_minus()
# b.data(2,7)
# print(a.first,b.second)
# print(a.plus())
# print(a.minus())
# 객체 a와 b는 각각 독립적이다)
# 여기서 doata가 바로 인스턴스 매서드 이고
# 인스턴스 매서드는 self를 항상 첫번째 paremeter로 사용
# 이름이self일 필요는 없으나 관례적으로 self를 사용함

# __init__
# 매직 매서드(init zdd str등) == 인스턴스 생성하자마자 자동 호출!!
# 특수한 매서드를 사용함으로써, 파이썬의 행위를 여러가지로 커스터마이즈 할수 있다.

# 파이썬에서 문자열에서 + 연산자를 사용하면 두 문자열이 합쳐지는 것은
# 실습
# 예를들어 자동차를 생성하는 클래스를 만들고 자동차 가격의 합을
# 사용자가 쉽게 출력할 수 있도록 해보겠다.

class car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self, another):
        return  self.price + another.price
    def __str__(self):
        return (f'{self.name}의 가격은 {self.price}입니다.')

kia=car('k8',300)
bmw=car('m5',500)
print(kia+bmw)
#
# # add 라는 매직매서드를 커스터마이징 해서 덧셈 연산을 지원하도록 하겠다.
# print(kia+bmw) # 커스터마이징 할 것이다!! 이거 지금 출력하면 버그
#
#

print(kia)
print(kia,bmw)
#
# del kia # 인스턴스 삭제
# del bmw

# 클래스 매소드(데코레이터를 사용해서 정의, 호출시 첫번째 인자로 클래스가 전달됨)
# 스태틱 매소드(정적매소드)(클래스변수나 인스턴스 변수를 사용하지 않는 경우)

#데코레이터
#장식하는 사람이라는 뜻
# 함수를 하나 만드는데 그 함수를 직접 수정하지 않고 함수에 기능을 추가하고자 할때 사용

# 1.먼저 데코레이터 사용안한 예
# 이름과 나이를 출력 해 주는 각각의 함수를 정의해 보자

# def call_name(name):
#     print('반짝'*5)
#     print(name)
#     print('샤방'*5)
# def call_age(age):
#     print('반짝' * 5)
#     print(age)
#     print('샤방' * 5)
# def call_nickname(nick):
#     print('반짝' * 5)
#     print(nick)
#     print('샤방' * 5)
#
# call_name('최민호')
# call_age(39)
# ---------------------------------------------

# def deco(func):
#     def wrapping(value):
#         print('반짝'*5)
#         func(value)
#         print('샤방'*5)
#     return wrapping
#
# @deco
# def call_name(name):
#     print(name)
#
# @deco
# def call_age(age):
#     print(age)
#
# call_name('최민호')
# call_age(39)

# --------------------------------------
# 정적 매서드

class car:
    @staticmethod
    def add_price(one,another):
        print(one+another)

# 정적 매소드에는 @staticmethod를 붙입니다.
# 그리고 self가 없다!!(self는 인스턴스 메서드 사용)
# add_price 함수에 매겨변수를 넣는데 self 사용하지 않습니다.

car.add_price(400,800)
# 정적 매서드를 호출할 때는 클래스에서 바로 매서드를 호출하면 됩니다.
# 클래스의 인스턴스가 없어도 문제가 될것 없음

# 다시 한번 말하지만 정적 매서드는 인스턴스 매서드 처럼
# self를 받지 않습니다 그래서 보통 정적 매서드는
# self와 같은 속성을 다루지 않고 단지
# 함수의 행동(가능)(매서드내용만)하는 매서드를 클래스에 정의 할때 사용한다
# 그래서 호출할때 클래스에서 바로 매서드를 호출함
# car.add_price(400,800)

# 그러나
# 인스턴스가 있다면 인스턴스로도 static method에 접근은 가능
# 이것은 파이썬에서 가능!
a7 = car()
a7.add_price(500,600)
# 인스턴스로 정적매소드 호출은 잘 하지 않음 그 이유는 !!!
# 정적 매소드를 사용하는 이유!!
# 이 매소드는 클래스의 인스턴스에 어떠한 변화도 일으키지 않는
# 함수라는 의미를 내포하고 암시할때 사용한다.

# 클래스 매서드

# 몇명이 파이 만들었는지 확인하는 코드를 클래스 매서드를 사용해 보자
class make_pie:
    cnt=0
    def __init__(self,name):
        self.name=name
        make_pie.cnt += 1

    @classmethod
    def number_of_pie(cls): # cls = make_pie
        print(f'파이를{cls.cnt}명이 만들고 있습니다.')

    @classmethod
    def create(cls,name): # 클래스 내부에서 클래스안에 있는 매소드를 호출하는 함수
        p = cls(name)
        return p


a= make_pie('kevin')
b= make_pie('jane')
c= make_pie('jhon')

# @classmethod라는 데코레이터를 사용함
# 호출시 첫번째 인자로 항상 cls를 사용하고
# cls는 클래스 자체를 의미하며 바로 make_pies를 뜻함

make_pie.number_of_pie()
make_pie.create('tom')
make_pie.create('bob')
make_pie.number_of_pie()

