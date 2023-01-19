# 함수 : 기능을 분해하고 재사용 가능하게 만들고
# 명시적인 return 값이 없는 경우 = void function
# 함수 실행후 , return문을 통해 값 반환
# return을 하게 되면, 값 반환 후 함수가 바로 종료
# print vs return
# print 를 사용하면 호출될때마다 값이 출력됨 (주로 테스트를 위해 사용)
# 데이터 처리를 위해서는 return사용
# local 함수가 호출되고 함수가 종료되면 사라진다
# enclosed function locals
# global 하나의 파이썬 파일 이라고 생각
# built-in 파이썬이 실행된 이후부터 영원히 유지


# filter
# 리스트나 튜플과 같은 순화 가능한 데이터구조 값들을 함수에 적용하는데
# 적용후 값중 True만 변환 !!! filter 라는 객체로 변화
#
# 리스트에서 짝수만
# num = [1,2,3,4,5]
#
# def get_even(t):
#     return True if t%2==0 else False
#
# result = filter(get_even,num)
# print(list(result))

# lambda
# 익명함수.. 함수를 간략하게 적기 위해서 사용!!

# 숫자 2개 입력받고 getsum 함수로 전달
# get sum 함수에서 전달받은 두수의 합을 리턴함
# 리턴 받은 값 출력하기

# def getsum(a,b):
#     return a+b
# ret = getsum(3,5)
# print(ret)

# result = (lambda a,b:a+b)(3,5)
# print(result)
#
# sum2=(lambda a,b:a+b)
# print(sum2(3,5))
#
# lst1=[1,2,3,4,5]
# lst2=[6,7,8,9,10]
#
# # 두 리스트 값들의 합을 lst3에 람다 함수를 사용하여 값을 채운후 출력
# lst3=map(lambda a,b:a+b,lst1,lst2)
# print(list(lst3))
#
# lst = list(range(100))
# # 리스트에서 짝수만 빼오기
# # filter + lamda
#
# lst2 = filter(lambda even:even%2==0, lst)
# print(list(lst2))
# 순환 가능한 데이터 구조에 일괄 적용 = map
# 데이터에 일괄적용하는데 True값만 따로 저장하겠다. = filter
# lambda 익명함수(사용자 함수를 직접 적지 않고 간단하게 함수를 사용하고 싶을때 사용)


# recursion 재귀!! 재귀호출
# 함수가 하나 있는데 함수 자기가 자기자신을 계속 호출!!


#1 2 3 4 5 6 7 8 9 10 10 9 8 7 6 5 4 3 2 1
# def abc():
#     abc()
#
# abc()

# for i in range(1,11):
#     print(i,end='')
# for i in range(10,0,-1):
#     print(i,end='')
#
    # ---------------------
# def abc(level):
#     print(level,end=' ')
#     if level == 3:
#         print(level,end=' ')
#         return
#     abc(level+1)
#     print(level,end=' ')
#
# abc(1)
# ---------------------------
# 문자열
# 리스트 튜플 딕셔너리 셋 관련 메소드
# copy (깊은복사 얕은 복사)
# ___________________________
# 문자 'a'가 존재하는지 확인하고자 합니다.
st= 'apple,banana,mango'
index = st.find('a',1) # 없으면 -1 값 반환
print(index)

alpha=st.index('p') # 없으면 버그!!
print(alpha)
# 대소문자 확인
st='apple,banana,mango'
print(st.isupper())#대문자 구분
print(st.islower())#소문자 구분
print(st.isalpha())#알파벳 구분

print(st.count('a'))#문자열의 갯수 구하기
# join (합치기)
st = ['a','p','p','l','e']
st2 =''.join(st)#안에는 구분자를 넣는다
print(st2)
#리스트안에 문자를 압치는데 사이사이에 ,를 넣어라
st2 =','.join(st)
print(st2)

st=['apple','banana','mango']
st2=','.join(st)
print(st2)

#모두 대문자로 바꾸기
#모두 소문자로 바꾸기
st ='apple,banan,mango'
str2=st.upper()
print(str2)
str2 = str2.lower()
print(str2)

# 공백지우기
st= '    apple'
st2=st.lstrip() #왼쪽 공백 지우기 오른쪽은 rstrip
print(st2)
st='     apple     '
str2=st.strip()# 양쪽 공백 지우기
print(str2)
#교체 replace
st='apple'
str2 =st.replace('ap','mp')
print(str2)

#리스트 값 추가
st =['apple','banana','mango']
st.append('orange')
st.insert(1,'orange')
print(st)

st=[1,2,3]
str2=[4,5]
print(st+str2)
st.extend(str2) # 리스트 더하는거
print(st)

st=[1,2,3]
#리스트 값 지우기

st.pop()
print(st)

st=[1,2,3,4,1,2,3,4]
st.remove(4)
print(st)
st=[1,2,3,4,1,2,3,4]
del st[3:]
print(st)

st=[1,2,3,4,1,2,3,4]

st.reverse()
print(st)
print(st[::-1])

# sort
a1 = [6,3,9]
print(a1)
a1.sort() #오름차순 디폴트
print(a1)
a1.sort(reverse=True)#내림차순
print(a1)
a1 = [6,3,9]
ret=sorted(a1) #원본 데이터 값 유지 (sort랑 다른점)
print(a1,ret)
ret= sorted(a1,reverse=True) # 내림차순
print(ret)

#lambda 를 이용한 sort
lst=list(range(10))
print(lst)
ret=sorted(lst,key=lambda x:x)# ret=sorted(lst)와 같다
ret=sorted(lst,key=lambda x:x,reverse=True)# 내림차순 정석 (문자건 수자건 다 잘 작동)
ret=sorted(lst,key=lambda x:-x)#내림차순


lst = [(3,'banana'),(2,'apple'),(1,'carrot')]
ret=sorted(lst,key=lambda x:x[1])
print(ret)

#딕셔너리
st = {'kevin':1,'jhon':2,'bob':3}

# 딕셔너리(key랑value)값 추가하기
st['kate']='hi'
print(st)

st['kevin']=11
print(st)

del st['kate']
print(st)

lst=st.keys()# 리스트화를 따로 시켜줘야함
print(list(lst))
lst=st.values()
print(list(lst))

lst=st.items()
print(list(lst))# 튜플의 형태로 (key,value)변환

#딕셔너리 값 출력하기
st = {'kevin':1,'jhon':2,'bob':3}
print(st.get('kevin','값 없음 '))# 값없으면 반환값도 지정 가능

#딕셔너리 값 정렬하기
st = {'kevin':27,'jhon':22,'bob':35}
#아이들의 나이가 적은 순으로(오름차순으로) 딕셔너리를 정렬하기!!
ret=dict(sorted(st.items(),key=lambda x:x[1]))
print(ret)


#리스트 copy
a=5
b=a
print(b)

lst=[1,2,3]
lst2=lst
lst[0]=100
print(*lst2)

lst=[1,2,3]
# lst2=lst.copy() # 얕은복사
lst2=lst[:]#위처럼 쓴거랑 똑같은 개념
lst[0]=100
print(lst2)

lst=[[1,2],[3,4]]
lst2= lst[:] #copy()
#얕은 복사이후
lst[0][0]=100
print(lst2[0][0])
#깊은 복사
import copy
lst=[[1,2],[3,4]]
lst2=copy.deepcopy(lst)
lst[0][0]=100
print(lst2[0][0])

# 주소값을 찍어보자
a=5
b=5
print(id(a),id(b))

lst=[1,2,3]
lst2=lst
print(id(lst),id(lst2))

lst=[1,2,3]
lst2=lst[:]
print(id(lst),id(lst2))

lst=[[1,2],[3,4]]
lst2=lst[:]
print(id(lst),id(lst2))

print(id(lst[0]),id(lst2[0]))

import copy
lst= [[1,2],[3,4]]
lst2= copy.deepcopy(lst)
print(id(lst[0]),id(lst2[0]))