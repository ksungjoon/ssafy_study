from collections import deque
R,C = map(int,input().split())
lst = [list(map(str,input().split()))for i in range(R)]
drx=[0,-1,1,0]
dry=[-1,0,0,1]