# a = {'사과','바나나','수박'}
# print(a.clear())
# print(a)
#
# sample_list = [11,22,33,55,66]
#주어진 리스트인 4번째 짜리에 있는 항복을 제거하고 변수에 할당해주세요ㅗ
import copy

# elem = sample_list.pop(3)
# print('list after:',sample_list)
# print('elem:',elem)

#주어진 sample_list의 가장뒤에 44를 추가해보세요

# sample_list.append((77))

# 할당해놓은 변수의 값을 sample_list의 2번 index에 추가해보세요

# sample_list.insert(2,elem)
# print(sample_list)

#tuple

# my_tuple = (11,22,33,44,55,66)
#주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당해보세요.
# new_tuple  = my_tuple[3: -1]
# print(new_tuple)

# 깊은 복사하는법  import copy
# copy.deepcopy()
# deepcopy 안쓰고 깊복 하는법
a=[1, 2, ['a' ,'b']]
b=a[0:2]+[a[2][:]]
b[0]= 0
print(a,b)

# test_list = [1,2,3,8,2,4,7]
# test_list.sort()
# print(test_list)
#
scores = [('eng',88),('sci',90),('math',80)]
# def check(x):
#     return x[1]
# print(scores)
# scores.sort(key=check)
scores.sort(key=lambda x: x[1] )
print(scores)