# lst1  = list(map(int,input().split()))
# lst2 = [[0]*3for i in range(2)]
# a = 0
# Max = 0
# Min = lst1[0]
# for i in lst1:
#     if Max < i:
#         Max = i
#     if Min > i:
#         Min = i
# for j in range(2):
#     for k in range(3):
#         lst2[j][k] = lst1[a]
#         a += 1
#         if lst2[j][k] == Max:
#             print(f'({j},{k})')
#         if lst2[j][k] == Min:
#             print(f'({j},{k})')
map1 =[[3,55,42],[-5,-9,-10]]
pix = [list(map(int,input().split()))for i in range(2)]
def findnum(value):
      for i in range(2):
            for j in range(3):
                  if map1[i][j]==value:
                        return 1
      return 0

for i in range(2):
      for j in range(2):
            ret=findnum(pix[i][j])
            if ret:
                  print('Y',end=' ')
            else:
                  print('N',end=' ')
      print()