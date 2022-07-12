import re
string= 'hello how are you? all good hello'
check = re.match('^hello',string)
check2 = re.match('.* hello$',string)
check3 = re.findall('hello',string)
print(check)
print(check2)
print(check3)