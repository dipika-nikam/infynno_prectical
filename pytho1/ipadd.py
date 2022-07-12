import re

add = input('enter ip address')
check = re.findall('(([0-2][0-5][0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}([0-2][0-5][0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',add)
print(check)
if check:
    print('valid IP')
else:
    print('invalid')
