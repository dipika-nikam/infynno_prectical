import re

string ='at.widge.list.makeview(listview.java:1727)'
grou= re.findall('([a-z]+)\(([\w\.]+):([0-9]+)\)',string)
print(grou)