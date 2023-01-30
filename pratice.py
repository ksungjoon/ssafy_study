# 1
# N = int(input())
#
# lst=[]
#
# for i in range(1,N+1):
#     if N%i==0:
#         lst.append(i)
# sorted(lst)
# print(lst)
#
# 2
# a_lst=list(map(int,input().split()))
# a_sum=0
# for i in a_lst:
#     a_sum+= i
# print(a_sum)
#
# 3
# dic=[{'name':'kim','age':12},{'name':'lee','age':4}]
# dic_sum=0
# for i in range(len(dic)):
#     dic_sum+=dic[i]['age']
# print(dic_sum)
#
# 4
# lst = [[1],[2,3],[4,5,6],[7,8,9,10]]
# def all_list_sum(a):
#     all = 0
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             all += a[i][j]
#     return all
# print(all_list_sum(lst))
#
# 5
#
# lst=[83,115,65,102,89]
# def get_secret_word(a):
#     result= ""
#     for i in a:
#         result+=chr(i)
#     return result
#
# print(get_secret_word(lst))
#
# 6
#
# def get_secret_number(a):
#     result = 0
#     for i in a:
#         result += ord(i)
#     return result
# print(get_secret_number('happy'))
#
# 7
#
# def get_strong_word(a,b):
#     a_sum=0
#     b_sum=0
#     for i in a:
#         a_sum += ord(i)
#     for j in b:
#         b_sum += ord(j)
#     if a_sum > b_sum:
#         return a
#     elif b_sum > a_sum:
#         return b
#     elif a_sum==b_sum:
#         return a,b
#
# print(get_strong_word('delilah','delilah'))
#
# user_data1 = {
#     'id': 'jungssafy5',
#     'password': '1q2w3e4r',
# }
# print(user_data1['id'][-1])
# for i in range
# def one ():
#     a = int(input())
#     return a
# def two():
#     b = str(input())
#     return b
# print(one(),two(),sep='')
#
# lst = [[' ']*3 for _ in range(3)]
import random


# 나의 국적은 대한민국
#
# class Calculator:
#     def __init__(self,first,second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def substract(self):
#         result = self.first - self.second
#         return result
#     def multuply(self):
#         result = self.first * self.second
#         return result
#     def divde(self):
#         try:
#             result = self.first / self.second
#             return result
#         except ZeroDivisionError:
#             print('0으로 나눌 수 없습니다.')
#
# a= Calculator(1,2)
# b= Calculator(2,1)
# c= Calculator(3,4)
# d= Calculator(4,0)
# print(a.add())
# print(b.substract())
# print(c.multuply())
# print(d.divde())


# class ClassHelper:
#     import random
#     def __init__(self,lst):
#         self.lst = lst
#     def pick(self,n):
#         return random.sample(self.lst,n)
#
#     def match_pair(self):
#         match_list = self.lst[:]
#         random.shuffle(match_list)
#         result = []
#         while match_list:
#             if len(match_list) > 3:
#                 pair = [match_list.pop(0), match_list.pop(0)]
#             else:
#                 pair = match_list[:]
#                 match_list.clear()
#             result.append(pair)
#         return result
#
# ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])
# print(ch.pick(1))
# print(ch.pick(1))
# print(ch.pick(2))
# print(ch.pick(3))
# print(ch.pick(4))
#
# print(ch.match_pair())

# class Doggy:
#     num_of_dogs = 0
#     birth_of_dogs = 0
#     def __init__(self,name,sort):
#         self.name = name
#         self.sort = sort
#         Doggy.birth_of_dogs += 1
#         Doggy.num_of_dogs += 1
#     def bark(self):
#         return (f'{self.name}는 짖는다.')
#
#     def get_status(self):
#         return(f'태어난 개 숫자:{self.birth_of_dogs},현재있는 개 숫자:{self.num_of_dogs}')
#     def del_dog(self):
#         Doggy.num_of_dogs -= 1
#         del self
#
# dog1 = Doggy('뽀삐','포메')
# dog2 = Doggy('초록','골든리트리버')
# dog3 = Doggy('노랑','진돗개')
# dog4 = Doggy('빨강','시바')
# print(dog2.bark())
# dog2.del_dog()
# print(dog4.get_status())

# lst = [['0']*5 for _ in range(5)]
# a,b = map(str,input().split())
# for i in reversed(range(5)):
#     lst[int(a)-1][i] = b
#     new_b = ord(b)+1
#     b = chr(new_b)
# for i in range(5):
#     print(*lst[i],sep='')

N = input()

print(f'{len(N)}글자')