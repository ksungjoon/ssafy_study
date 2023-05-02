# M,N = map(int,input().split())
# lst1 =
# for i in range(N):
lst = input().split('-')
result = 0
a= []
for i in range(0,len(lst)):
    if '+' in lst[i]:
        a = lst[i].split('+')
        for j in a:
            if i==0:
                result+=int(j)
            else:
                result-=int(j)
    else:
        if i==0:
            result+=int(lst[i])
        else:
            result-=int(lst[i])

print(result)