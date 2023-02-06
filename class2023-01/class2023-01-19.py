# 실습문제
#
# # 2-2
# st="<div>오늘은 기분이 좋아</div>"
# st=st[5:-6]
# print(st)
#
# st="<div>오늘은 기분이 좋아</div>"
# st=st[st.find('>')+1:st.find('<',1)]
#
# # 2-3
# str_lst = input().lower().split()
#
# ret = ((str_lst[0][-1] == str_lst[1][0]) and (str_lst[1][-1] == str_lst[-1][0]))
#
# if ret:
#     print('Pass')
# else:
#     print('Fail')
#
# # 2-4
# name='kevin'
# height=174
# weight=90.237
#
# print(f'{name}의 키는 {height}cm 이며 몸무게는 {weight}kg 입니다.')
# print(f'{name}의 키는 {height}cm 이며 몸무게는 {weight:.1f}kg 입니다.')
# print(f'{name}의 키는 {height}cm 이며 몸무게는 {weight:.2f}kg 입니다.')
# print(f'{name}의 키는 {height}cm 이며 몸무게는 {weight:f}kg 입니다.')
#
#
# #문자 정렬하기
# print(f'내 이름은{name}입니다.')
# print(f'내 이름은{name:>8}입니다.')
# print(f'내 이름은{name:<8}입니다.')
# print(f'내 이름은{name:^8}입니다.')
# print(f'내 이름은{name:8}입니다.') #부호가 없는 정렬은 왼쪽 정렬이 디폴트 (문자-왼쪽)
#
# #정수값 정렬하기
# print(f'키는{height}입니다')
# print(f'키는{height:>8}입니다')
# print(f'키는{height:<8}입니다')
# print(f'키는{height:^8}입니다')
# print(f'키는{height:8}입니다') #부호가 없는 정렬은 오른쪽 정렬이 디폴트 (숫자-오른쪽)
#
# height=1000000
# print(f'키는{height:>10,}입니다')
#
#
# #출력 결과 예시
# # 스테이크   50,000
# # + VAT     7,500
# # 총계 ₩    57,500
#
# steak = 50000
# VAT = int(steak * 0.15)
#
# print(f'스테이크{steak:>8,}') #스테이크가격을 우측에 정렬 후 , 넣기
# print(f'+ VAT{VAT:>10,}')
# print(f'총계 ₩{(steak+VAT):>10,}')


# # 2-5
# todo = [("Python Homework", 3), ("Essay", 4), ("Vacation", 10)]
#
# task = input("해야할 일을 입력: ")
# d_day = input("남은 일 수를 입력: ")
#
# d_integer = int(d_day)
#
# todo.append((task, d_integer))
#
# print(todo)

# # 3-1
# fruit = 'apple,rottenBanana,apple,RoTTenorange,Orange'
# fruit=fruit.lower()
# fruit=fruit.replace('rotten','')
# new_fruit=fruit.split(',')
# print(new_fruit)


# # 3-2
# word=input('문자열을 입력받아 주세요:')
# num=len(word)//2    #문자열의 길이를 구한후 절반찾기
# if len(word)%2:    #문자열의 길이가 홀수 일때!!
#     mid=word[num]  # 가운데 글자 출력
# else:
#     mid=word[num-1:num+1]
# print(mid)

# # 3-3
#
# infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
# sum = 0
# for i in range(len(infos)):
#     sum += infos[i]['age']
# print(sum)

# # 3-4
#
# blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
# dic={}
#
#
# dic2={'kevin':1}
# # kevin의 값을 2로 바꾼다면?
# # dic2['kevin']=2
#
# #bob을 dic2에 등록을 한다면?
# # dic2['bob']=4
#
#
# # dic.get(key)  하면 value가 반환 되지요~
# for i in blood_types:
#     if dic.get(i,0):
#         dic[i]+=1
#     else:
#         dic[i]=1
#
# print(dic)