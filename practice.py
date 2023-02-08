# import sys
# sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    a,n = map(str,input().split())
    lst = list(map(str,input().split()))
    dic ={}
    for i in lst:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
