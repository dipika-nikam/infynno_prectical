n = int(input('Enter values'))
li = [12, 44, 8, 98, 64, 16, 20,15,5]
for i in li:
    if i % n == 0:
        print('partner{}'.format(i))
    else:
        print('not partner{}'.format(i))