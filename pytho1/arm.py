n = int(input('Enter value'))
sum = 0
num = n
while n != 0:
    number = n % 10
    sum = sum + (number * number * number)
    n = n // 10

if num == sum:
    print('{} is aram'.format(num))
else:
    print('Not arm')
