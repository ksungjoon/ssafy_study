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
lst = [[0]*4 for _ in range(4)]
N = int(input())
for i in range(4):
    lst[i].