
T = int(input())
for test_case in range(1, T +1):
    N = int(input())
    lst = list(map(int,input().split()))
    count_list =[]
    count = 0
    max = 0
    for i in range(N):
        for j in range(i,N):
            if lst[i] > lst[j]:
                count+=1
        count_list.append(count)
        count = 0
    for i in count_list:
        if max<i:
            max=i
    print(f'#{test_case} {max}')