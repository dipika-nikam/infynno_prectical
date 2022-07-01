string =input("enter string ")

open_tup = tuple('({[')
close_tup = tuple(')}]')
m = dict(zip(open_tup, close_tup))
q = []

for i in string:
    if i in open_tup:
        q.append(m[i])
    elif i in close_tup:
        if not q or i != q.pop():
            print('Unbalanced')
        break
if not q:
    print('Balanced')
else:
    print('Unbalanced')
