import re

string='https://www.something.com/news/2016/09/02/this-is-latest-news'
check = re.findall('\d+', string)
print('/'.join(check))