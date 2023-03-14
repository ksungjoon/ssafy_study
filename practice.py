N = int(input())
lst = input()
Max = -21e9
first =[0]*(N//2+2)
result = int(lst[0])
def dfs(lev):
    global Max
    result = int(lst[0])
    if lev == N//2 :
        for k in range(len(lst)):
            if k%2==1:
                if first[(k+1)//2]==0 and first[(k+1)//2+1]==0:
                    if lst[k]=='+':
                        result += int(lst[k+1])
                    elif lst[k]=='-':
                        result -= int(lst[k+1])
                    elif lst[k]=='*':
                        result *= int(lst[k+1])
                elif first[(k+1)//2]==1:
                    if lst[k]=='+':
                        result += int(lst[k-1])+int(lst[k+1])
                    elif lst[k]=='-':
                        result -= int(lst[k+1])
                    elif lst[k]=='*':
                        result *= int(lst[k+1])


            return
    for i in range(1,N//2+1):
        if first[i-1]==0 and first[i+1]==0:
            first[i]=1
            dfs(lev+1)
            first[i]=0
dfs(0)