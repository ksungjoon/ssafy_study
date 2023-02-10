T = int(input())
def abc(a,lst):
    lst[2][2]=a
    return result


for test_case in range(1, T + 1):
    a= input()
    lst= [['..#..'],['.#.#.'],['#.a.#'],['.#.#.'],['..#..']]
    result = []
    abc(a[0],lst)
    for i in range(1,len(a)):
        result = [x+y for x,y in zip(result, abc(a[i],lst))]
    print(result)