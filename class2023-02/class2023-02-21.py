# 트리의 순회
#           A
#       B       C
#   D      E  F    G
# preorder전위 순회 : ABDECFG
# postorder후위 순회: DEBFGCA
# inorder 중위순회: DBEAFCG
# arr=' ABCDEFG'
#
# def preorder(now):
#     if now>len(arr)-1: return
#     print(arr[now],end=' ')
#     preorder(now*2)
#     preorder(now*2+1)
#
# def postorder(now):
#     if now > len(arr) - 1: return
#     postorder(now * 2)
#     postorder(now * 2 + 1)
#     print(arr[now], end=' ')
#
# def inorder(now):
#     if now > len(arr) - 1: return
#     inorder(now * 2)
#     print(arr[now], end=' ')
#     inorder(now * 2 + 1)
#
# preorder(1)   # 전위순회
# print()
# postorder(1)  # 후위순회
# print()
# inorder(1) # 중위순회

# BST
# 검색을 빠르게 하는 대표적인 알고리즘으로
# BST와 HASH가 있습니다
# BST는 로그N의 속도로 검색을 가능하게 하지만
# 입력되는 데이터가 좋지 않을시 최악의 경우
# 오더N의 속도가 날 수도
# print(있습니다)이때 발란스드 트리로 만들어 주는 알고리즘을
# 적용하여 로그N의 속도로 탐색이 가능하게끔 하는 과정이 필요합니다
# REDBLACK TREE
# 이분 탐색 트리
# lst =4 7 2 9 3 1 6
# 데이터가 좋아 최선 탐색 시간복잡도 O(logn) 최악 O(N)

# lst =[4,7,1,9,3,1,6]
# arr = [0]*10
#
# def insert(target):
#     now = 1
#     while 1:
#         if arr[now]==0:    # 루트노드가 비어있다면(맨처음을 뜻함)
#             arr[now]=target
#             return
#         if arr[now]<target:
#             now =now*2+1
#         else:
#             now=now*2
# def search(target):
#     now =1
#     while 1:
#         if now>20 : return 0  # now가 배열의 범위를 벗어나면 없다는 의미니깐 0리턴
#         if arr[now] ==0:   # 타겟이 없으면 0리턴
#             return 0
#         if arr[now]==target:# 타겟을 찾으면 1리턴
#             return 1
#         if arr[now]<target:
#             now=now*2+1
#         else:
#             now=now*2
# # 트리의 모양을 만들고 찾는 속도 O(logN)속도
#
# for i in range(len(lst)):
#     insert(lst[i]) # 트리의 모양으로 lst값을 저장
# n= int(input())
# ret =search(n)
# if ret ==1 :
#     print('존재함')
# else:
#     print('존재하지 않음')

# HEAP
# 항상 완벽한 이진트리의 형태로 저장하고
# 출력할때 logN의 속도로 출력 한다.

# 코드 구현
arr = [3,7,1,4,7,31,8]
heap = [0]*30  # MAX HEAP
hindex = 1 # 1번 인덱스에 첫값 저장 하기 위함

def insert(value):
    global hindex
    heap[hindex] = value
    now = hindex
    hindex += 1

    while 1:
        p = now//2    # 부모 인덱스 구하기
        if p==0: break# 만약에 부모 인덱스가 0이라면 (now는 루트노드)비교할것 없음 꺼버림
        if heap[p]>=heap[now]: break # 부모와 now값 비교해서 부모가 크거나 같으면 꺼버림
        heap[p], heap[now] =heap[now],heap[p] # 부모값<now값 이라면 swap
        now =p # 부모가 그다음의 now가 됨(부모가 부모의 부모(그 조상과)와 비교를 실행)
def top():
    return heap[1]
def pop():
    global hindex
    heap[1]=heap[hindex-1] # 맨뒤에 아이를 루트로 올리고
    heap[hindex] =0 # 맨 뒤에 값을 0으로 바꾸고
    hindex -=1 # hindex 값 감소
    now = 1 # 루트부터 자식들이랑 비교하기 위해서 now를 1로 셋팅
    while 1:
        son = now*2 # 왼쪽자식
        rson= now*2+1 # 오른쪽 자식
        #자식이 있고 오른쪽 자식이 왼쪽 자시복다 크면(오른쪽 자식과 now랑 비교하겠다)
        if son <= hindex and heap[son]<heap[rson]:
            son =rson
        # 자식이 엇거나 부모가 자식이 더크다면 break
        if son>hindex or heap[now] >heap[son]:
            break
        heap[now],heap[son]=heap[son],heap[now]
        now =son

for i in range(len(arr)):
    insert(arr[i])
for i in range(len(arr)):
    print(top(),end=' ')
    pop()