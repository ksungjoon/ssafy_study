import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    a,n = map(str,input().split())
    lst = list(map(str,input().split()))
    dic ={}
    result = []
    for i in lst:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in range(dic['ZRO']):
        result.append('ZRO')
    for i in range(dic['ONE']):
        result.append('ONE')
    for i in range(dic['TWO']):
        result.append('TWO')
    for i in range(dic['THR']):
        result.append('THR')
    for i in range(dic['FOR']):
        result.append('FOR')
    for i in range(dic['FIV']):
        result.append('FIV')
    for i in range(dic['SIX']):
        result.append('SIX')
    for i in range(dic['SVN']):
        result.append('SVN')
    for i in range(dic['EGT']):
        result.append('EGT')
    for i in range(dic['NIN']):
        result.append('NIN')
    print(a)
    print(*result)
    # print("ZRO "*dic["ZRO"], "ONE "*dic["ONE"], "TWO "*dic["TWO"], "THR "*dic["THR"], "FOR "*dic["FOR"], "FIV "*dic["FIV"], "SIX "*dic["SIX"], "SVN "*dic["SVN"], "EGT "*dic["EGT"], "NIN "*dic["NIN"],sep='')