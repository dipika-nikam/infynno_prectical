import re

add = input('enter ip address')
check = re.match(
    '^(([01]?[0-9][0-9]?)|([02][0-5][0-5]|[02][0-4][0-9]))\.(([01]?[0-5][0-9]?)|([02][0-5][0-5]|[02][0-4][0-9]){1,3})\.(([01]?[0-5][0-9]?)|([02][0-5][0-5]|[02][0-4][0-9]){1,3})\.(([01]?[0-5][0-9]?)|([02][0-5][0-5]|[02][0-4][0-9]){1,3})$',
    add)
if check:
    print('valid IP')
else:
    print('invalid')