import re
email = input('enter email')
check= re.match('^[a-z0-9-_]+@[a-z0-9]+\.[a-z].*$',email)
print(check)