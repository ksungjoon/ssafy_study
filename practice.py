lst = [input()for i in range(2)]
result = ''
max = 0
answer=''
for i in range(len(lst[0])):
    result=''
    for j in range(i,len(lst[0])):
        result+=lst[0][j]
        if result in lst[1]:
            if max<len(result):
                max = len(result)
                answer=result
print(answer)
