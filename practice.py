arr = [[0,0,1,1,0,1],
       [0,0,0,1,1,1],
       [0,0,0,0,1,1],
       [0,0,0,0,0,0],
       [1,0,0,0,0,1],
       [0,0,0,0,0,0]]
used = [0]*6
def abc(lev):
    if lev ==5:
        return
    print(lev, end=' ')
    for i in range(6):
        if arr[lev][i]==1:
            if used[i]==0:

                used[i]=1
                abc(i)
abc(0)