import re

string = """// this is a single line comment 
x = 1;
// a single line comment after code
y = 2; """
check = re.findall('.*;',string)
print(check)