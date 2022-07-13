import re
string='<a href="https://google.com">Google</a><li>'
check = re.findall('<([^(?!\/) \d>]+)',string)
print(check)