#
# lst = [['A','B','C'],['A','G','H'],['H','I','J'],['K','A','B'],['A','B','C']]
# bucket =[0] * 26
# result = [0]* 15
# for i in range(5):
#     for j in range(3):
#         bucket[ord(lst[i][j])-65] += 1
# for j in range(len(bucket)-1):
#     bucket[j+1] = bucket[j]+bucket[j+1]
# for i in range(5):
#     for j in range(3):
#         result[bucket[ord(lst[i][j])-65]-1] = lst[i][j]
#         bucket[ord(lst[i][j]) - 65] -= 1
# print(*result,sep='')

T = int(input())
for test_case in range(1, T + 1):
    a,b = map(int,input().split())
    lst = list(map(int,input().split()))
    result = []
    c = 0
    d = 0
    for i in range(a-b+1):
        for j in range(c,c+b):
            d += lst[j]
        result.append(d)
        d = 0
        c += 1
    y = max(result)-min(result)
    print(f'#{test_case} {y}')


