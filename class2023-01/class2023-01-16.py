# 메모리 -cs컴지식
# include<iostream> = c++
# include<stdio.h> = c언어
# a=7
# b=a
# print(id(a))
# print(id(b))
# 변수
# a=3
# b=5
# print(f'{a} + {b} = {a+b}입니다')

# swap
#
# a=3
# b=5
#
# a,b=b,a
#
# temp =a
# a=b
# b=temp

# # 자료형
# a=3
# print(type(a))
# a=3.14
# print(type(a)) #float형 (실수= 소수점 없는것)
# print(round(a,1))
# print(f'{a:.1f}')
#
# a=5
# a=str(a)
# print(type(a))
#
# print('오늘은 "100%"입니다')
#
# #slicing
#
# s="abcdefg"
# print(s[:3])
# print(s[3:])
# print(s[2:5])
# print(s[5:2:-1])# 5 4 3 fed
# print(s[1:5:2])# b d
# a,b=0,-1
# a,b=bool(a),bool(b)
# print(a,b)

# #리스트
# lst=[1,2,3,4,5]
# print(lst)
# print(*lst)
# print(type(lst))
# print(lst[1])
# print(len(lst))
# print(lst[-1])

# #tuple
# tp=(1,2,3,4,5)
# print(tp)
# print(type(tp))
# print(len(tp))
# print(tp[-1])

#range

# print(list(range(3)))
# print(list(range(1,5)))

#set - 리스트에서 중복된것 제거
lst =[2,1,3,4,2,1,2,4,2,1,24]
lst = list(set(lst))
# 라이브
# 복습 (꼭 직접 타이핑 하기)
# 온라인 실습
# 시간 남으면 과제까지
# 여기까지 다했으면
# 자기공부 또는 민코딩
s={1,2,3,4,5}
s.add(6)
print(s)
s.update([11,12,8,7])
print(s)
s.remove(6)#삭제하려고하는 대상에 삭제하려는 값이 없으면 버그
print(s)
s.discard(12)#discard는 값이 없어도 버그 안남
print(s)
s.clear()#다삭제
print(s)
#집합
s1=[1,2,3,4,5]
s2=[2,4,6,8]

#교집합
s1,s2=set(s1),set(s2)
print(s1&s2)
#합집합
print(s1|s2)
print(s1.union(s2))
#차집합
print(s1-s2)