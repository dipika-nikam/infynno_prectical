import re
string =input('enter')
check = re.match('[0-9]{3}\-[0-9]{3}\-[\d]{4}',string)
print(check)