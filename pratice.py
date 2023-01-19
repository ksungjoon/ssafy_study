#sw 중문제

# T= int(input())
# result=[]
# for i in range(T):
#     a = int(input())
#     b=[]
#     for i in range(a):
#         b.append(list(map(str,input().split())))
#     for i in range(a):
#         print(b[2][0]+b[1][0]+b[0][0])
#
#     print(f'#{i+1}')
#     print()
# 필터써보기
# -----------------------------------

stake = 50000
vat = 0.15
print(f"""stake{stake:>8}
+VAT{round(vat*stake):>8}
총계￦{round(stake*vat+stake):>8}
""")

print(}')