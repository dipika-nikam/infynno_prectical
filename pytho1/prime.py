n = int(input("Enter value"))

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print('not')
            break
        else:
            print(n)
else:
    print('not')
