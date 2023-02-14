lst = list(map(str,input()))
count = 0
def abc (lev):
    global count
    if lev == 4:
        count+=1
        return
    for i in range(4):
        if lst[i] == 'B' and lst[i+1]=='T':continue
        if lst[i] == 'T' and lst[i + 1] == 'B': continue
        abc(lev+1)
abc(0)
print(count)