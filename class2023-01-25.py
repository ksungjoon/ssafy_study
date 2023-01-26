# 주어진 문자열에서 숫자,문자,기호가 각각 몇개 인지를 판단하는 함수를 작성해 보세요
def check(input_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in input_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    return (char_count,digit_count,symbol_count)

    pass


input_str = "123$4#$!@dlksdkl_fsk"
char_count, digit_count, symbol_count = check(input_str)
print(f'char:{char_count},digit:{digit_count},symbol:{symbol_count}')
#문자:10개, 숫자 :2개 기호 :7개