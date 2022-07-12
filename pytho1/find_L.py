import re
string = ' I like coffee but I always date to tea.'
check = re.findall('I | i',string)
print(len(check))