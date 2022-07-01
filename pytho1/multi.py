# num = "5, +, 1,0, -, 6, 5, *, 2, +, 3, 2, /, 4"
# importing module
from operator import sub,mul,add,truediv
test_str = '5, +, 1,0, -, 6,5, *, 2, +, 3,2, /, 4 '
str_1= test_str.replace(',','')
print("The original string is : " + str(str_1))
result = []
for i in str_1:
    # print(i)
    if i=='+':
        res2 = sum(add(*map(int, ele.split('+'))) for ele in str_1.split(', '))
        result.append(res2)
        continue
    elif i =='-':
        res3 = sum(mul(*map(int, ele.split('-'))) for ele in str_1.split(', '))
        result.append(res3)
        continue
    elif i =='*':
        res1 = sum(mul(*map(int, ele.split('*'))) for ele in str_1.split(', '))
        result.append(res1)
        continue
    elif i == '/':
        res = sum(truediv(*map(int, ele.split('/'))) for ele in str_1.split(', '))
        result.append(res)
        continue

# print("The computed summation of products : " + str(res1))

#         stack.append(i)
# print(stack)
# new_stack = stack
# for m in new_stack:
#    print(m)

















# def calculate(s: str) -> int:
#    stack = []
#    summ = 0
#    sign = 1
#    i = 0
#    while i < len(s):
#       if s[i].isdigit():
#          temp = ''
#          while i < len(s) and s[i].isdigit():
#             print(i)
#             temp += str(s[i])
#             i += 1
#          summ += int(temp) * sign
#          i -= 1
#       elif s[i] == '+':
#          sign = 1
#       elif s[i] == '-':
#          sign = -1
#       elif s[i] == '(':
#          stack.append(summ)
#          stack.append(sign)
#          summ = 0
#          sign = 1
#
#       elif s[i] == ')':
#          summ = summ * stack.pop()
#          summ += stack.pop()
#       i += 1
#    return summ
# calculate(s="5, +, 10, -, 6, 5, *, 2, +, 3, 2, /, 4 ")
