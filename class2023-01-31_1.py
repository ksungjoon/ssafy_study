# 클래스 매서드
# 데코레이터
# @ 데코레이터(함수명)형태

# name = input()
# def ko_hello(a):
#     print(f'안녕하세요 {a}님!')
#
# def en_hello(a):
#     print(f'Hello, {a}!')
#
# ko_hello(name)
# en_hello(name)
#
# def emoji_hello(a,func):
#     func(a)
#     print('^~^//')
#
# emoji_hello(name,ko_hello)
#
# def emogi_decorator(func):
#     def wrapper(name):
#         func(name)
#         print('^~^//')
#
#     return wrapper
#
# emogi_decorator(ko_hello)('성준')
#
# class MyClass:
#
#     def method(self):
#         return 'instance method',self
#     @classmethod
#     def classmethod(cls):
#         def classmethod(cls)
#             return 'class method',cls
#

# 객체지향 프로그램이 핵심 개념
# 객체 지향의 핵심 개념
# 추상화 상속 다형성 캡슐화

# 추상화
# 현실 세계를 프로그램 설게에 반영

# 상속
# 두 클래스 사이 부모 - 자식 관계를 정립하는 것
# 클래스는 상속이 가능함
# 모든 파이썬 클래스는 object를 상속받음
# 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
# 부모클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐

# 다형성
# 여러 모양을 뜻하는 그리스어
# 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
# 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답할 수 있음

# 캡슐화
# 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
# 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음

# public access modifier : 모두가능
# protected access modifier : 상속관계에서만 가능
# private access modifier : 나만 가능

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print((f'반값습니다.{self.name}입니다'))
#
# class professor(Person):
#     def __init__(self,name,age,department):
#         self.name = name
#         self.age = age
#         self.department = department
# class student(Person):
#     def __init__(self,name,age,gpa):
#         self.name = name
#         self.age = age
#         self.gpa = gpa
#
# p1 = professor('김교수',35,'컴퓨터 공학과')
#
# p1.talk()

# class person:
#     pass
# class professor(person):
#     pass
# class student:
#     pass
#
# p1 = professor()
# p2 = student()
#
# print(issubclass(professor,))

class pluss_minus:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def plus(self):
        result = self.first+self.second
        return  result
    def minus(self):
        result = self.first - self.second
        return result

class morefunction(pluss_minus):
    def __init__(self,first,second,third):
        super().__init__(first,second)
        self.third = third
    def mul(self):
        result = self.first*self.second*self.third
        return result
p1 = morefunction(3,4,5)

print(p1.mul())

print(p1.plus())

# 단 자식클래스에서 생성된 메서드를 부모클래스에서 사용은 불가능

# _-------------------------------------------

# 메서드 오버라이딩
# 오버라이딩이란 덮어쓰기를 말한다.
# 부모클래스에 있는 메서드!! 를 동일한 이름으로 자식클래스에서 다시 만드는 것이다.
# (부모 클래스의 매서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용)

# 부모 클래스에서 상속받은 plus의 매소드의 기능에서
# 숫자 2개가 아닌 숫자 3개의 합이 100이 넘는다면
# '버그'라고 출력이 되도록
# 자식클래스에서 plus의 메소드 업그레이드 하려 한다고 가정하자
class morefunction(pluss_minus):
    def __init__(self,first,second,third):
        super().__init__(first,second)
        self.third = third
    def mul(self):
        result = self.first*self.second*self.third
        return result
    def plus(self):
        get_sum = self.first+self.second+self.third
        if get_sum>100:
            print('버그')
        else:
            return print(get_sum)
    def parents_plus(self):
        ret = super().plus()
        return ret
a = morefunction(1,1,99)
a.plus()
print(a.parents_plus())

print(morefunction.mro())
# 이처럼 부모클래스의 plus 매서드르
# 새롭게 다시 정의하는 것을 "매서드 오버라이딩"이라고 한다.
# 이번에는 자식클래스에서 plus 매서드를 다시 정의했지만(매서드 오버라이딩을 했지만)
# 부모 클래스에서의 plus 매서드를 자식클래스에서도 또 사용하고 싶다면
# 이때 super()를 이용할 수 있다.

# class object는 뭘 의미하는지?
# bool은 int의 자식 클래스 인게 true 인데 이것만 예외인건지?
# issubclass 뒤에 classinfo에 부모 만 있으면 무조건 참?

# -----------------------------------
# 캡슐화
# pubilc
# protected
# 암묵적 규칙에 의해 메소드를 호출시
# 부모클래스 내부나 자식클래스에서만 호출이 가능하다
# 그러나 강제성은 없으므로 실제로는 public과 거의 동일하게 외부 접근이간으하다
# (정말 막아주지는 않고 암묵적인 규칙)

# private

# getter 매소드와 setter 매소드를 만들어 사용하면 간으하다
# getter 매소드와 setter 매소드는
# 각각 property 그리고 setter라는 데코레이터를 사용한다
class person:
    def __init__(self,name,age):
        self.name =name
        self.__age = age
    def getter(self):
        return self.__age
    def setter(self,value):
        self.__age=value

k = person('kevin', 39)
print(k.getter())
k.setter(29)
print(k.getter())

# 클래스의 private한 속성값을 getter와 setter를 이용해서 확인 그리고 값 변경이 가능함
# 그 다음에는 위 코드를 조금 더 간단하게 적기 위해 데코레이터를 사용할 것이다.

# getter 매소드에는 @property라는 데코레이터를 사용하고
# setter 매소드에는 @변수.setter 로 데코레이터를 사용할 것이다

class person:
    def __init__(self,name,age):
        self.name =name
        self.__age =age
    @property   #getter 함수 위에 @property 라고 적어주고
    def age(self):
        return self.__age
    @age.setter  #메서드명.setter라고 적어준다.
    def age(self,value):
        self.__age=value  # 함수명을 같게 만들자!

k = person('kevin',39)
print(k.age)
k.age = 29
print(k.age)

# 참고로 @property 데코레이터 사용을 하면 매서드 호출시 ()를 생략해야한다
# 관례상 setter getter 함수명은 변수명을 따른다.

# 객체지향의 핵심개념(상속 추상화 캡슐화 다향성) 상추캐다
# 상속: 부모클래스, 자식클래스 관계 - 속성과 매소드를 물려받아 사용 (super통해서 부모의 요소 호출 가능)
# 추상화: 복잡한것은 숨기고, 필요한 것 나타냄(공통적인것은 부모클래스에 구현)
# 캡슐화: 객체 일부 구현 내용에 대해 외부로 부터 직접적인 액세스 차단, getter,setter
# 다형성: 동일한 매서드가 클래스에 따라 다르게 행동할 수 있음 매서드 오버라이딩.

# 에러와 예외처리

print(issubclass(bool,int))
print(type(int))
print(type(float))
print(type(bool))
print(morefunction.mro())
print(type(object()))