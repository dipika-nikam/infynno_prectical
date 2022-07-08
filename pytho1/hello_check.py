import re
string= 'hello how are you? all good hello'
check = re.match('^hello',string)
check2 = re.match('.* hello$',string)
check3 = re.findall('hello',string)
if string:
    print(check)
elif string:
    print(check2)
else:
    print(check3)