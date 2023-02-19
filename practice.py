# T = int(input())
# for test_case in range(1, T + 1):
#     word = input()
#     stack=[]
#     for i in word:
#         if i == '(' or i == '{':
#             stack.append(i)
#         elif i ==')' or i =='}':
#             if len(stack) == 0:
#                 stack.append(i)
#                 break
#             elif stack[-1] == '(' and i ==')':
#                 stack.pop()
#             elif stack[-1]=='{' and i =='}':
#                 stack.pop()
#             else:
#                 stack.append(i)
#                 break
#     if len(stack)==0:
#         print(f'#{test_case} 1')
#     else:
#         print(f'#{test_case} 0')

T = int(input())
for test_case in range(1,T+1):
    word = input()
    stack = []
    for i in word:
        if i == '(' or i== '{':
            stack.append(i)
        elif i =='}' or i==')':
            if len(stack)==0:
                stack.append(i)
                break
            elif i=='}' and stack[-1]=='{':
                stack.pop()
            elif i =='(' and stack[-1]==')':
                stack.pop()
            else:
                stack.append(i)
                break
