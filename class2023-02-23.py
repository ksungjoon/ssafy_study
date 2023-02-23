# (A B) (C) (D) (E) (F) 의 각각의 독립된 data를 그룹화 시키려고 한다.
# 그룹을 어떻게 시킬지 입력 받은 후
# 최종적으로 몇개의 그룹이 존재하는지 출력하세요
#
# 4    # 그룹화를 몇번 진행 할지 입력받은후
# A E # 어떠한 data를 그룹화 시킬 것인지 정보를 입력받아 주세요.
# C F
# B D
# E A

# n=int(input()) # 그룹화 시킬 횟수 입력
# cnt=6 # 그룹화를 시키지 않은상태에서는 A<B<C<D<E<F 총 6개의 그룹이 존재 함ㅇ
# arr=[0]*200
# def findboss(m):
#     if arr[ord(m)]==0:
#         return m
#     ret=findboss(arr[ord(m)])
#     return ret
#
# def union(a,b):
#     aboss=findboss(a)
#     bboss=findboss(b)
#     if aboss==bboss:
#         return
#     arr[ord(bboss)]=aboss
#
# for i in range(n):
#     y,x=input().split()
#     if findboss(y)!=findboss(x):
#         union(y,x)
#         cnt-=1
#
# print(cnt)

# n = int(input())
# arr = [0]*200
# cnt = 6
# def findboss(m):
#     if arr[ord(m)]==0:
#         return m
#     ret = findboss(arr[ord(m)])
#     return ret
#
# def union (a,b):
#     fa,fb =findboss(a),findboss(b)
#     if fa == fb:
#         return
#     arr[ord(fb)]=fa
#
# for i in range(n):
#     x,y =input().split()
#     if findboss(y)!=findboss(x):
#         union(x,y)
#         cnt -= 1
# print(cnt)

# 크루스칼 알고리즘
# spannig tree 싸이클이 존재하지 않는 트리
# 최소 신장트리
arr=[0]*200
k=int(input())  # 정점의 개수
n=int(input())  # 간선의 정보 개수
lst=[list(input().split()) for _ in range(n)] # 간선의 정보 입력

# 설계
# 비용을 기준으로 sort

# unionfind 하는데 보스가 같으면 안하고
#                   보스가 다르면 합체 / cnt+=1 / total 비용 더하기
#cnt가 k-1개 되면 끝

lst.sort(key=lambda x:int(x[2]))

def findboss(m):
    if not arr[ord(m)]:
        return m
    ret=findboss(arr[ord(m)])
    arr[ord(m)]=ret
    return ret

def union(a,b,i):
    global total,cnt
    aboss,bboss=findboss(a),findboss(b)
    if aboss == bboss:
        return
    total += int(lst[i][2])             # 다리건설 할때 드는 비용 더하기
    cnt+=1                              # 다리 개수 1 증가
    arr[ord(bboss)]=aboss               # 다리 건설하기!

total=0   # 최소비용
cnt=0    # 다리 개수
for i in range(n):
    if cnt==k-1:            # 다리개수가 정점개수 -1 개와 같으면 출력하고 끝내기
        print(total)
        break
    union(lst[i][0],lst[i][1],i)














