T = 10
for test_case in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split()))for i in range(100)]
    cnt = 0
    for i in range(100):
        a = 0
        for j in range(100):
            if lst[j][i]==1:
                a=1
            if a==1 and lst[j][i]==2:
                cnt+=1
                a=0
    print(f'#{test_case} {cnt}')

