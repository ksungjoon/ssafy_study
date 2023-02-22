# union find
# setunion(a,b) > [0,a,0,0,0,0]
#                 [a,b,c,d,e,f]
# setunion(d,e) > [0,a,0,0,d,0]
#                 [a,b,c,d,e,f]
# setunion(b,e) > [0,a,0,a,d,0]
#                 [a,b,c,d,e,f]
# setunion(c,f) > [0,a,0,a,d,c]
#                 [a,b,c,d,e,f]
# setunion(f,e) > [c,a,0,a,d,c]
#                 [a,b,c,d,e,f]

#
# arr=[0]*200
# def findboss(member):
#     if arr[ord(member)] == 0: # 자기자신이 보스라면!!
#         return member
#     ret = findboss(arr[ord(member)])
#     return ret
#
# def setunion(a,b):
#     fa,fb = findboss(a),findboss(b)
#     if fa ==fb: # 각각의 보스를 보았는데 어! 보스가 같네.. 우리 같은 식구였어
#         return
#     arr[ord((fb))]=fa
#
# setunion('a','b')
# setunion('d','e')
# setunion('b','e')
# setunion('b','d')
# setunion('e','f')
# y,x =input().split()
# if findboss(y) == findboss(x):
#     print('같은그룹')
# else:
#     print('다른그룹')

# arr=[0]*200
#
# def findess(word):
#     if arr[ord(word)]==0:
#         return word
#     ret = findess(arr[ord(word)])
#     return ret
#
#
# def union(a,b):
#     fa,fb =findess(a),findess(b)
#     if fa==fb:
#         return
#     arr[ord(fb)]=fa
# union('a','b')
# union('d','e')
# union('b','e')
# union('c','f')
# union('f','e')
# x,y = input().split()
#
# if findess(x)==findess(y):
#     print('같은그룹')
# else:
#     print('다른그룹')


# 싸이클 발생여부 확인
# 4 ab bc be cd

# n = int(input())
# lst = [list(input().split())for i in range(n)]
# arr = [0]*200
# flag = 0
# def findess(member):
#     if arr[ord(member)]==0:
#         return member
#     ret = findess(arr[ord(member)])
#     arr[ord(member)]=ret  # 경로 단축
#     return ret
# def union(a,b):
#     global flag
#     fa,fb = findess(a),findess(b)
#     if fa == fb:
#         flag =1
#         return
#     arr[ord(fb)]= fa
#
# for i in range(len(lst)):
#     union(lst[i][0],lst[i][1])
# if flag ==1:
#     print('싸이클 발생')
# else:
#     print('싸이클 없음')

# 교수님이 짜신거거

# n=int(input())                               #4
# edge=[]
# arr=[0]*200
# for _ in range(n):
#     edge.append(input().split())            # a b  # b c  # b e  # c e (cycle 발생)
#                                             # a b  # b c  # b e  # c d (미발견)
# def findboss(member):
#     if arr[ord(member)]==0:
#         return member
#     ret=findboss(arr[ord(member)])
#     arr[ord(member)]=ret # 경로단축
#     return ret
#
# def union(a,b):
#     fa,fb=findboss(a),findboss(b)
#     if fa==fb:
#         return 1
#     arr[ord(fb)]=fa
#
# answer='미발견'
# for i in range(n):
#     a,b=edge[i]
#     ret=union(a,b)
#     if ret==1:
#         answer='발견'
#         break
print(answer)














