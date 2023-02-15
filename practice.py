lst = [list(map(int,input().split()))for i in range(3)]
resultx=[]
resulty=[]
for i in range(3):
    resultx.append(lst[i][0])
    resulty.append(lst[i][1])
if len(set(resultx))==3 and len(set(resulty))==3:
    print('안전')
else:
    print('위험')

