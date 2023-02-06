from collections import Counter
lst =['apple','banana','mango','mango','apple']

# counter 는 리스트 안에 중복된 데이터가 각각 몇개씩 있는지 알려줌

print(Counter(lst))

ret =dict(Counter(lst))
print(ret)

st = 'an apple mango'

ret =dict(Counter(st))
print(ret)
ret = sorted(ret.items(),key=lambda x:x[1],reverse=True)
print(ret[0])

# st요소를 세어, 최빈값 n개를 반환한다.
st = 'an apple mango'
ret = Counter(st).most_common(3)
print(ret)

#추가적으로 conter를 가지고 덧셈 뺄셈도 지원합니다.
a= Counter('apple')
b= Counter('mango')
print(a+b)
print(a-b)

# 두 문자열을 대조할때 사용도 가능
a.subtract(b)
print(a)