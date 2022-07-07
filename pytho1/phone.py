import re
phone = input('Enter phone')
check = re.match('^\++[0-9]{1,2} +[0-9]{5} +[0-9]{5}', phone)
print(check)