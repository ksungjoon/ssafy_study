lst = [list(map(int,input().split()))for i in range(5)]
directy = [-1, -1, -1, 0, 0, 1, 1, 1]
directx = [-1, 0, 1, -1, 1, -1, 0, 1]
def state(y,x):
    for i in range(8):
        dy = y+directy[i]
        dx = x+directx[i]
        if dy<0 or dx<0 or dy>4 or dx>3: continue
        if lst[dy][dx]==1:
            return 1
    return 0

def state2():
    for i in range(5):
        for j in range(4):
            if lst[i][j]==1:
                if state(i,j) == 1:
                    return 1
    return 0
if state2() ==1:
    print('불안정한 상태')
else:
    print('안정된 상태')
#
# map1 = [[3,5,1],[3,8,1],[1,1,5]]
# lst = [list(map(str,input()))for i in range(2)]
# max = 0
# for i in range(2):
#     for j in range(2):
#         if lst[i][j]==
