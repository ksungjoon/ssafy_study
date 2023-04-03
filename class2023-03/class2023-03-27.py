# def perm(i,k):   # i 값을 결정할 자리, k 결정할 개수
#     if i == k:
#         print(*p)
#     else:
#         for j in range(i,k):  # 자신부터 오른쪽원소들과 교환
#             p[i],p[j]=p[j],p[i]
#             perm(i+1,k)
#             p[i],p[j]=p[j],p[i]
#
# p  = [1,2,3]
#
# perm(0,3)



# def perm (i, k):
#     if i == k:
#         print(*p)
#     else:
#         for j in range(k):  #사용하지 않은 숫자를
#             if used[j] == 0: # used에서 순서대로 검색
#                 p[i] = A[j]
#                 used[j] = 1 # j번 자리 숫자 사용으로 표시
#                 perm(i+1,k)
#                 used[j] = 0 # j번 자리 숫자를 다른 자리에서 쓸수 있게
#
# A = [1,2,3]
# p = [0] * 3
# used = [0] * 3
#
# perm(0,3)