n = int(input("Enter value"))
if n % 2 != 0:
    print('odd {}'.format(n))
else:
    print('Even {}'.format(n))

num = [1, 2, 3, 4, 5, 6, 7, 8]
odd = []
even = []
for i in num:
    if i % 2 == 0:
        even.append(i)

    else:
        odd.append(i)
print(even)
print(odd)