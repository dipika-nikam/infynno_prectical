import re
code = input('enter code')
check = re.match('[0-9]{6}',code)
check2 = re.match('[0-9]{5} +[0-9]{4}',code)
print(check)