n = int(input('Enter value'))
a=0
b=1
if n <= 0:
    print('Enter valid number')

elif n==1:
    print(b)
else:
    for i in range(1,n):
         c = a+b
         a = b
         b=c
         print(b)

