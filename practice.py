T = 10

for test_case in range(1,T+1):
    N = int(input())
    lst = [list(map(str,input()))for i in range(100)]
    a = []
    result =0
    max = 0
    for k in range(100):
        for i in range(100):
            for j in range(100-i):
                a.append(lst[k][i+j])
            if a==a[::-1]and max<len(a):
                max = len(a)
                result = len(a)
