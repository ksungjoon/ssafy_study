# # 문제
# 10 70 110 원짜리 동전이 있다
# 거슬러 줄 돈을 입력 받은 후
# 최소 몇개의 동전을 사용하여 거슬러 줄 수 있는지 출력해 주세요
#
# # 설계
# 1. dp 테이블 셋팅 후 (2차원 배열)
# 2. "사용할 동전"으로 딱 나누어 질 때 -> 나눈 몫으로 값넣기
#                   딱 나누어 지지 않을 떄(나머지가 있을때) ->
#                   2-1 몫이 0일떄 (동전값이 너무 크다면) 윗줄에서 구한 값 넣기
#                   2-2 몫이 0이 아닐떄 (동전값이 너무 큰 것이 아니라면)
#                          윗줄에서 구한 값 vs 몫+그줄에서 구한 나머지의 최대치를 비교해서 적은값 넣기
#

# 구현
coin=[10,70,110]
n=int(input())
arr=[[0 for _ in range(n+1)] for _ in range(3)]  #dp 배열 만들기
for i in range(3): # 동전의 개수만큼 for문 돌리기
    for j in range(n+1): # j는 dp테이블의 너비를 뜻함
        mok=j//coin[i]
        if j%coin[i]==0:    # 나누어 질떄
            arr[i][j]=mok
        else:
            if mok==0:
                arr[i][j]=arr[i-1][j] # 윗줄에서 구한 값
            else:
                arr[i][j]=min(arr[i-1][j],mok+arr[i][j%coin[i]]) # 최소값 (윗줄에서 구한값 vs 몫+그줄에서 구한 나머지의 최대치를 비교해서 적은값 넣기)

print(arr[2][n])







# 내가 푼 문제
# n = int(input())
# lst = [70,20,10]
#
# result=[]
# for i in range(len(lst)):
#     a= n
#     cnt = 0
#     for j in range(i,len(lst)):
#         if a//lst[j]!=0:
#             cnt += a//lst[j]
#             a = a % lst[j]
#         if a == 0:
#             result.append(cnt)
#             break
# print(min(result))