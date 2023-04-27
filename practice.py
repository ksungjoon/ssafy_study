N=int(input())
M=input()

for i in range(2,-1,-1):
    print(N*int(M[i]))
print(int(M)*N)